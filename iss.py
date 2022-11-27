import requests
import pandas as pd
from datetime import datetime, timezone
from dateutil.tz import *


class Astros:
    def __init__(self, message, number, people):
        self.message = message
        self.number = number
        self.people = people


def people_per_craft(people):
    people_per_craft_count = {}
    for i in people:
        people_per_craft_count[i["craft"]] = people_per_craft_count.get(i["craft"], 0) + 1
    return people_per_craft_count


def people_list(people):
    df = pd.DataFrame.from_dict(people)
    df['runtime_utc'] = datetime.now(timezone.utc)
    df['runtime_local'] = datetime.now(tzlocal())
    return df.to_string()


response = requests.get('http://api.open-notify.org/astros.json')
output = Astros(response.json()["message"], response.json()["number"], response.json()["people"])
print(people_per_craft(output.people))
print(people_list(output.people))
