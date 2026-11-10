from typing import NamedTuple
from .Defines import wobbledogs_data, wobbledogs_base_id
from BaseClasses import Location, LocationProgressType

class WobbledogsLocation(Location):
    game: str = "Wobbledogs"

class WobbledogsLocationData(NamedTuple):
    id: int
    progress: LocationProgressType

wobbledogs_location_table: dict[str, WobbledogsLocationData] = {
    "Tutorial Food Dispenser Section": WobbledogsLocationData(wobbledogs_base_id + 300, LocationProgressType.DEFAULT) # This location should always get prefilled with a random food dispenser
}

current_id = wobbledogs_base_id + 301

# Add every Goal/Achievement as a location
for key, value in wobbledogs_data["goals"].items():
    wobbledogs_location_table[key] = WobbledogsLocationData(current_id, LocationProgressType.PRIORITY if value["priority"] else LocationProgressType.DEFAULT)
    current_id = current_id + 1

# Add every flora completion as a location for use with Florasanity
for key, value in wobbledogs_data["flora"].items():
    wobbledogs_location_table[key + " Guide Page Effects Completed"] = WobbledogsLocationData(current_id, LocationProgressType.DEFAULT)
    current_id = current_id + 1

for key, value in wobbledogs_data["flora"].items():
    wobbledogs_location_table[key + " Guide Page Occurrences Completed"] = WobbledogsLocationData(current_id, LocationProgressType.DEFAULT)
    current_id = current_id + 1