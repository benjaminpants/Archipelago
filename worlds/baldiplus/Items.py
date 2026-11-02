from typing import NamedTuple
from BaseClasses import Item, ItemClassification
from .Defines import *

baldiplus_base_id: int = 9999000

class BaldiPlusItem(Item):
    game: str = "Baldi's Basics Plus"

class BaldiPlusItemData(NamedTuple):
    id: int | None = None
    classification: ItemClassification = ItemClassification.filler

# TODO: Remove excess stickers, move student YTPs out of filler? Add small YTP amounts as junk

filler_item_data_table: dict[str, BaldiPlusItemData] = {
    "Random Sticker": BaldiPlusItemData(baldiplus_base_id + 50),
    "Random Bonus Sticker": BaldiPlusItemData(baldiplus_base_id + 51),
    "Quarter": BaldiPlusItemData(baldiplus_base_id + 52),
    "Zesty Bar": BaldiPlusItemData(baldiplus_base_id + 53),
    "10 YTPs": BaldiPlusItemData(baldiplus_base_id + 54),
    "25 YTPs": BaldiPlusItemData(baldiplus_base_id + 55),
    "50 YTPs": BaldiPlusItemData(baldiplus_base_id + 56),
    "3 Second Praise": BaldiPlusItemData(baldiplus_base_id + 57)
}

filler_item_list = list(filler_item_data_table.keys())

useful_item_data_table: dict[str, BaldiPlusItemData] = {
    # Student YTPs
    "100 YTPs (Student Reward #1)": BaldiPlusItemData(baldiplus_base_id + 100, ItemClassification.useful | ItemClassification.deprioritized),
    "125 YTPs (Student Reward #2)": BaldiPlusItemData(baldiplus_base_id + 101, ItemClassification.useful | ItemClassification.deprioritized),
    "150 YTPs (Student Reward #3)": BaldiPlusItemData(baldiplus_base_id + 102, ItemClassification.useful | ItemClassification.deprioritized),
    "175 YTPs (Student Reward #4)": BaldiPlusItemData(baldiplus_base_id + 103, ItemClassification.useful | ItemClassification.deprioritized),
    "200 YTPs (Student Reward #5)": BaldiPlusItemData(baldiplus_base_id + 104, ItemClassification.useful),
}

useful_item_ability_data_table: dict[str, BaldiPlusItemData] = {
    "BSODA Usage": BaldiPlusItemData(baldiplus_base_id + 130, ItemClassification.progression_skip_balancing), # Needed for tutorial
    "Zesty Bar Usage": BaldiPlusItemData(baldiplus_base_id + 131, ItemClassification.progression_skip_balancing), # Needed for tutorial
    "Swinging Door Lock Usage": BaldiPlusItemData(baldiplus_base_id + 132, ItemClassification.useful),
    "Quarter Usage": BaldiPlusItemData(baldiplus_base_id + 133, ItemClassification.progression), # Needed for tutorial
    "Baldi's Least Favorite Tape Usage": BaldiPlusItemData(baldiplus_base_id + 134, ItemClassification.useful),
    "Principal's Keys Usage": BaldiPlusItemData(baldiplus_base_id + 135, ItemClassification.useful),
    "WD-NoSquee Usage": BaldiPlusItemData(baldiplus_base_id + 136, ItemClassification.useful),
    "Safety Scissors Usage": BaldiPlusItemData(baldiplus_base_id + 137, ItemClassification.filler), # Safety Scissors sucks
    "Alarm Clock Usage": BaldiPlusItemData(baldiplus_base_id + 138, ItemClassification.useful),
    "Techno-Boots Usage": BaldiPlusItemData(baldiplus_base_id + 139, ItemClassification.progression_skip_balancing), # Needed for tutorial
    "Dangerous Teleporter Usage": BaldiPlusItemData(baldiplus_base_id + 140, ItemClassification.useful),
    "Grappling Hook Usage": BaldiPlusItemData(baldiplus_base_id + 141, ItemClassification.progression_skip_balancing), # Needed for tutorial
    "An Apple For Baldi Usage": BaldiPlusItemData(baldiplus_base_id + 142, ItemClassification.useful),
    "Dirty Chalk Eraser Usage": BaldiPlusItemData(baldiplus_base_id + 143, ItemClassification.progression_skip_balancing), # Needed for Stealthy Challenge
    "Principal Whistle Usage": BaldiPlusItemData(baldiplus_base_id + 144, ItemClassification.useful),
    "Faculty Nametag Usage": BaldiPlusItemData(baldiplus_base_id + 145, ItemClassification.useful),
    "Portal Poster Usage": BaldiPlusItemData(baldiplus_base_id + 146, ItemClassification.useful),
    "Diet BSODA Usage": BaldiPlusItemData(baldiplus_base_id + 147, ItemClassification.progression), # Important to warrant early game/being a progression item
    "Super Stretchy Glove Usage": BaldiPlusItemData(baldiplus_base_id + 148, ItemClassification.progression_skip_balancing), # Needed for tutorial
    "Invisibility Elixir Usage": BaldiPlusItemData(baldiplus_base_id + 149, ItemClassification.useful),
    "'Nana Peel Usage": BaldiPlusItemData(baldiplus_base_id + 150, ItemClassification.useful)
}

