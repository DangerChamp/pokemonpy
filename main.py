import json

with open("pokemon.json") as f:
    pokemon = json.load(f)

class Pokemon:
    def __init__(self, pName, pLvl):
        self.name, self.level = pName, pLvl
        self.type = pokemon[pName]["type"]

party = []
party.append(Pokemon("BULBASAUR", 16))