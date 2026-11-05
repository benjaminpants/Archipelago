import json
import os
from collections import OrderedDict
wobbledogs_base_id: int = 7878000

wobbledogs_data: dict[str, OrderedDict] = {
}

# TODO: refactor foods.json to have the food source as the base

with open(os.path.join(os.path.dirname(__file__), "achievements.json"), "r") as json_data:
    wobbledogs_data["goals"] = json.load(json_data, object_pairs_hook=OrderedDict)
with open(os.path.join(os.path.dirname(__file__), "flora.json"), "r") as json_data:
    wobbledogs_data["flora"] = json.load(json_data, object_pairs_hook=OrderedDict)
with open(os.path.join(os.path.dirname(__file__), "foods.json"), "r") as json_data:
    wobbledogs_data["food"] = json.load(json_data, object_pairs_hook=OrderedDict)

# DEBUG
"""
for key, value in wobbledogs_data["goals"].items():
    if value.get("requirements") is None:
        continue
    if value["requirements"].get("items") is None:
        continue
    if value["requirements"]["items"].pop("Progressive Instability", None) is not None:
        print("removed stability requirement from:" + key)
"""