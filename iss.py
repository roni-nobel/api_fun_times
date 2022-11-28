import requests
import pandas as pd
from collections import defaultdict
from datetime import datetime, timezone
# from dateutil.tz import *


def people_per_craft(people):
    people_per_craft_count = defaultdict(int)
    for person in people:
        people_per_craft_count[person["craft"]] += 1
    return people_per_craft_count


def people_list(people):
    df = pd.DataFrame.from_dict(people)
    df['runtime_utc'] = datetime.now(timezone.utc)
    # df['runtime_local'] = datetime.now(tzlocal())
    return df.to_string()


response = requests.get('http://api.open-notify.org/astros.json')
dataset = response.json()
# print(people_per_craft(dataset["people"]))
print(people_list(dataset["people"]))
