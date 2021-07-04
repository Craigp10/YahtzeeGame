

import random
from client_communicate import Client_Communicate as cc
import Scoring



class Player:
    '''Player class for each player in Yahtzee game'''
    def __init__(self, name: str, score: int, scorecard: dict):
        self.score = score
        self.scorecard = scorecard
        self.name = name

    def TakeTurn(self):
        '''Player takes turn'''
        print(f"{self.name} is taking turn...")
        print(f"Here's a reminder of what scores you can choose from!\n {self.scorecard} \n")
        dice_list = []
        for roll in range(3):
            print(f"{self.name}'s roll", int(roll) + 1, "out of 3")
            dice_rolled = []
            if roll == 2:
                print(f"roll 3... Time to pick a score!")
                dice_list.extend(self.makeRoll(dice_list))
                dice_list.sort()
                print(f"{self.name}'s Dice:", dice_list)
            elif len(dice_list) == 5:
                print(f"You kept all 5 dice.. Time to pick a score!")
                break
            else:
                dice_rolled = self.makeRoll(dice_list)
                print(f"{self.name} rolled:", dice_rolled)
                answer = cc.client_input(self,"Would you like to keep any dice? Y for yes, press anything else for no \n")
                if answer.lower() == 'y':
                    dice_list = self.Check_Dice(dice_rolled,dice_list)
                    print(f"{self.name}'s Dice:", dice_list)
                answer = input("Would you like to remove any kept dice? Y for yes, press anything else for no \n")
                if answer.lower() == 'y':
                    dice_list = self.Remove_Dice(dice_list)
                    print("You're dice: ",dice_list)
            if len(dice_list) == 5:
                dice_list.sort()
                self.MakeScore(dice_list)
                break
        return

    def makeRoll(self, dice_list):
        dice_rolled = []
        [dice_rolled.append(random.randint(1, 6) * 10 // 10) for i in range(5 - len(dice_list))]
        dice_rolled.sort()
        return dice_rolled



    def Keep_Dice(self,dice_picked):
        '''Keeps dice the player wants to keep for next roll'''
        dice_picked.extend(input("What Dice would you like to keep? (Enter dice as 123 for 1,2,3 \n"))
        return dice_picked

    def Check_Dice(self,dice_rolled,dice_list):
        '''Pick Dice to keep, Validate the dice choosen, and create new list of dice if passes validate'''
        dice_picked = []
        dice_picked = self.Keep_Dice(dice_picked)
        if self.ValidateDicePicked(dice_picked,dice_rolled):
            for dice in dice_picked:
                dice_list.append(int(dice))
            return dice_list
        else:
            return self.Check_Dice(dice_rolled,dice_list)

    def ValidateDicePicked(self,dice_picked,dice_group):
        '''Validate the dice picked (dice_picked) with dice the available (dice_group)'''
        if len(dice_picked) > 5:
            print('*****LengthError*****\nYou are trying to keep too many dice')
            return False
        else:
            for dice in dice_picked:
                if int(dice) in dice_group:
                    dice_group.remove(int(dice))
                else:
                    print("*****ValueError*****\nYou are trying to keep dice that weren't rolled")
                    return False
        return True

    def split(self,word: str):
        return [char for char in word]

    def convertToInt(self,test_list: list):
        for i in range(0, len(test_list)):
            test_list[i] = int(test_list[i])
        return test_list

    def Remove_Dice(self, dice_list: list):
        '''Remove chosen dice'''
        toRemove = []
        toRemove.append(self.split(input('What Dice would you like to remove? (Enter dice as 123 for 1,2,3 \n')))
        toRemove = self.convertToInt(toRemove[0])
        if all(dice in dice_list for dice in toRemove):
            for dice in toRemove:
                dice_list.remove(int(dice))
            return dice_list
        else:
            return self.Remove_Dice(dice_list)

    def MakeScore(self,dice_list):
        '''Make a score on the players scorecard with their current dice'''
        print("scoring with... ",dice_list)
        print("You're available scorecard",self.scorecard)
        score = Scoring.Scoring(self, dice_list)
        score.runScore(self,dice_list)
        return

    def __str__(self):
        return f'{self.name}, \n{self.score}, \n{self.scorecard}'

    def __repr__(self):
        return f'{self.name}'