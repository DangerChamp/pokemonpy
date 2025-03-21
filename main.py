import json
import random

with open("pokemon.json") as f:
    pokemon = json.load(f)

class Pokemon:
    def __init__(self, pName, pLvl):
        self.__name, self.__level = pName, pLvl
        self.__type = pokemon[pName]["type"]

    def levelup():
        pass

class Player:
    def __init__(self):
        self.__party = []
        self.__pc = []
        self.__bag = []
    
    def start(self, choice):
        self.__party.append(Pokemon(choice))

    def addCaughtPokemon(self, pk):
        if len(self.__party) < 6:
            self.__party.append(Pokemon(pk))
        else:
            self.__pc.append(Pokemon(pk))

player = Player()

def encounter():
    highestLvl = 0
    party = getattr(player, "_Player__party")
    for i in range(len(party)):
        if highestLvl < getattr(party[i], "_Pokemon__level"):
            highestLvl = getattr(party[i], "_Pokemon__level")
    encounterLvl = random.randint(highestLvl-5, highestLvl+5)

for i in range(6):
    try:
        print(getattr(getattr(player, "_Player__party")[i], "_Pokemon__name"))
    except IndexError:
        print("EMPTY")