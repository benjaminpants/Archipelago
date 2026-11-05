from dataclasses import dataclass
from .Defines import wobbledogs_data
from Options import Toggle, Range, Choice, PerGameCommonOptions, OptionSet

class AllowDogImporting(Toggle):
    """If importing dogs should be allowed, if False, a random dog(Mail-in Dog) is put into the item pool that grants the \"Mail Time\" goal."""
    display_name = "Allow Dog Importing"
    default = False

class FloraSanity(Toggle):
    """If the completion of a flora's field guide page should be a check."""
    display_name = "Flora-sanity"
    default = True

class FloraLock(Toggle):
    """If Flora should be locked behind items found in the multi-world. Will cause a generation failure if generating solo."""
    display_name = "Flora-Lock"
    default = False

class ClearCondition(Choice):
    """The clear condition for the game."""
    display_name = "Clear Condition"
    option_all_goals = 0
    option_specific_goals = 1
    option_dog_match = 2
    default = 0

class SpecificGoalClearSelectedGoals(OptionSet):
    """Which goals/achievements should be counted for the Specific Goals clear condition"""
    default = {"A Bit More Wobbly", "Ancient", "Bigheaded", "Flat", "Leggy", "Long", "One Winged Angel", "Peabrained", "Short", "Small", "Spindly", "Take To The Skies!", "Two Faced", "What's This?", "Wide", "Worm", "More of Them!"}
    valid_keys = wobbledogs_data["goals"].keys()

class RandomizeStartingFoodDispenser(Toggle):
    """Randomizes the Food Dispenser you get during the tutorial"""
    display_name = "Randomize Starting Food Dispenser"

class DefaultDogRandomization(Choice):
    """Determines if the default dog is randomized, and by how much. Also effects the \"Default Coloration\" mutator"""
    display_name = "Default Dog Randomization"
    option_off = 0,
    option_colors = 1,
    option_full = 2,
    default = 0

@dataclass
class WobbleDogsOptions(PerGameCommonOptions):
    random_starting_food_dispenser: RandomizeStartingFoodDispenser
    random_default_dog: DefaultDogRandomization
    clear_condition: ClearCondition
    specific_goal_goals: SpecificGoalClearSelectedGoals
    allow_imports: AllowDogImporting
    flora_sanity: FloraSanity
    flora_lock: FloraLock
