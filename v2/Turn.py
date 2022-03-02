
import Dice, Player, Scoring, GameCommunication as gc


class Turn:
  def __init__(self, player: Player, diceCount, gameCommunication: gc):
    self.self = self
    self.rolls = 1
    self.player = player
    self.gc = gameCommunication
    self.dice = [Dice.Dice(6) for _ in range(diceCount)]
    self.rollAllDice()
    self.scoring = Scoring.Scoring([dice.value for dice in self.dice], self.player.getUnusedScoreCard())
    self.gc.printStatement(f"{self.player.name} is taking turn...")
    
    '''
      1. rolling dice
      2. player can decide to score with the rolled dice or reroll with keeping selected dice
      3. on third roll -- auto force a score
      4. once scoring decision has been made end turn
    '''

  def handleTurn(self):
    while(self.rolls < 3):
      self.sortDice()
      self.gc.printStatement("Here are your scores choices with the currently rolled dice")
      self.printCurrentScores()
      self.printDice()
      if self.gc.boolInputstatement("Would you like to score (Y) or re roll dice (N)? Y - score, N - Reroll "):
        #break out and handle scoring
        break
      else:
        reRollDice = self.gc.stringInputstatement("Which dice would you like to reroll? enter the number of the dice index as 1 number. \nFor Example 1 3 4 2 2 - re roll first and third dice: 13. \n")
        if len(reRollDice) == 5:
          self.rollAllDice()
        else:
          reRollDice = self.split(reRollDice)
          [self.rollDice(index - 1) for index in reRollDice]
      #pick dice to reroll repeat process... return score and choosen score
      self.rolls += 1
      self.scoring.updateDice([dice.value for dice in self.dice])
    self.printCurrentScores()
    return self.makeDecision()

  def sortDice(self):
    # self.dice.sort()
    self.dice.sort(key=lambda x: x.value)
    return

  def split(self, diceStr: str) -> list:
    return [int(index) for index in diceStr]

  def rollDice(self, index:int) -> None:
    # //roll a single dice w/ given index
    self.dice[index].roll()
    return

  def rollAllDice(self) -> None:
    [dice.roll() for dice in self.dice]
    return

  def pickDice(self, indices: str) -> None:
    for i in range(len(indices)):
      self.dice[indices[i]].roll()
    return
  
  def printCurrentScores(self):
    a = self.scoring.getScores()
    {print(key + ": " +str(a[key])) for key in a}
    return

  def makeDecision(self):
    #handle pick decision
    choice = ""
    while (choice not in self.scoring.scoreCard.keys()):
      choice = self.gc.stringInputstatement("Which score would you like to pick? Must be one of the options ")
    return (choice, self.scoring.scoreCard[choice])

  def printDice(self):
    self.gc.printStatement(self.dice)
    return



