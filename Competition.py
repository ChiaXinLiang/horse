import numpy as np
import random
from horseList import *
from skillRule import *
from collections import Counter
import random



class Competition:
    def __init__(self, horseList, skillTable):
        self.horseList = horseList
        self.skillTable = skillTable

    def start(self):
        self.horseList.allHorseResetHp()
        chosen_horse = random.sample(list(self.horseList.showAllHorse()), 8)
        for horseName in chosen_horse:
            horse = self.horseList.getHorse(horseName)
            horse.addCompetitionRound()
        #first round
        round1_part1_winner = self.fight(self.horseList.getHorse(chosen_horse[0]), self.horseList.getHorse(chosen_horse[1]))
        round1_part2_winner = self.fight(self.horseList.getHorse(chosen_horse[2]), self.horseList.getHorse(chosen_horse[3]))
        round1_part3_winner = self.fight(self.horseList.getHorse(chosen_horse[4]), self.horseList.getHorse(chosen_horse[5]))
        round1_part4_winner = self.fight(self.horseList.getHorse(chosen_horse[6]), self.horseList.getHorse(chosen_horse[7]))
        print("first round winner: {}, {}, {}, {}".format(round1_part1_winner.showName(), 
                                                          round1_part2_winner.showName(), 
                                                          round1_part3_winner.showName(), 
                                                          round1_part4_winner.showName()))

        #second round
        round1_part1_winner.resetHp()
        round1_part2_winner.resetHp()
        round1_part3_winner.resetHp()
        round1_part4_winner.resetHp()
        round2_part1_winner = self.fight(round1_part1_winner, round1_part2_winner)
        round2_part2_winner = self.fight(round1_part3_winner, round1_part4_winner)
        print("second round winner: {}, {}".format(round2_part1_winner.showName(), round2_part2_winner.showName()))

        #final round
        round2_part1_winner.resetHp()
        round2_part2_winner.resetHp()
        round3_winner = self.fight(round2_part1_winner, round2_part2_winner)
        print("final round winner: {}".format(round3_winner.showName()))
        return round3_winner



    
    def fight(self, horse1, horse2):
        #first skill
        if horse1.show_first_skill() == horse2.show_first_skill():
            horse1.minusHp()
            horse2.minusHp()
        else:
            winner = self.skillTable.computeWinner(horse1.show_first_skill(),horse2.show_first_skill())
            if winner == "first":
                horse2.minusHp()
            elif winner == "second":
                horse1.minusHp() 

        #second skill
        if horse1.show_second_skill() == horse2.show_second_skill():
            horse1.minusHp()
            horse2.minusHp()
        else:
            winner = self.skillTable.computeWinner(horse1.show_second_skill(),horse2.show_second_skill())
            if winner == "first":
                horse2.minusHp()
            elif winner == "second":
                horse1.minusHp() 

        #check need third round?
        if horse1.showHp() == 50 and horse2.showHp() == 50:
            if horse1.show_first_skill() == horse2.show_first_skill():
                horse1.minusHp()
                horse2.minusHp()
            else:
                winner = self.skillTable.computeWinner(horse1.show_first_skill(),horse2.show_first_skill())
                if winner == "first":
                    horse2.minusHp()
                elif winner == "second":
                    horse1.minusHp() 
        
        if horse1.showHp() != 0 and horse2.showHp() == 0:
            winner = horse1
        elif horse1.showHp() == 0 and horse2.showHp() != 0:
            winner = horse2
        elif horse1.showHp() == 0 and horse2.showHp() == 0:
            winner = horse1
        return winner 
    
    def startNoPrint(self):
        self.horseList.allHorseResetHp()
        chosen_horse = random.sample(list(self.horseList.showAllHorse()), 8)
        for horseName in chosen_horse:
            horse = self.horseList.getHorse(horseName)
            horse.addCompetitionRound()
        #first round
        round1_part1_winner = self.fight(self.horseList.getHorse(chosen_horse[0]), self.horseList.getHorse(chosen_horse[1]))
        round1_part2_winner = self.fight(self.horseList.getHorse(chosen_horse[2]), self.horseList.getHorse(chosen_horse[3]))
        round1_part3_winner = self.fight(self.horseList.getHorse(chosen_horse[4]), self.horseList.getHorse(chosen_horse[5]))
        round1_part4_winner = self.fight(self.horseList.getHorse(chosen_horse[6]), self.horseList.getHorse(chosen_horse[7]))

        #second round
        round1_part1_winner.resetHp()
        round1_part2_winner.resetHp()
        round1_part3_winner.resetHp()
        round1_part4_winner.resetHp()
        round2_part1_winner = self.fight(round1_part1_winner, round1_part2_winner)
        round2_part2_winner = self.fight(round1_part3_winner, round1_part4_winner)

        #final round
        round2_part1_winner.resetHp()
        round2_part2_winner.resetHp()
        round3_winner = self.fight(round2_part1_winner, round2_part2_winner)
        return round3_winner

    def oneMatchStatistic(self, input_horses):
        dataList = []
        reference = ['Gildedmane', 'Scarletgem', 'Steelhorn', 'Oakhoof', 'Emeraldu', 'ArcanaCrest', 
                    'Colorful CNM', 'Shardik', 'Fenrir', 'Fury', 'Dakila', 'Caco', 'Shibazuke', 'Panda', 'Tiger']
        
        input_horses_ori = input_horses.copy()
        if "secret" in input_horses_ori:
            secret_index = input_horses.index("secret")
        for i in range(0, 10000):
            #輸入8只馬，依照順序
            # Iterate through reference to find a replacement horse that's not in input_horses
            input_horses = input_horses_ori.copy()
            if "secret" in input_horses:
                replacement_horse = None
                random.shuffle(reference)
                for ref_horse in reference:
                    if ref_horse not in input_horses:
                        #隨機選取馬
                        random_number = random.random()
                        if random_number > 0.5:
                            random_horse = self.horseList.getHorse(ref_horse)
                            random_horse.swapSkill() #將隨機馬對調技能
                        replacement_horse = ref_horse
                        break

                #替換馬
                if replacement_horse is not None:
                    input_horses[secret_index] = replacement_horse

            dataList.append(self.oneMatchResult(input_horses[0],input_horses[1],input_horses[2],input_horses[3],input_horses[4],input_horses[5],input_horses[6],input_horses[7]).showName())

        occurrences = dataList
        reference = ['Gildedmane', 'Scarletgem', 'Steelhorn', 'Oakhoof', 'Emeraldu', 'ArcanaCrest', 
                    'Colorful CNM', 'Shardik', 'Fenrir', 'Fury', 'Dakila', 'Caco', 'Shibazuke', 'Panda', 'Tiger']
        
        if "secret" in input_horses_ori:
            input_horses_set = set(input_horses_ori)
            for i in range(len(occurrences)):
                if occurrences[i] not in input_horses_set:
                    occurrences[i] = "secret"
        occurrences = Counter(occurrences)
        sorted_occurrences = dict(sorted(occurrences.items(), key=lambda x: input_horses_ori.index(x[0])))
        total_games = sum(sorted_occurrences.values())  # Total number of games played

        winning_rates = {}
        for item, occurrences in sorted_occurrences.items():
            winning_rate = occurrences / total_games
            winning_rates[item] = winning_rate
        return [sorted_occurrences, winning_rates]

    def oneMatchResult(self, horseName1, horseName2, horseName3, horseName4, horseName5, horseName6, horseName7, horseName8):
        #first round
        self.horseList.allHorseResetHp()
        round1_part1_winner = self.fight(self.horseList.getHorse(horseName1), self.horseList.getHorse(horseName2))
        round1_part2_winner = self.fight(self.horseList.getHorse(horseName3), self.horseList.getHorse(horseName4))
        round1_part3_winner = self.fight(self.horseList.getHorse(horseName5), self.horseList.getHorse(horseName6))
        round1_part4_winner = self.fight(self.horseList.getHorse(horseName7), self.horseList.getHorse(horseName8))
        # print("first round winner: {}, {}, {}, {}".format(round1_part1_winner.showName(), 
        #                                                   round1_part2_winner.showName(), 
        #                                                   round1_part3_winner.showName(), 
        #                                                   round1_part4_winner.showName()))

        #second round
        round1_part1_winner.resetHp()
        round1_part2_winner.resetHp()
        round1_part3_winner.resetHp()
        round1_part4_winner.resetHp()
        round2_part1_winner = self.fight(round1_part1_winner, round1_part2_winner)
        round2_part2_winner = self.fight(round1_part3_winner, round1_part4_winner)
        # print("second round winner: {}, {}".format(round2_part1_winner.showName(), round2_part2_winner.showName()))

        #final round
        round2_part1_winner.resetHp()
        round2_part2_winner.resetHp()
        round3_winner = self.fight(round2_part1_winner, round2_part2_winner)
        # print("final round winner: {}".format(round3_winner.showName()))
        return round3_winner
      