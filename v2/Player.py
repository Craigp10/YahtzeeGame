

class Player:
  def __init__(self, playerName:str, startingScore, scoreScareScores):
    self.self = self
    self.name = playerName
    self.score = startingScore
    self.scoreCard = {key: (0, False) for key in scoreScareScores}
      # "One": (0, false),
      # "Two": (0, false),
      # "Three":(0, false),
      # "Four":(0, false),
      # "Five":(0, false),
      # "Six":(0,  false),
      # "Three of A Kind": (0, false),
      # "Four of A Kind": (0, false),
      # "Small Straight": (0, false),
      # "Big Straight": (0, false),
      # "Full House": (0, false),
      # "Yahtzee":(0, false),
      # "Chance": (0, false)
    

  def getScore(self) -> int:
    return self.score


  def getUnusedScoreCard(self):
      # {del self.scoreCard[score] if self.scoreCard[score][1] == True else False for score in self.scoreCard}
      scoreCardList = []
      for score in self.scoreCard:
        if self.scoreCard[score][1] == False:
          scoreCardList.append(score)
      return scoreCardList

  def getScorecard(self) -> dict: #scoreCard 
    return self.scorecard
  
  def updateScore(self, scoreTuple: tuple) -> None:
    '''Parameters: score:int, scoreCardChoosen: str'''
    self.score += scoreTuple[1]
    self.scoreCard[scoreTuple[0]] = (scoreTuple[1], True)
    # print(self)

  def __repr__(self) -> str:
      return f'{self.name, self.scoreCard}'

