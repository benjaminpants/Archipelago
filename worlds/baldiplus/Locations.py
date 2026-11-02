from BaseClasses import Location
from BaseClasses import LocationProgressType
from typing import NamedTuple
from .Defines import *

baldiplus_base_location_id = 9999300

class BaldiPlusLocation(Location):
    game: str = "Baldi's Basics Plus"

class BaldiPlusLocationData(NamedTuple):
    id: int
    progress: LocationProgressType
    name: str

item_location_table: dict[str, BaldiPlusLocationData] = {
    # Item Obtains
    "BSODA Obtained": BaldiPlusLocationData((baldiplus_base_location_id + 12), LocationProgressType.DEFAULT, "BSODA Obtained"),
    "Zesty Bar Obtained": BaldiPlusLocationData((baldiplus_base_location_id + 13), LocationProgressType.DEFAULT, "Zesty Bar Obtained"),
    "Swinging Door Lock Obtained": BaldiPlusLocationData((baldiplus_base_location_id + 14), LocationProgressType.DEFAULT, "Swinging Door Lock Obtained"),
    "Quarter Obtained": BaldiPlusLocationData((baldiplus_base_location_id + 15), LocationProgressType.DEFAULT, "Quarter Obtained"),
    "Baldi's Least Favorite Tape Obtained": BaldiPlusLocationData((baldiplus_base_location_id + 16), LocationProgressType.DEFAULT, "Baldi's Least Favorite Tape Obtained"),
    "Principal's Keys Obtained": BaldiPlusLocationData((baldiplus_base_location_id + 17), LocationProgressType.DEFAULT, "Principal's Keys Obtained"),
    "WD-NoSquee Obtained": BaldiPlusLocationData((baldiplus_base_location_id + 18), LocationProgressType.DEFAULT, "WD-NoSquee Obtained"),
    "Safety Scissors Obtained": BaldiPlusLocationData((baldiplus_base_location_id + 19), LocationProgressType.DEFAULT, "Safety Scissors Obtained"),
    "Alarm Clock Obtained": BaldiPlusLocationData((baldiplus_base_location_id + 20), LocationProgressType.DEFAULT, "Alarm Clock Obtained"),
    "Techno-Boots Obtained": BaldiPlusLocationData((baldiplus_base_location_id + 21), LocationProgressType.DEFAULT, "Techno-Boots Obtained"),
    "Dangerous Teleporter Obtained": BaldiPlusLocationData((baldiplus_base_location_id + 22), LocationProgressType.DEFAULT, "Dangerous Teleporter Obtained"),
    "Grappling Hook Obtained": BaldiPlusLocationData((baldiplus_base_location_id + 23), LocationProgressType.DEFAULT, "Grappling Hook Obtained"),
    "An Apple For Baldi Obtained": BaldiPlusLocationData((baldiplus_base_location_id + 24), LocationProgressType.DEFAULT, "An Apple For Baldi Obtained"),
    "Dirty Chalk Eraser Obtained": BaldiPlusLocationData((baldiplus_base_location_id + 25), LocationProgressType.DEFAULT, "Dirty Chalk Eraser Obtained"),
    "Principal Whistle Obtained": BaldiPlusLocationData((baldiplus_base_location_id + 26), LocationProgressType.DEFAULT, "Principal Whistle Obtained"),
    "Faculty Nametag Obtained": BaldiPlusLocationData((baldiplus_base_location_id + 27), LocationProgressType.DEFAULT, "Faculty Nametag Obtained"),
    "Portal Poster Obtained": BaldiPlusLocationData((baldiplus_base_location_id + 28), LocationProgressType.DEFAULT, "Portal Poster Obtained"),
    "Diet BSODA Obtained": BaldiPlusLocationData((baldiplus_base_location_id + 29), LocationProgressType.DEFAULT, "Diet BSODA Obtained"),
    "Super Stretchy Glove Obtained": BaldiPlusLocationData((baldiplus_base_location_id + 30), LocationProgressType.DEFAULT, "Super Stretchy Glove Obtained"),
    "Invisibility Elixir Obtained": BaldiPlusLocationData((baldiplus_base_location_id + 31), LocationProgressType.DEFAULT, "Invisibility Elixir Obtained"),
    "'Nana Peel Obtained": BaldiPlusLocationData((baldiplus_base_location_id + 32), LocationProgressType.DEFAULT, "'Nana Peel Obtained"),
    "Green Plus Icon Obtained": BaldiPlusLocationData((baldiplus_base_location_id + 33), LocationProgressType.PRIORITY, "Green Plus Icon Obtained"),
    "Silver Plus Icon Obtained": BaldiPlusLocationData((baldiplus_base_location_id + 34), LocationProgressType.PRIORITY, "Silver Plus Icon Obtained"),
    "Gold Plus Icon Obtained": BaldiPlusLocationData((baldiplus_base_location_id + 35), LocationProgressType.PRIORITY, "Gold Plus Icon Obtained")
}

