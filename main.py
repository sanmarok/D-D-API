from classes import *
from os import system
import json

system("cls")


dm = dungeon_master()

print(json.dumps(dm.rolls(20),indent= 2))