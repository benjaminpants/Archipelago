import json
import os
import pkgutil
from collections import OrderedDict
wobbledogs_base_id: int = 7878000

wobbledogs_data: dict[str, OrderedDict] = {
}

# TODO: refactor foods.json to have the food source as the base

wobbledogs_data["goals"] = json.loads(pkgutil.get_data(__name__, "achievements.json"), object_pairs_hook=OrderedDict)
wobbledogs_data["flora"] = json.loads(pkgutil.get_data(__name__, "flora.json"), object_pairs_hook=OrderedDict)
wobbledogs_data["food"] = json.loads(pkgutil.get_data(__name__, "foods.json"), object_pairs_hook=OrderedDict)