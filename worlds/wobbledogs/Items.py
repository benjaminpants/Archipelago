from typing import NamedTuple
from BaseClasses import Item, ItemClassification
from .Defines import wobbledogs_data, wobbledogs_base_id


class WobbledogsItem(Item):
    game: str = "Wobbledogs"


class WobbledogsItemData(NamedTuple):
    id: int | None = None
    classification: ItemClassification | None = ItemClassification.filler

# TODO: Fix! This is ugly!
wobbledogs_always_in_items = [
    "Premium Pebble Floor",
    "Stained Concrete Floor",
    "Prickly Pear",
    "Sample Table",
    "Space Carpet Unlock",
    "Space Wallpaper Unlock",
    "Snowy Carpet",
    "Progressive Digging", "Progressive Digging",
    "Progressive Instability", "Progressive Instability", "Progressive Instability", "Progressive Instability", "Progressive Instability",
    "Progressive Instability", "Progressive Instability", "Progressive Instability", "Progressive Instability", "Progressive Instability",
    "Ghost Summoning",
    "Pooper Scooper",
    "Vacuum",
    "Robotic Vacuum",
    "Clean-up Broom",
    "Randy", "Proto", "Mud", "Granule", "Superior",
    "Dog Pen", "Dog Pen", "Dog Pen", "Dog Pen", "Dog Pen", "Dog Pen", "Dog Pen", "Dog Pen",
    "Storage Chest",
    "Noble Dog Statue",
    "Phonograph",
    "Rock Speaker",
    "Mud Floor",
    "Ground Ivy",
    "Cloud Wallpaper",
    "Arcade Floor",
    "Flower Wallpaper",
    "Doggy Bopper",
    "Industrial Fan",
    "Inflatable Dog",
    "CD Player",
    "Gravity Machine",
    "Jukebox",
    "Road Carpet",
    "Simulated Floor",
    "Strange Plush",
    "Outdoor Flooring",
    "Toilet Paper Roll x10",
    "Dog Stack",
    "Doggy Launcher",
    "Foam Ham",
    "Doggivision Jr",
    "Vine Wallpaper"
]

