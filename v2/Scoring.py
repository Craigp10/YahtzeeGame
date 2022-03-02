
from collections import Counter

class Scoring:
  def __init__(self, diceList:list, playerScoreCardList: list ):
        self.self = self
        self.playerScoreCardList = playerScoreCardList
        self.diceList = diceList
        self.diceDict = Counter(diceList)
        self.scoreCard = {}
        self.calcScores()

  def grabScore(self, chooseScore:str) -> int:
    score = self.scoreCard[chooseScore]
    return score
  
  def updateDice(self,newDiceList):
    self.diceList = newDiceList
    self.diceDict = Counter(newDiceList)
    self.calcScores()

  def calcScores(self):
    # scoreCard = {}
    scoreCardMap = { #self.createScoreCard
          "One": self.CheckDiceValue(1),
          "Two": self.CheckDiceValue(2),
          "Three": self.CheckDiceValue(3),
          "Four": self.CheckDiceValue(4),
          "Five": self.CheckDiceValue(5),
          "Six": self.CheckDiceValue(6),
          "Three of A Kind": self.OfAKindScore(3),
          "Four of A Kind": self.OfAKindScore(4),
          "Small Straight": self.StraightScores(4,30),
          "Big Straight": self.StraightScores(5,40),
          "Full House": self.FullHouseScore(),
          "Yahtzee": self.CheckYahtzee(5),
          "Chance": self.ChanceScore()
    }
    scoreCard = {key:scoreCardMap[key] for key in self.playerScoreCardList}
    self.scoreCard = scoreCard
    return
  
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

  def CheckDiceValue(self, diceValue):
      '''returns the # of dice for a given value in the dict'''
      if self.diceDict.get(diceValue) == None:
          return 0
      value = self.diceDict.get(diceValue) * diceValue
      return value

  def ChanceScore(self):
      '''Chance Score'''
      score = 0
      #dice = 0
      for dice in self.diceDict:
          score += self.diceDict[dice] * int(dice)
      return score


  def StraightScores(self, count, score):
    '''Sliding Window Approach to handle straight scores... Given a count and a score determine if there is a straight
    for the provided count, if so return the score provided, if not return 0
    '''
    straightList = self.RemoveRepeatDice(self.diceList)
    if len(straightList) < count:
      return 0
    start = 0
    end = 1
    while (end < len(straightList)):
      if (straightList[end] - straightList[end-1] == 1): 
        end += 1
      else:
        start = end
        end += 1
      
      if end - start == count:
        return score
      
    return 0
      
  def StraightScores(self, count: int, score: int) -> int:
      '''Returns scores for the straight scores. Given count to check for and value to return'''
      straightList = self.RemoveRepeatDice(self.diceList)
      # print("STRAINT SCORES",straightList)
      if len(straightList) < count:
          return 0
      for diceIndex in range(1, len(straightList)):
          counter = 1
          isStraight = self.recursiveStraightCheck(straightList, diceIndex, counter, count)
          if isStraight:
              return score
          else:
              return 0

  def recursiveStraightCheck(self, diceList, diceIndex:int, counter: int, count:int) -> bool:
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

  def FullHouseScore(self) -> int:
      '''Returns score for Full House score'''
      if self.GrabMaxDiceCount(self.diceDict) == 3 and self.GrabMinDiceCount(self.diceDict) == 2:
          return 25
      return 0

  def OfAKindScore(self, count: int) -> int:
      '''Checks dice dict for of a kind dice and the count given ######ERROR, if I have 4 fours and 1 5, it multiples the 5 by 4, not 4 by 4.'''
      for dice in self.diceDict:
          if self.diceDict[dice] >= count:
              OfAKindScore = int(dice)*count
              return OfAKindScore
          # else:
          #     pass
      return 0

  def CheckYahtzee(self, count: int) -> int:
      '''Check for Yahtzee score with the dice (5 of 1 #)'''
      for test in self.diceDict:
          if self.diceDict[test]>= count:
              return 50
          else:
              return 0
  def getScores(self):
    return self.scoreCard

  def __repr__(self) -> str:
      return f"{self.scoreCard}"
