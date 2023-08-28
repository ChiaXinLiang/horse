class Horse:
    def __init__(self, horse_name, skill_1, skill_2):
        self.horse_name = horse_name
        self.skill_1 = skill_1
        self.skill_2 = skill_2
        self.hp = 100
        self.competitionRound = 0

    def showInfo(self):
        return [self.horse_name, self.skill_1, self.skill_2, self.hp, self.competitionRound]
    
    def updateSkill(self, skill_1, skill_2):
        self.skill_1 = skill_1
        self.skill_2 = skill_2
    
    def showName(self):
        return self.horse_name
    
    def show_first_skill(self):
        return self.skill_1
    
    def show_second_skill(self):
        return self.skill_2

    def minusHp(self):
        self.hp = self.hp -50

    def resetHp(self):
        self.hp = 100
    
    def showHp(self):
        return self.hp
    
    def addCompetitionRound(self):
        self.competitionRound += 1

    def swapSkill(self):
        temp_skill = self.skill_1
        self.skill_1 = self.skill_2
        self.skill_2 = temp_skill

class HorseList:
    def __init__(self, horseList={}):
        self.horseList = horseList

    def addHorse(self, horseName, horse):
        if horseName in self.horseList:
            self.horseList[horseName].append(horse)
        else:
            self.horseList[horseName] = [horse]

    def getHorse(self, horseName):
        return self.horseList[horseName][0]

    def showAllHorse(self):
        return self.horseList

    def allHorseResetHp(self):
        for horse_list in self.horseList.values():
            for horse in horse_list:
                horse.resetHp()