progression_item_data_table: dict[str, BaldiPlusItemData] = {
    "Staminometer": BaldiPlusItemData(baldiplus_base_id + 200, ItemClassification.progression | ItemClassification.useful),
    "Bus Pass": BaldiPlusItemData(baldiplus_base_id + 201, ItemClassification.progression_skip_balancing), # Progression item, but it should be anywhere in the run.
    "Shape Keys Usage": BaldiPlusItemData(baldiplus_base_id + 202, ItemClassification.progression), # Needed since Bus Pas is imp for progression
    # First 2 are progression, last 2 are progression skip balancing, as 3 slots is manageable while 4 and 5 are just nice to haves
    # "Item Slot 2": BaldiPlusItemData(baldiplus_base_id + 203, ItemClassification.progression | ItemClassification.useful),
    # "Item Slot 3": BaldiPlusItemData(baldiplus_base_id + 204, ItemClassification.progression | ItemClassification.useful),
    "Item Slot 4": BaldiPlusItemData(baldiplus_base_id + 205, ItemClassification.progression | ItemClassification.useful),
    "Item Slot 5": BaldiPlusItemData(baldiplus_base_id + 206, ItemClassification.progression | ItemClassification.useful),
    # You should start with Sticker Slot 1 already unlocked for the sake of the game not being absolute hell.
    #"Sticker Slot 1": BaldiPlusItemData(baldiplus_base_id + 207, ItemClassification.progression | ItemClassification.useful),
    "Sticker Slot 2": BaldiPlusItemData(baldiplus_base_id + 208, ItemClassification.progression | ItemClassification.useful),
    "Sticker Slot 3": BaldiPlusItemData(baldiplus_base_id + 209, ItemClassification.progression_skip_balancing | ItemClassification.useful),
    "Sticker Slot 4": BaldiPlusItemData(baldiplus_base_id + 210, ItemClassification.progression_skip_balancing | ItemClassification.useful),

    "Gluestick": BaldiPlusItemData(baldiplus_base_id + 211, ItemClassification.progression_skip_balancing | ItemClassification.useful),
    # "Gluestick 2": BaldiPlusItemData(baldiplus_base_id + 212, ItemClassification.progression_skip_balancing | ItemClassification.useful),
    # "Gluestick 3": BaldiPlusItemData(baldiplus_base_id + 213, ItemClassification.progression_skip_balancing | ItemClassification.useful),
    # "Gluestick 4": BaldiPlusItemData(baldiplus_base_id + 214, ItemClassification.progression_skip_balancing | ItemClassification.useful),
    "Tutorial": BaldiPlusItemData(baldiplus_base_id + 215, ItemClassification.progression),
    "Challenges": BaldiPlusItemData(baldiplus_base_id + 216, ItemClassification.progression),
    "Field Trips": BaldiPlusItemData(baldiplus_base_id + 217, ItemClassification.progression)
}

# These are given to the player whenever they buy a gluestick so I can keep track of how many they have bought
# (For ordering reasons, since you can only buy the next progression gluestick after buying the previous ones)
progress_tracking_item_data_table : dict[str, BaldiPlusItemData] = {
    "Gluestick Purchase #1": BaldiPlusItemData(baldiplus_base_id + 250, ItemClassification.progression),
    "Gluestick Purchase #2": BaldiPlusItemData(baldiplus_base_id + 251, ItemClassification.progression),
    "Gluestick Purchase #3": BaldiPlusItemData(baldiplus_base_id + 252, ItemClassification.progression),
    "Gluestick Purchase #4": BaldiPlusItemData(baldiplus_base_id + 253, ItemClassification.progression),
    "Progressive Floor Unlock": BaldiPlusItemData(baldiplus_base_id + 254, ItemClassification.progression_skip_balancing),
}

baldiplus_item_data_table = {
    **filler_item_data_table,
    **useful_item_data_table,
    **useful_item_ability_data_table,
    **progression_item_data_table,
    **progress_tracking_item_data_table
}

# Initial items in the item pool data table
item_item_pool_init_data_table = {
    **useful_item_data_table,
    **useful_item_ability_data_table,
    **progression_item_data_table
}