wobbledogs_item_data_table: dict[str, WobbledogsItemData] = {
    # Food Dispensers
    "Classic Food Dispenser": WobbledogsItemData(wobbledogs_base_id + 0, ItemClassification.progression),
    "Spacelab Food Dispenser": WobbledogsItemData(wobbledogs_base_id + 1, ItemClassification.progression),
    "Suburban Food Dispenser": WobbledogsItemData(wobbledogs_base_id + 2,ItemClassification.progression),
    "Spooky Food Dispenser": WobbledogsItemData(wobbledogs_base_id + 3,ItemClassification.progression),
    "Jungle Food Dispenser": WobbledogsItemData(wobbledogs_base_id + 4,ItemClassification.progression),
    "Dessert Food Dispenser": WobbledogsItemData(wobbledogs_base_id + 5,ItemClassification.progression),
    # Key (still food) related items
    "Premium Pebble Floor": WobbledogsItemData(wobbledogs_base_id + 6,ItemClassification.progression),
    "Stained Concrete Floor": WobbledogsItemData(wobbledogs_base_id + 7,ItemClassification.progression),
    "Prickly Pear": WobbledogsItemData(wobbledogs_base_id + 8,ItemClassification.progression),
    "Sample Table": WobbledogsItemData(wobbledogs_base_id + 9,ItemClassification.progression),
    # Key items for certain goals
    "Space Carpet Unlock": WobbledogsItemData(wobbledogs_base_id + 10,ItemClassification.progression),
    "Space Wallpaper Unlock": WobbledogsItemData(wobbledogs_base_id + 11,ItemClassification.progression),
    "Snowy Carpet": WobbledogsItemData(wobbledogs_base_id + 12,ItemClassification.progression),
    "Mail-in Dog": WobbledogsItemData(wobbledogs_base_id + 13,ItemClassification.progression), # Only applicable if Import Codes are off.
    # Abilities/Tools
    "Progressive Digging": WobbledogsItemData(wobbledogs_base_id + 14,ItemClassification.progression), # Should be 2
    "Progressive Instability": WobbledogsItemData(wobbledogs_base_id + 15,ItemClassification.progression_skip_balancing), # Should be 10
    "Ghost Summoning": WobbledogsItemData(wobbledogs_base_id + 16,ItemClassification.progression),
    "Pooper Scooper": WobbledogsItemData(wobbledogs_base_id + 17,ItemClassification.progression),
    "Vacuum": WobbledogsItemData(wobbledogs_base_id + 18,ItemClassification.progression),
    "Robotic Vacuum": WobbledogsItemData(wobbledogs_base_id + 19,ItemClassification.progression_skip_balancing),
    "Clean-up Broom": WobbledogsItemData(wobbledogs_base_id + 20,ItemClassification.progression_skip_balancing),
    # Dogs
    "Randy": WobbledogsItemData(wobbledogs_base_id + 21,ItemClassification.useful),
    "Proto": WobbledogsItemData(wobbledogs_base_id + 22,ItemClassification.useful),
    "Mud": WobbledogsItemData(wobbledogs_base_id + 23,ItemClassification.useful),
    "Granule": WobbledogsItemData(wobbledogs_base_id + 24,ItemClassification.useful),
    "Superior": WobbledogsItemData(wobbledogs_base_id + 25,ItemClassification.useful),
    # Useful Items
    "Dog Pen": WobbledogsItemData(wobbledogs_base_id + 26,ItemClassification.useful), # Should be 9 of these
    "Storage Chest": WobbledogsItemData(wobbledogs_base_id + 27,ItemClassification.useful),
    # Filler Items
    "Capsule Item": WobbledogsItemData(wobbledogs_base_id + 28,ItemClassification.filler),
    "Dog Egg": WobbledogsItemData(wobbledogs_base_id + 29,ItemClassification.filler),
    "Dog Hunger Refill": WobbledogsItemData(wobbledogs_base_id + 30,ItemClassification.filler),
    "Dog Energy Refill": WobbledogsItemData(wobbledogs_base_id + 31,ItemClassification.filler),
    "Dog Play Refill": WobbledogsItemData(wobbledogs_base_id + 32,ItemClassification.filler),
    # Goal/Achievement exclusive items, "None" here, but will either be filler or deprioritized useful depending on setting
    # Any that are commented out are because they could potentially fuck up progression.
    "Noble Dog Statue": WobbledogsItemData(wobbledogs_base_id + 33,None),
    "Phonograph": WobbledogsItemData(wobbledogs_base_id + 34,None),
    "Rock Speaker": WobbledogsItemData(wobbledogs_base_id + 35,None),
    "Mud Floor": WobbledogsItemData(wobbledogs_base_id + 36,None),
    "Ground Ivy": WobbledogsItemData(wobbledogs_base_id + 37,None),
    "Cloud Wallpaper": WobbledogsItemData(wobbledogs_base_id + 38,None),
    #"Tree x10": WobbledogsItemData(wobbledogs_base_id + 1,None),
    "Arcade Floor": WobbledogsItemData(wobbledogs_base_id + 39,None),
    #"Weed Mix": WobbledogsItemData(wobbledogs_base_id + 1,None),
    "Flower Wallpaper": WobbledogsItemData(wobbledogs_base_id + 40,None),
    "Doggy Bopper": WobbledogsItemData(wobbledogs_base_id + 41,None),
    "Industrial Fan": WobbledogsItemData(wobbledogs_base_id + 42,None),
    #"Alien Wall": WobbledogsItemData(wobbledogs_base_id + 1,None), # TODO: CHECK
    #"Golden Lupine Flowers": WobbledogsItemData(wobbledogs_base_id + 1,None),
    "Inflatable Dog": WobbledogsItemData(wobbledogs_base_id + 43,None),
    "CD Player": WobbledogsItemData(wobbledogs_base_id + 44,None),
    "Gravity Machine": WobbledogsItemData(wobbledogs_base_id + 45,None),
    "Jukebox": WobbledogsItemData(wobbledogs_base_id + 46,None),
    #"Blue Blanket Flowers": WobbledogsItemData(wobbledogs_base_id + 1,None),
    "Road Carpet": WobbledogsItemData(wobbledogs_base_id + 47,None),
    #"Pink Daisy Flowers": WobbledogsItemData(wobbledogs_base_id + 1,None),
    "Simulated Floor": WobbledogsItemData(wobbledogs_base_id + 48,None),
    "Strange Plush": WobbledogsItemData(wobbledogs_base_id + 49,None),
    "Outdoor Flooring": WobbledogsItemData(wobbledogs_base_id + 50,None),
    "Toilet Paper Roll x10": WobbledogsItemData(wobbledogs_base_id + 51,None),
    "Dog Stack": WobbledogsItemData(wobbledogs_base_id + 52,None),
    "Doggy Launcher": WobbledogsItemData(wobbledogs_base_id + 53,None),
    "Foam Ham": WobbledogsItemData(wobbledogs_base_id + 54,None),
    "Doggivision Jr": WobbledogsItemData(wobbledogs_base_id + 55,None),
    "Vine Wallpaper": WobbledogsItemData(wobbledogs_base_id + 56,None),
}

current_id = wobbledogs_base_id + 100 # Give room for about 50 or so extra items if need be

# Add all food items into the pool
for key, value in wobbledogs_data["food"].items():
    if not value["source_randomizable"]: # Non-randomizable items are non-randomizable because they are obtained through non-standard means and thus can't be gated. If they are made randomizable, this check must be changed.
        continue
    wobbledogs_item_data_table[key] = WobbledogsItemData(current_id, ItemClassification.progression)
    current_id += 1

# Add all flora access items into the pool
for key, value in wobbledogs_data["flora"].items():
    wobbledogs_item_data_table[key] = WobbledogsItemData(current_id, ItemClassification.progression)
    current_id += 1