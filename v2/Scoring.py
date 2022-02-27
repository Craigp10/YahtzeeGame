
from collections import Counter

class Scoring:
  def __init__(self, playerScoreCard: dict, diceList:list):
        self.self = self
        self.player = playerScoreCard
        self.diceList = diceList
        self.diceDict = Counter(diceList)
        self.scoreCard = {
          "One": self.CheckDiceValue(self.diceDict, 1),
          "Two": self.CheckDiceValue(self.diceDict, 2),
          "Three": self.CheckDiceValue(self.diceDict, 3),
          "Four": self.CheckDiceValue(self.diceDict, 4),
          "Five": self.CheckDiceValue(self.diceDict, 5),
          "Six": self.CheckDiceValue(self.diceDict, 6),
          "Three of A Kind": self.OfAKindScore(self.diceDict, 3),
          "Four of A Kind": self.OfAKindScore(self.diceDict, 4),
          "Small Straight": self.StraightScores(self.diceList,4,30),
          "Big Straight": self.StraightScores(self.diceList,5,40),
          "Full House": self.FullHouseScore(self.diceDict),
          "Yahtzee": self.CheckYahtzee(self.diceDict,5),
          "Chance": self.ChanceScore(self.diceDict)
        }
        print(self.scoreCard)


  def grabScore(self, chooseScore:str) -> int:
    score = self.scoreCard[chooseScore]
    return score

  def RemoveRepeatDice(self,diceList):
        '''Remove Any duplicate dice values in the list, used to measure the Straight Score'''
        WorkingSet = diceList
        diceList = []
        for dice in WorkingSet:
            if dice not in diceList:
                diceList.append(int(dice))
        return diceList

  def GrabMaxDiceCount(self, diceDict):
      '''Obtain max dice value in the dict'''
      maxDiceValue = max(diceDict.values())
      return maxDiceValue

  def GrabMinDiceCount(self, diceDict):
      '''Obtain min dice value in the dict'''
      minDiceValue = min(diceDict.values())
      return minDiceValue

  def CheckDiceValue(self, diceDict, diceValues):
      '''returns the # of dice for a given value in the dict'''
      if diceDict.get(diceValues) == None:
          return 0
      value = diceDict.get(diceValues) * diceValues
      return value

  def ChanceScore(self, diceDict):
      '''Chance Score'''
      score = 0
      #dice = 0
      for dice in diceDict:
          score += diceDict[dice] * int(dice)
      return score

  def StraightScores(self, diceList: int, count: int, score: int) -> int:
      '''Returns scores for the straight scores. Given count to check for and value to return'''
      straightList = self.RemoveRepeatDice(diceList)
      if len(straightList) < count:
          return 0
      for diceIndex in range(1, len(straightList)):
          counter = 1
          isStraight = self.recursiveStraightCheck(straightList, diceIndex, counter, count)
          if isStraight:
              return score
          else:
              return 0

  def recursiveStraightCheck(self, diceList: list,  diceIndex:int, counter: int, count:int) -> bool:
      '''Called with StraightScores to check for a straight with each dice iteration through diceList'''
      try:
          if counter == count:
              return True
          elif (int(diceList[diceIndex]) - int(diceList[diceIndex - 1])) == 1:
              counter += 1
              diceIndex += 1
              return self.recursiveStraightCheck(diceList, diceIndex, counter, count)
          else:
              return False

      except IndexError:
          return False

  def FullHouseScore(self, diceDict:int) -> int:
      '''Returns score for Full House score'''
      if self.GrabMaxDiceCount(diceDict) == 3 and self.GrabMinDiceCount(diceDict) == 2:
          return 25
      return 0

  def OfAKindScore(self, diceDict: dict, count: int) -> int:
      '''Checks dice dict for of a kind dice and the count given ######ERROR, if I have 4 fours and 1 5, it multiples the 5 by 4, not 4 by 4.'''
      for test in diceDict:
          if diceDict[test] >= count:
              OfAKindScore = int(test)*count
              return OfAKindScore
          # else:
          #     pass
      return 0

  def CheckYahtzee(self, diceDict: dict, count: int) -> int:
      '''Check for Yahtzee score with the dice (5 of 1 #)'''
      for test in diceDict:
          if diceDict[test]>= count:
              return 50
          else:
              return 0




# a = Scoring({},[1,1,2,4,4,5,6,6])