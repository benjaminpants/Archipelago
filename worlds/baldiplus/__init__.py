import logging

from BaseClasses import Region
from .Items import *
from .Locations import *
from .Options import *
from worlds.AutoWorld import World, WebWorld


class BaldiPlusWeb(WebWorld):
    tutorials = []

# TODO: how to add softlock prevention to bus pass spawn. Allow it in endless mode? Allow for replaying levels?
# TODO: Do not allow our progression items to be placed in the last level! This is stupid!
class BaldiPlusWorld(World):
    """Baldi's Basics Plus is an active stealth roguelike that parodies cheap '90s edutainment with a subtle horror twist!
    Try to collect all the notebooks in each level as Baldi uses his incredible hearing to track you down in a game of "Hide & Seek"."""

    game = "Baldi's Basics Plus"

    options_dataclass = BaldiPlusOptions
    options = BaldiPlusOptions

    item_name_to_id = {}
    location_name_to_id = {}
    # Closest possible to locations existing at multiple places

    for key, value in baldiplus_item_data_table.items():
        item_name_to_id[key] = value.id

    for key, value in location_table.items():
        location_name_to_id[key] = value.id

    web = BaldiPlusWeb()

    def __init__(self, multiworld: "MultiWorld", player: int):
        super().__init__(multiworld, player)
        self.item_name_to_region = {}

        self.pitstop_region: Region
        self.field_trip_region: Region

    def create_item(self, name: str):
        return BaldiPlusItem(name, baldiplus_item_data_table[name].classification, self.item_name_to_id[name], self.player)

    def create_location_from_name(self, name: str, parent: Region, access_rule = None):
        created_local = BaldiPlusLocation(self.player, location_table[name].name, location_table[name].id, parent)
        created_local.progress_type = location_table[name].progress
        if access_rule is not None:
            created_local.access_rule = access_rule
        return created_local

    # TODO: FIX! THIS CRASHES!
    def get_filler_item_name(self) -> str:
        # Most filler items should be 10 YTPs
        if self.random.randrange(1, 5) != 1:
            return "10 YTPs"
        return self.random.choice(filler_item_list)

    starting_early_items = ["Diet BSODA Usage", "'Nana Peel Usage", "Dirty Chalk Eraser Usage"]

    def create_items(self) -> None:
        # Choose a random item to give early game so you aren't doing an itemless run
        self.multiworld.local_early_items[self.player][self.random.choice(self.starting_early_items)] = 1
        itempool = [self.create_item(item_name) for item_name in item_item_pool_init_data_table.keys()]
        itempool.extend([self.create_item("Gluestick"),self.create_item("Gluestick"),self.create_item("Gluestick")]) # a gluestick is already added into the pool via previous call

        unfilled_item_count = len(self.multiworld.get_unfilled_locations(self.player))

        # Fill the item pool with the 10 YTPs we'd normally get from collecting notebooks
        for l in range(1, baldiplus_laps_total + 1):
            for i in range(1, baldiplus_floors_per_lap + 1):
                if l != 1 or i != 1: # We are always able to play F1
                    itempool.append(self.create_item("Progressive Floor Unlock"))
                for n in range(1, baldiplus_notebookcounts[i - 1] + 1):
                    if i == 1 and (unfilled_item_count - len(itempool) > 0): # Don't add more filler items than unfilled items
                        itempool.append(self.create_item("25 YTPs"))

        # Fill remaining with filler item
        filler_count = unfilled_item_count - len(itempool)
        itempool.extend(self.create_item(self.get_filler_item_name()) for _ in range(filler_count))

        self.multiworld.itempool.extend(itempool)

    def create_item_regions(self):
        for key in item_location_table.keys():
            fixed_key = key.removesuffix(" Obtained")
            created_region = Region(fixed_key, self.player, self.multiworld)
            created_region.locations.append(self.create_location_from_name(key, created_region))
            self.item_name_to_region[fixed_key] = created_region
            self.multiworld.regions.append(created_region)

    def connect_item_regions_to(self, item_list, region: Region):
        for itm in item_list:
            region.connect(self.item_name_to_region[itm])

    def create_regions(self) -> None:
        menu_region = Region("Menu", self.player, self.multiworld)
        self.multiworld.regions.append(menu_region)

        self.pitstop_region = Region("Pitstop", self.player, self.multiworld)
        self.multiworld.regions.append(self.pitstop_region)

        student_region = Region("Students", self.player, self.multiworld)
        student_region.locations.append(self.create_location_from_name("Student Reward #1", student_region))
        student_region.locations.append(self.create_location_from_name("Student Reward #2", student_region))
        student_region.locations.append(self.create_location_from_name("Student Reward #3", student_region))
        student_region.locations.append(self.create_location_from_name("Student Reward #4", student_region))
        student_region.locations.append(self.create_location_from_name("Student Reward #5", student_region))
        self.multiworld.regions.append(student_region)

        locked_faculty_region = Region("Locked Faculty", self.player, self.multiworld)
        locked_faculty_region.locations.append(self.create_location_from_name("Bus Pass Spawn", locked_faculty_region))
        self.multiworld.regions.append(locked_faculty_region)

        self.field_trip_region = Region("Field Trip", self.player, self.multiworld)
        self.multiworld.regions.append(self.field_trip_region)
        self.field_trip_region.locations.append(self.create_location_from_name("Field Trip Completion", self.field_trip_region, lambda state: state.has("Bus Pass", self.player))) # Field Trips mode gives you the win if you get the high score, but ONLY if you have the bus pass.
        self.field_trip_region.locations.append(self.create_location_from_name("Campfire Frenzy 200 Score", self.field_trip_region, lambda state: state.has("Field Trips", self.player)))
        self.field_trip_region.locations.append(self.create_location_from_name("Pic-Quick-Nic 1000 Score", self.field_trip_region, lambda state: state.has("Field Trips", self.player)))

        trip_enter_local = self.create_location_from_name("Field Trip Area Entered", self.field_trip_region)
        trip_enter_local.place_locked_item(self.create_item("Field Trips"))
        self.field_trip_region.locations.append(trip_enter_local)
        self.pitstop_region.connect(self.field_trip_region, None, lambda state: state.has("Bus Pass", self.player))
        menu_region.connect(self.field_trip_region, None, lambda state: state.has("Field Trips", self.player))

        # Gluestick purchase events
        gluestick_purchase_event = BaldiPlusLocation(self.player, "Purchase Gluestick #1", None, self.pitstop_region)
        gluestick_purchase_event.place_locked_item(BaldiPlusItem("Gluestick Purchase",ItemClassification.progression, None, self.player))
        gluestick_purchase_event.show_in_spoiler = False
        self.pitstop_region.locations.append(gluestick_purchase_event)
        gluestick_purchase_event = BaldiPlusLocation(self.player, "Purchase Gluestick #2", None, self.pitstop_region)
        gluestick_purchase_event.place_locked_item(BaldiPlusItem("Gluestick Purchase", ItemClassification.progression, None, self.player))
        gluestick_purchase_event.show_in_spoiler = False
        self.pitstop_region.locations.append(gluestick_purchase_event)
        gluestick_purchase_event = BaldiPlusLocation(self.player, "Purchase Gluestick #3", None, self.pitstop_region)
        gluestick_purchase_event.place_locked_item(BaldiPlusItem("Gluestick Purchase", ItemClassification.progression, None, self.player))
        gluestick_purchase_event.show_in_spoiler = False
        self.pitstop_region.locations.append(gluestick_purchase_event)
        gluestick_purchase_event = BaldiPlusLocation(self.player, "Purchase Gluestick #4", None, self.pitstop_region)
        gluestick_purchase_event.place_locked_item(BaldiPlusItem("Gluestick Purchase", ItemClassification.progression, None, self.player))
        gluestick_purchase_event.show_in_spoiler = False
        self.pitstop_region.locations.append(gluestick_purchase_event)

        # Actual purchase locations
        self.pitstop_region.locations.append(self.create_location_from_name("1st Gluestick Purchased", self.pitstop_region, lambda state: state.has("Gluestick Purchase", self.player, 1)))
        self.pitstop_region.locations.append(self.create_location_from_name("2nd Gluestick Purchased", self.pitstop_region, lambda state: state.has("Gluestick Purchase", self.player, 2)))
        self.pitstop_region.locations.append(self.create_location_from_name("3rd Gluestick Purchased", self.pitstop_region, lambda state: state.has("Gluestick Purchase", self.player, 3)))
        self.pitstop_region.locations.append(self.create_location_from_name("4th Gluestick Purchased", self.pitstop_region, lambda state: state.has("Gluestick Purchase", self.player, 4)))

        self.create_item_regions()

        self.multiworld.completion_condition[self.player] = lambda state: state.has(f"F{baldiplus_floors_per_lap} R{baldiplus_laps_total} Victory", self.player)

        # Handle it here.
        for l in range(1, baldiplus_laps_total + 1):
            for f in range(1, baldiplus_floors_per_lap + 1):
                f_region = self.create_floor_region(f, l)
                if l == 1 and f == 1:
                    menu_region.connect(f_region)
                else:
                    f_region.connect(student_region)
                    f_region.connect(locked_faculty_region, None, lambda state: state.has("Shape Keys Usage", self.player))

        # Challenges
        challenges_region = Region("Challenges", self.player, self.multiworld)
        menu_region.connect(challenges_region, None, lambda state: state.has("Challenges", self.player))

        # Grapple Challenge
        grapple_challenge_region = Region("Grapple Challenge", self.player, self.multiworld)
        challenges_region.connect(grapple_challenge_region, None, lambda state: state.has("Grappling Hook Usage", self.player)) # You can't even move in grapple challenge without the hook
        grapple_challenge_region.locations.append(self.create_location_from_name("Grapple Challenge Complete", grapple_challenge_region))
        self.connect_item_regions_to(["An Apple For Baldi", "WD-NoSquee", "Swinging Door Lock", "BSODA", "Quarter"], grapple_challenge_region)

        # Speedy Challenge
        speedy_challenge_region = Region("Speedy Challenge", self.player, self.multiworld)
        challenges_region.connect(speedy_challenge_region) # You can enter without running, but you can't win
        speedy_challenge_region.locations.append(self.create_location_from_name("Speedy Challenge Complete", speedy_challenge_region, lambda state: state.has("Staminometer", self.player) and state.has("Quarter Usage", self.player)))
        self.connect_item_regions_to(["BSODA", "Quarter"], speedy_challenge_region) # TODO: Check if BSODA is reachable without running

        # Stealthy Challenge
        stealthy_challenge_region = Region("Stealthy Challenge", self.player, self.multiworld)
        challenges_region.connect(stealthy_challenge_region)  # You can enter without running, but you can't win
        stealthy_challenge_region.locations.append(self.create_location_from_name("Stealthy Challenge Complete", stealthy_challenge_region, lambda state: state.has("Staminometer", self.player) and state.has("Dirty Chalk Eraser Usage", self.player)))
        self.connect_item_regions_to(["Dirty Chalk Eraser", "Zesty Bar"], stealthy_challenge_region)  # The zesty bar is reachable without running

        # Tutorial
        tutorial_region = Region("Tutorial", self.player, self.multiworld)

        self.multiworld.regions.append(tutorial_region)
        menu_region.connect(tutorial_region, None, lambda state: state.has("Tutorial", self.player))

        # Running Section
        tutorial_running_section_region = Region("Tutorial Running Section", self.player, self.multiworld)
        tutorial_region.connect(tutorial_running_section_region, None, lambda state: state.has("Staminometer", self.player))
        tutorial_running_section_region.locations.append(self.create_location_from_name("Tutorial Running Section Complete", tutorial_running_section_region))
        self.multiworld.regions.append(tutorial_running_section_region)

        # None of these sections have any requirements so
        tutorial_mid_section_region = Region("Tutorial Mid Section", self.player, self.multiworld)
        tutorial_running_section_region.connect(tutorial_mid_section_region)
        tutorial_mid_section_region.locations.extend([self.create_location_from_name("Tutorial Noise Section Complete", tutorial_mid_section_region), self.create_location_from_name("Tutorial Notebook Section Complete", tutorial_mid_section_region)])
        self.multiworld.regions.append(tutorial_mid_section_region)

        # We need to be able to use the quarter and BSODA
        tutorial_item_section = Region("Tutorial Item Section", self.player, self.multiworld)
        tutorial_mid_section_region.connect(tutorial_item_section, None, lambda state: state.has("BSODA Usage", self.player) and state.has("Quarter Usage", self.player))
        tutorial_item_section.locations.append(self.create_location_from_name("Tutorial Item Section Complete", tutorial_item_section))
        self.multiworld.regions.append(tutorial_item_section)

        # We need to be able to use one of the pitstop items, and from there, no more requirements.
        tutorial_shop_section = Region("Tutorial Shopping Section", self.player, self.multiworld)
        tutorial_item_section.connect(tutorial_shop_section, None, lambda state: state.has("Zesty Bar Usage", self.player) or state.has("Techno-Boots Usage", self.player) or state.has("Grappling Hook Usage", self.player) or state.has("Super Stretchy Glove Usage", self.player))
        tutorial_shop_section.locations.extend([self.create_location_from_name("Tutorial Shopping Section Complete", tutorial_shop_section), self.create_location_from_name("Tutorial Complete", tutorial_shop_section)])
        self.connect_item_regions_to(["Green Plus Icon", "Silver Plus Icon", "Gold Plus Icon", "Zesty Bar", "Grappling Hook", "Techno-Boots", "Super Stretchy Glove"], tutorial_shop_section)
        self.multiworld.regions.append(tutorial_shop_section)


    # We need later laps to be seperate regions, but everything else is the same
    def create_floor_region(self, number, lap) -> Region:
        f_region = Region(f"F{number} (Run #{lap})", self.player, self.multiworld)
        for notebook in range(1, baldiplus_notebookcounts[number - 1] + 1):
            f_region.locations.append(self.create_location_from_name(f"F{number} {notebook}/{baldiplus_notebookcounts[number - 1]} (Run #{lap})", f_region))

        f_region.locations.append(self.create_location_from_name(f"F{number} Complete (Run #{lap})", f_region))
        # We have a location for completing the floor, but since we want a random item to be given upon its completion, we will use an event for tracking its completion during generation time
        floor_complete_event = BaldiPlusLocation(self.player, f"F{number} (Run #{lap}) Completion", None, f_region)
        floor_complete_event.place_locked_item(BaldiPlusItem(f"F{number} R{lap} Victory", ItemClassification.progression, None, self.player))
        floor_complete_event.show_in_spoiler = False
        f_region.locations.append(floor_complete_event)
        # You must complete the floor to go to the pitstop
        f_region.connect(self.pitstop_region, None, lambda state: state.has(f"F{number} R{lap} Victory", self.player))
        # You must have completed the previous level to enter this one from the pitstop
        amount_of_progress_items_required = (((lap - 1) * baldiplus_floors_per_lap) + number)-1
        if number == 1 and lap == 1:
            self.pitstop_region.connect(f_region, None)
        elif number == 1:
            self.pitstop_region.connect(f_region, None, lambda state: state.has(f"F{baldiplus_floors_per_lap} R{lap - 1} Victory", self.player) and state.has("Progressive Floor Unlock", self.player, amount_of_progress_items_required))
        elif number > 2: # Floors 4 and 5 may require stamina due to conveyor belts (This is a stretch, but I want it to be guranteed you have the staminometer by these floors so they aren't complete hell)
            self.pitstop_region.connect(f_region, None, lambda state: state.has(f"F{number - 1} R{lap} Victory", self.player) and state.has("Progressive Floor Unlock", self.player, amount_of_progress_items_required) and state.has("Staminometer", self.player))
        else:
            self.pitstop_region.connect(f_region, None, lambda state: state.has(f"F{number - 1} R{lap} Victory", self.player) and state.has("Progressive Floor Unlock", self.player, amount_of_progress_items_required))

        self.connect_item_regions_to(baldiplus_floor_items[number - 1], f_region)
        self.multiworld.regions.append(f_region)
        return f_region