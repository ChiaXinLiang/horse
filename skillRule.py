import numpy as np
import random

class SkillTable:
    def __init__(self, skill_1, skill_2, skill_3, skill_4, skill_5, skill_6):
        self.skillsList = [skill_1, skill_2, skill_3, skill_4, skill_5, skill_6]
        self.AccTable = np.array([[0,0.85,0.85,0.5,0.15,0.15],
                        [0.15,0,0.85,0.85,0.5,0.15],
                        [0.15,0.15,0,0.85,0.85,0.5],
                        [0.5,0.15,0.15,0,0.85,0.85],
                        [0.85,0.5,0.15,0.15,0,0.85],
                        [0.85,0.85,0.5,0.15,0.15,0]])

    def computeWinner(self, skill_1, skill_2):
        self.skill_1_id = self.skillsList.index(skill_1)
        self.skill_2_id = self.skillsList.index(skill_2)
        skill_1_winningRate = self.AccTable[self.skill_1_id, self.skill_2_id]
        if random.random() < skill_1_winningRate:
            winner = "first"
        else:
            winner = "second"
        return winner
