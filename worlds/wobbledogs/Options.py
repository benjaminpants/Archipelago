from dataclasses import dataclass
from .Defines import wobbledogs_data
from Options import Toggle, Range, Choice, PerGameCommonOptions, OptionSet

class AllowDogImporting(Toggle):
    """If importing dogs should be allowed, if False, a random dog(Mail-in Dog) is put into the item pool that grants the \"Mail Time\" goal."""
    display_name = "Allow Dog Importing"
    default = False

class FloraEffectSanity(Toggle):
    """If the completion of a flora's field guide effects page should be a check."""
    display_name = "Flora Effect-sanity"
    default = True

class FloraOccurrenceSanity(Toggle):
    """If the completion of a flora's field guide occurrence page should be a check."""
    display_name = "Flora Occurrence-sanity"
    default = False

class FloraLock(Toggle):
    """If Flora should be locked behind items found in the multi-world. May cause a generation failure if generating solo."""
    display_name = "Flora-Lock"
    default = False

class ClearCondition(Choice):
    """The clear condition for the game.
    All Goals means you must have every single goal completed to win.
    Specific Goals means you must have every goal in specific_goal_goals completed to win.
    Goal Percentage means you must have the percentage specified in goal_percentage completed to win.
    Dog Match means the game will generate an amount of dogs for you to attempt to match. TODO POLISH THIS MESSAGE
    """
    display_name = "Clear Condition"
    option_all_goals = 0
    option_specific_goals = 1
    option_goal_percentage = 2
    option_dog_match = 3
    default = 0

class PercentageGoalPercentage(Range):
    """The percentage of goals that must be completed to win if the clear condition is set to goal percentage"""
    display_name = "Percentage Goal Percentage"
    range_start = 0
    range_end = 100
    default = 80

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
    option_none = 0
    option_colors = 1
    option_full = 2
    default = 0

@dataclass
class WobbleDogsOptions(PerGameCommonOptions):
    random_starting_food_dispenser: RandomizeStartingFoodDispenser
    random_default_dog: DefaultDogRandomization
    clear_condition: ClearCondition
    specific_goal_goals: SpecificGoalClearSelectedGoals
    goal_percentage: PercentageGoalPercentage
    allow_imports: AllowDogImporting
    flora_effect_sanity: FloraEffectSanity
    flora_occurrence_sanity: FloraOccurrenceSanity
    flora_lock: FloraLock
