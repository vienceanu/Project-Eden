from Ship import Ship as Ship
import json

with open("data.json", "r") as f:
    data = json.load(f)

class Gun:
    level = 1
    Resources = {"uranium":1 * level, "titanium": 2 * level}

class Hull:
    level = 1
    Resources = {"iron":3 * level, "titanium": 2 * level}