location_table: dict[str, BaldiPlusLocationData] = {
    "Bus Pass Spawn": BaldiPlusLocationData((baldiplus_base_location_id + 1), LocationProgressType.PRIORITY, "Bus Pass Spawn"),
    "Field Trip Completion": BaldiPlusLocationData((baldiplus_base_location_id + 2), LocationProgressType.PRIORITY, "Field Trip Completion"),
    "Student Reward #1": BaldiPlusLocationData((baldiplus_base_location_id + 3), LocationProgressType.PRIORITY, "Student Reward #1"),
    "Student Reward #2": BaldiPlusLocationData((baldiplus_base_location_id + 4), LocationProgressType.DEFAULT, "Student Reward #2"),
    "Student Reward #3": BaldiPlusLocationData((baldiplus_base_location_id + 5), LocationProgressType.DEFAULT, "Student Reward #3"),
    "Student Reward #4": BaldiPlusLocationData((baldiplus_base_location_id + 6), LocationProgressType.DEFAULT, "Student Reward #4"),
    "Student Reward #5": BaldiPlusLocationData((baldiplus_base_location_id + 7), LocationProgressType.DEFAULT, "Student Reward #5"),
    "1st Gluestick Purchased": BaldiPlusLocationData((baldiplus_base_location_id + 8), LocationProgressType.PRIORITY, "1st Gluestick Purchased"),
    "2nd Gluestick Purchased": BaldiPlusLocationData((baldiplus_base_location_id + 9), LocationProgressType.DEFAULT, "2nd Gluestick Purchased"),
    "3rd Gluestick Purchased": BaldiPlusLocationData((baldiplus_base_location_id + 10), LocationProgressType.DEFAULT, "3rd Gluestick Purchased"),
    "4th Gluestick Purchased": BaldiPlusLocationData((baldiplus_base_location_id + 11), LocationProgressType.DEFAULT, "4th Gluestick Purchased"),

    "Tutorial Running Section Complete": BaldiPlusLocationData((baldiplus_base_location_id + 50), LocationProgressType.PRIORITY, "Tutorial Running Section Complete"),
    "Tutorial Noise Section Complete": BaldiPlusLocationData((baldiplus_base_location_id + 51), LocationProgressType.DEFAULT, "Tutorial Noise Section Complete"),
    "Tutorial Notebook Section Complete": BaldiPlusLocationData((baldiplus_base_location_id + 52), LocationProgressType.DEFAULT, "Tutorial Notebook Section Complete"),
    "Tutorial Item Section Complete": BaldiPlusLocationData((baldiplus_base_location_id + 53), LocationProgressType.DEFAULT, "Tutorial Item Section Complete"),
    "Tutorial Shopping Section Complete": BaldiPlusLocationData((baldiplus_base_location_id + 54), LocationProgressType.PRIORITY, "Tutorial Shopping Section Complete"),
    "Tutorial Complete": BaldiPlusLocationData((baldiplus_base_location_id + 55), LocationProgressType.PRIORITY, "Tutorial Complete"),
    "Speedy Challenge Complete": BaldiPlusLocationData((baldiplus_base_location_id + 56), LocationProgressType.PRIORITY, "Speedy Challenge Complete"),
    "Grapple Challenge Complete": BaldiPlusLocationData((baldiplus_base_location_id + 57), LocationProgressType.PRIORITY, "Grapple Challenge Complete"),
    "Stealthy Challenge Complete": BaldiPlusLocationData((baldiplus_base_location_id + 58), LocationProgressType.PRIORITY, "Stealthy Challenge Complete"),
    "Campfire Frenzy 200 Score": BaldiPlusLocationData((baldiplus_base_location_id + 59), LocationProgressType.PRIORITY, "Campfire Frenzy 200 Score"),
    "Pic-Quick-Nic 1000 Score": BaldiPlusLocationData((baldiplus_base_location_id + 60), LocationProgressType.PRIORITY, "Pic-Quick-Nic 1000 Score"),
    "Field Trip Area Entered": BaldiPlusLocationData((baldiplus_base_location_id + 61), LocationProgressType.PRIORITY, "Field Trip Area Entered"),
    **item_location_table
}

baldiplus_current_location_id = baldiplus_base_location_id + 61
for lap in range(1,baldiplus_laps_total + 1):
    for fnumber in range(1,baldiplus_floors_per_lap + 1):
        baldiplus_current_location_id += 1
        for notebook in range(1, baldiplus_notebookcounts[fnumber - 1] + 1):
            name = f"F{fnumber} {notebook}/{baldiplus_notebookcounts[fnumber - 1]} (Run #{lap})"
            location_table[name] = BaldiPlusLocationData(baldiplus_current_location_id, LocationProgressType.DEFAULT, name)
            baldiplus_current_location_id += 1
        # Do not need to increment id again, as the notebook loop has already done that
        name = f"F{fnumber} Complete (Run #{lap})"#"F" + str(fnumber) + " Complete (Run #" + str(lap) + ")"
        location_table[name] = BaldiPlusLocationData(baldiplus_current_location_id, LocationProgressType.PRIORITY, name)

