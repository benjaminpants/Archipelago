import logging
import copy
from collections import OrderedDict
from BaseClasses import Region, ItemClassification, MultiWorld, CollectionState, LocationProgressType
from .Options import *
from .Items import wobbledogs_item_data_table, wobbledogs_always_in_items, WobbledogsItem
from .Locations import wobbledogs_location_table, WobbledogsLocation
from .Defines import wobbledogs_data
from worlds.AutoWorld import World, WebWorld

# TODO: replace dummy food dispenser code with actual code that stores a food dispenser list, takes one during the region making process and saves the rest for the item pool filling
# TODO: implement flora regions and flora locations, alongside events for the individual mutators
# TODO: implement all the randomizations
class WobbleDogsWorld(World):
    """Wobbledogs is a 3D pet simulation where you raise your own personal hive of rapidly mutating dogs, physically simulated all the way down to their guts!"""

    game = "Wobbledogs"

    options_dataclass = WobbleDogsOptions
    options = WobbleDogsOptions

    item_name_to_id = {}
    location_name_to_id = {}

    for key, value in wobbledogs_item_data_table.items():
        item_name_to_id[key] = value.id

    for key, value in wobbledogs_location_table.items():
        location_name_to_id[key] = value.id

    def __init__(self, multiworld: MultiWorld, player: int):
        super().__init__(multiworld, player)
        self.chosen_starting_dispenser = None
        self.local_wobbledogs_data: dict[str, OrderedDict] = None
        self.home_region = None
        self.available_food_dispensers = ["Classic Food Dispenser", "Spacelab Food Dispenser", "Suburban Food Dispenser", "Spooky Food Dispenser", "Jungle Food Dispenser", "Dessert Food Dispenser"]

    def create_item(self, name: str):
        classification = wobbledogs_item_data_table[name].classification
        if classification is None:
            classification = ItemClassification.filler # TODO: In future, this will be determined by a setting
        return WobbledogsItem(name, classification, wobbledogs_item_data_table[name].id, self.player)

    def create_location_from_name(self, name: str, parent: Region, access_rule=None):
        created_local = WobbledogsLocation(self.player, name, wobbledogs_location_table[name].id, parent)
        created_local.progress_type = wobbledogs_location_table[name].progress
        if access_rule is not None:
            created_local.access_rule = access_rule
        return created_local

    def get_filler_item_name(self) -> str:
        if self.random.randrange(1,12) == 1:
            return "Dog Egg"
        if self.random.randrange(1,30) == 1:
            return self.random.choice(["Dog Hunger Refill", "Dog Energy Refill", "Dog Play Refill"])
        return "Capsule Item"

    # TODO: perform randomization here!
    def generate_early(self) -> None:
        self.local_wobbledogs_data = copy.deepcopy(wobbledogs_data)

    def create_items(self) -> None:
        self.multiworld.local_early_items[self.player]["Progressive Instability"] = 2 # Please
        item_pool = [self.create_item(item_name) for item_name in wobbledogs_always_in_items]
        if not self.options.allow_imports:
            item_pool.append(self.create_item("Mail-in Dog"))

        # Add the remaining food dispensers (one should have been popped for the tutorial)
        item_pool.extend(self.create_item(item_name) for item_name in self.available_food_dispensers)

        # Add the appropriate food items
        for key, value in self.local_wobbledogs_data["food"].items():
            if not value["source_randomizable"]:  # Non-randomizable items are non-randomizable because they are obtained through non-standard means and thus can't be gated. If they are made randomizable, this check must be changed.
                continue
            if value["default"]:
                print(key + " is default, adding.")
                self.multiworld.push_precollected(self.create_item(key))
            else:
                print(key + " excluded because not default.")
                item_pool.append(self.create_item(key))

        # Add the appropriate flora access items
        for key, value in self.local_wobbledogs_data["flora"].items():
            print("pushing precollected:" + key)
            self.multiworld.push_precollected(self.create_item(key))


        unfilled_item_count = len(self.multiworld.get_unfilled_locations(self.player))


        # Fill remaining with filler item
        filler_count = unfilled_item_count - len(item_pool)
        item_pool.extend(self.create_item(self.get_filler_item_name()) for _ in range(filler_count))

        self.multiworld.itempool.extend(item_pool)

    def add_event_to_region(self, event_name: str, event_item_name: str, region: Region, access_rules = None):
        created_event = WobbledogsLocation(self.player, event_name, None, region)
        if access_rules is not None:
            created_event.access_rule = access_rules
        created_event.show_in_spoiler = False
        created_event.place_locked_item(WobbledogsItem(event_item_name, ItemClassification.progression, None, self.player))
        created_event.progress_type = LocationProgressType.PRIORITY
        region.locations.append(created_event)

    def create_food_dispenser_regions(self, name: str, flora_regions: dict[str, Region], parent: Region):
        dispenser_region = Region(name, self.player, self.multiworld)
        self.multiworld.regions.append(dispenser_region)
        print("Created: " + str(dispenser_region))
        # state.has("Progressive Digging", self.player, 2)
        # if name == "Premium Pebble Floor" or name == "Stained Concrete Floor" or name == "Snowy Carpet":
        parent.connect(dispenser_region, "Use " + name, lambda state: state.has(name, self.player))

        # This whole thing is bad and is a reason why I must refactor the food JSON to have the food sources as the main keys
        for key, value in self.local_wobbledogs_data["food"].items():
            if value["source"] != name:
                continue
            print("Adding " + key + " to: " + name)
            requires_digging_level = 0
            # TODO: replace! YUCK!
            if key == "Snowball" or key == "Dirt Clump":
                requires_digging_level = 1
            elif name == "Premium Pebble Floor" or name == "Stained Concrete Floor" or name == "Snowy Carpet":
                requires_digging_level = 2

            food_region = self.create_food_region(key, flora_regions)
            if requires_digging_level > 0:
                dispenser_region.connect(food_region, None, lambda state: state.has("Progressive Digging", self.player, requires_digging_level))
            else:
                if self.item_name_to_id.get(key) is None:
                    dispenser_region.connect(food_region, None)
                else:
                    dispenser_region.connect(food_region, None, lambda state: state.has(key, self.player, 1))

            food_region.connect(dispenser_region)



    def create_flora_region(self, name: str):
        flora_region = Region(name, self.player, self.multiworld)
        self.add_event_to_region(name + " Flora Found", "Gut Flora", flora_region)
        effect_num = 0
        for mutator, _ in self.local_wobbledogs_data["flora"][name].items():
            effect_num += 1
            self.add_event_to_region(name + " Effect #" + str(effect_num), mutator, flora_region)
        self.multiworld.regions.append(flora_region)

        if self.options.sanity_flora:
            flora_region.locations.append(self.create_location_from_name(name + " Guide Page Completed", flora_region))

        # Pretty sure this does nothing
        # flora_region.connect(self.home_region)

        return flora_region

    def create_food_region(self, name: str, flora_regions: dict[str, Region]):
        food_region = Region(name, self.player, self.multiworld)
        self.multiworld.regions.append(food_region)
        food_data = self.local_wobbledogs_data["food"][name]

        # Uncomment to see the horrors.
        # self.add_event_to_region(name + " Food Found", name + " Food Found", food_region)

        for flora in food_data["flora"]:
            food_region.connect(flora_regions[flora])

        return food_region

    def goal_access_rule(self, data, state: CollectionState) -> bool:
        # print("got:" + str(data))
        ret = True
        item_requirements = data["requirements"].get("items")
        if item_requirements is not None and len(item_requirements) > 0:
            ret &= state.has_all_counts(item_requirements, self.player)

        mutator_requirements = data["requirements"].get("mutators")
        if mutator_requirements is not None and len(mutator_requirements) > 0:
            ret &= state.has_all(mutator_requirements, self.player)

        item_or_requirements = data["requirements"].get("items_or")
        if item_or_requirements is not None and len(item_or_requirements) > 0:
            ret &= state.has_any_count(item_or_requirements, self.player)

        mutator_or_requirements = data["requirements"].get("mutators_or")
        if mutator_or_requirements is not None and len(mutator_or_requirements) > 0:
            ret &= state.has_any(mutator_or_requirements, self.player)

        if data["requirements"].get("all_flora"):
            ret &= state.has("Gut Flora", self.player, len(self.local_wobbledogs_data["flora"].keys()))

        return ret

    # Create all the regions and locations we need, the data should already be randomized.
    def create_regions(self) -> None:
        if self.options.clear_condition == 0:
            self.multiworld.completion_condition[self.player] = lambda state: state.has("Goal Completion", self.player, len(self.local_wobbledogs_data["goals"].keys()))
        else:
            raise Exception("Unimplemented Clear Condition: " + self.options.clear_condition)

        menu_region = Region("Menu", self.player, self.multiworld)
        self.multiworld.regions.append(menu_region)

        self.home_region = Region("Home", self.player, self.multiworld)
        self.multiworld.regions.append(self.home_region)
        menu_region.connect(self.home_region)

        tutorial_food_location = self.create_location_from_name("Tutorial Food Dispenser Section", self.home_region)
        tutorial_food_location.place_locked_item(self.create_item(self.available_food_dispensers.pop(0 if not self.options.random_starting_food_dispenser else self.random.randrange(0, len(self.available_food_dispensers)))))
        self.home_region.locations.append(tutorial_food_location)

        # Add all achievement/goal locations
        for key, value in self.local_wobbledogs_data["goals"].items():
            # Create access rule based off of the items, items_or, mutators, and mutators_or fields, all of which are combined using and, meaning you can't do logic that requires items OR mutators.
            # But I doubt that will ever be a problem
            access_rule = lambda state, current_access_value=value: self.goal_access_rule(current_access_value, state)

            # Create a region for the goal, add it, and then add the appropriate location
            goal_region = Region(key, self.player, self.multiworld)
            self.multiworld.regions.append(goal_region)
            if value.get("requirements") is None:
                self.home_region.connect(goal_region, None)
            else:
                self.home_region.connect(goal_region, None, access_rule)

            goal_region.locations.append(self.create_location_from_name(key, self.home_region))
            self.add_event_to_region(key + " Completed", "Goal Completion", goal_region)

        # Create all flora regions
        flora_regions: dict[str, Region] = {}
        for key, _ in self.local_wobbledogs_data["flora"].items():
            flora_regions[key] = self.create_flora_region(key)

        # Add flora not obtainable through food items
        self.home_region.connect(flora_regions["Candida Neutralia"])
        self.home_region.connect(flora_regions["Bacillus Vitus"])

        # Create all food dispenser-esc regions
        food_givers = ["Classic Food Dispenser", "Dessert Food Dispenser", "Spacelab Food Dispenser", "Suburban Food Dispenser", "Spooky Food Dispenser", "Jungle Food Dispenser", "Snowy Carpet", "Sample Table", "Premium Pebble Floor", "Stained Concrete Floor", "Prickly Pear"]
        for giver in food_givers:
            self.create_food_dispenser_regions(giver, flora_regions, self.home_region)

        # Handle other food connections
        # HOW IS THIS FAILING
        self.home_region.connect(self.create_food_region("Baby Tooth", flora_regions))
        self.home_region.connect(self.create_food_region("Half-Eaten Food", flora_regions))
        self.home_region.connect(self.create_food_region("Empty Cocoon", flora_regions))
        self.home_region.connect(self.create_food_region("Ectoplasm", flora_regions))
        self.home_region.connect(self.create_food_region("Dog Parts", flora_regions))
        self.home_region.connect(self.create_food_region("Dud Egg", flora_regions))
        self.home_region.connect(self.create_food_region("Poop", flora_regions))
        self.home_region.connect(self.create_food_region("Dirt Clump", flora_regions), None, lambda state: state.has("Progressive Digging", self.player, 1))
