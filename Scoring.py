


class Scoring:
    '''Class for scoring on each turn'''
    def __init__(self, player,dice_list):
        self.self = self
        self.player = player
        self.dice_list = dice_list
        self.dice_dict = self.ConvertToDict(dice_list)


    def runScore(self,player,dice_list):
        '''Run scoring object commands'''
        dice_dict = self.dice_dict
        score_Dict = self.setDictionary(player,dice_list,dice_dict)
        choosenScore = self.CheckScore(player,dice_list,score_Dict)
        self.addScore( player, choosenScore, score_Dict)
        self.DeleteChoosenScores(player, choosenScore)

        return choosenScore

    def ConvertToDict(self, dice_list):
        '''Converts dice list with all the dice being used to a dictionary for scoring purposes'''
        dice_dict = {}
        for dice in dice_list:
            if dice in dice_dict:
                dice_dict[dice] += 1
            else:
                dice_dict[dice] = 1
        return dice_dict

    def setDictionary(self,player,dice_list,dice_dict):
        '''Creates dictionary for player to score from based off their available scores'''
        full_Dict = {"One": self.CheckDiceValue(dice_dict, 1),
                     "Two": self.CheckDiceValue(dice_dict, 2),
                     "Three": self.CheckDiceValue(dice_dict, 3),
                     "Four": self.CheckDiceValue(dice_dict, 4),
                     "Five": self.CheckDiceValue(dice_dict, 5),
                     "Six": self.CheckDiceValue(dice_dict, 6),
                     "Three of A Kind": self.OfAKindScore(dice_dict, 3),
                     "Four of A Kind": self.OfAKindScore(dice_dict, 4),
                     "Small Straight": self.StraightScores(dice_list,4,30),
                     "Big Straight": self.StraightScores(dice_list,5,40),
                     "Full House": self.FullHouseScore(dice_dict),
                     "Yahtzee": self.CheckYahtzee(dice_dict,5),
                     "Chance": self.ChanceScore(dice_dict)}

        score_Dict = {}
        for i in range(len(player.scorecard)):
            if player.scorecard[i] in full_Dict:
                score_Dict[player.scorecard[i]] = full_Dict[player.scorecard[i]]
        print("You're Choices:",score_Dict)
        return score_Dict

    def PickScore(self):
        '''Take in score player chooses'''
        choosenScore = input("What score would you like to choose? Enter exactly as seen above without quotes")
        return choosenScore

    def CheckScore(self,player, dice_list,score_Dict):
        '''check the scoring option typed in by the player. Make sure it is an available score'''
        choosenScore = ''
        choosenScore = self.PickScore()
        if choosenScore not in player.scorecard:
            print(f"{choosenScore} isn't a option to score with")
            return self.CheckScore(player,dice_list,score_Dict)
        else:
            return choosenScore

    def addScore(self,player,choosenScore,score_Dict):
        '''Add the score of the given scoring option to the respective player'''
        addingScore = score_Dict[choosenScore]
        player.score += addingScore
        print(f"{player.name}'s score: {player.score}")
        return player.score

    def DeleteChoosenScores(self,player,choosenScore):
        '''Delete the choosen score from the players instance scorecard,
        used so we can keep choosen scores from displaying in future turns'''
        player.scorecard.remove(choosenScore)
        return player.scorecard

    def findIndex(self, choosenScore):
        '''Find the index of the choosen score'''
        for i in range(len(self.scorecard)):
            if self.scorecard[i] == choosenScore:
                return i

    def RemoveRepeatDice(self,dice_list):
        '''Remove Any duplicate dice values in the list, used to measure the Straight Score'''
        Working_Set = dice_list
        dice_list = []
        for dice in Working_Set:
            if dice not in dice_list:
                dice_list.append(int(dice))
        return dice_list

    def DiceCount(self, dice_dict, dice_value):
        '''Grab count of dice in dict for given dice value'''
        value = dice_dict.get(str(dice_value)) * dice_value
        return value

    def GrabMaxDiceCount(self, dice_dict):
        '''Obtain max dice value in the dict'''
        maxDiceValue = max(dice_dict.values())
        return maxDiceValue

    def GrabMinDiceCount(self, dice_dict):
        '''Obtain min dice value in the dict'''
        minDiceValue = min(dice_dict.values())
        return minDiceValue

    def CheckDiceValue(self, dice_dict, dice_value):
        '''returns the # of dice for a given value in the dict'''
        if dice_dict.get(dice_value) == None:
            return 0
        value = dice_dict.get(dice_value) * dice_value
        return value

    def ChanceScore(self,dice_dict):
        '''Chance Score'''
        score = 0
        #dice = 0
        for dice in dice_dict:
            score += dice_dict[dice] * int(dice)
        return score

    def StraightScores(self,dice_list, count, score):
        '''Returns scores for the straight scores. Given count to check for and value to return'''
        straight_li = self.RemoveRepeatDice(dice_list)
        if len(straight_li) < count:
            return 0
        for dice_index in range(1, len(straight_li)):
            counter = 1
            isStraight = self.recursiveStraightCheck(straight_li, dice_index, counter, count)
            if isStraight:
                return score
            else:
                return 0

    def recursiveStraightCheck(self,dice_list, dice_index, counter, count):
        '''Called with StraightScores to check for a straight with each dice iteration through dice_list'''
        try:
            if counter == count:
                return True
            elif (int(dice_list[dice_index]) - int(dice_list[dice_index - 1])) == 1:
                counter += 1
                dice_index += 1
                return self.recursiveStraightCheck(dice_list, dice_index, counter, count)
            else:
                return False

        except IndexError:
            return False

    def FullHouseScore(self,dice_dict):
        '''Returns score for Full House score'''
        if Scoring.GrabMaxDiceCount(self,dice_dict) == 3 and Scoring.GrabMinDiceCount(self,dice_dict) == 2:
            return 25
        return 0

    def OfAKindScore(self, dice_dict, count):
        '''Checks dice dict for of a kind dice and the count given ######ERROR, if I have 4 fours and 1 5, it multiples the 5 by 4, not 4 by 4.'''
        for test in dice_dict:
            if dice_dict[test] >= count:
                OfAKindScore = int(test)*count
                return OfAKindScore
            else:
                pass
        return 0

    def CheckYahtzee(self,dice_dict,count):
        '''Check for Yahtzee score with the dice (5 of 1 #)'''
        for test in dice_dict:
            if dice_dict[test]>= count:
                return 50
            else:
                return 0

    def __str__(self):
        return ''