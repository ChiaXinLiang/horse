import numpy as np
from pydantic import BaseModel
from horseList import *
from skillRule import *
from Competition import *
from collections import Counter
import matplotlib.pyplot as plt
from fastapi import FastAPI



app = FastAPI()
# Define a Pydantic model for the input data
class InputHorse(BaseModel):
    name: str
    skill: list[str]

class InputData(BaseModel):
    horses: list[InputHorse]

class OutputData(BaseModel):
    occurrences: dict
    winning_rates: dict

allHorse = HorseList()
allHorse.addHorse("Gildedmane", Horse("Gildedmane", "Sprint", "Rotation"))
allHorse.addHorse("Scarletgem", Horse("Scarletgem", "Sprint", "Heavy_blow"))
allHorse.addHorse("Steelhorn", Horse("Steelhorn", "Sprint", "Dodge"))
allHorse.addHorse("Oakhoof", Horse("Oakhoof", "Sprint", "Protection"))
allHorse.addHorse("Emeraldu", Horse("Emeraldu", "Sprint", "Healing"))
allHorse.addHorse("ArcanaCrest", Horse("ArcanaCrest", "Rotation", "Heavy_blow"))
allHorse.addHorse("Colorful CNM", Horse("Colorful CNM", "Rotation", "Dodge"))
allHorse.addHorse("Shardik", Horse("Shardik", "Rotation", "Protection"))
allHorse.addHorse("Fenrir", Horse("Fenrir", "Rotation", "Healing"))
allHorse.addHorse("Fury", Horse("Fury", "Heavy_blow", "Dodge"))
allHorse.addHorse("Dakila", Horse("Dakila", "Heavy_blow", "Protection"))
allHorse.addHorse("Caco", Horse("Caco", "Heavy_blow", "Healing"))
allHorse.addHorse("Shibazuke", Horse("Shibazuke", "Dodge", "Protection"))
allHorse.addHorse("Panda", Horse("Panda", "Dodge", "Healing"))
allHorse.addHorse("Tiger", Horse("Tiger", "Protection", "Healing"))

skillTable = SkillTable("Sprint", "Rotation", "Heavy_blow", "Dodge", "Protection", "Healing")
competition = Competition(allHorse, skillTable)

@app.post("/calculate_stats/")
async def calculate_stats(input_data: InputData):
    input_horses = []
    for horse in input_data.horses:
        if horse.name != "secret":
            target_horse = allHorse.getHorse(horse.name)
            target_horse.updateSkill(horse.skill[0], horse.skill[1])
        input_horses.append(horse.name)

    occurrences, winning_rates = competition.oneMatchStatistic(input_horses)
    output_data = OutputData(occurrences=occurrences, winning_rates=winning_rates)
    return output_data
# [occurrences, winning_rates] =competition.oneMatchStatistic('Gildedmane','Scarletgem','Steelhorn','Emeraldu','Colorful CNM','Fury','Shibazuke','Tiger')
