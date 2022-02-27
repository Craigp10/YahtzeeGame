

class Player:
  def __init__(self, playerName:str, startingScore, scoreScareScores):
    self.self = self
    self.name = playerName
    self.score = startingScore
    self.scoreCard = {key: 0 for key in scoreScareScores}
      # "One": 0,
      # "Two": 0,
      # "Three":0,
      # "Four":0,
      # "Five":0,
      # "Six":0, 
      # "Three of A Kind": 0,
      # "Four of A Kind": 0,
      # "Small Straight": 0,
      # "Big Straight": 0,
      # "Full House": 0,
      # "Yahtzee":0,
      # "Chance": 0,
    

  def getScore(self) -> int:
    return self.score
 
  def getScorecard(self) -> dict: #scoreCard 
    return self.scorecard
  
  def updateScore(self, addScore:int) -> None:
    self.score += addScore
  

