
import Dice, Player, Scoring


class Turn:
  def __init__(self, player: Player, diceCount):
    self.self = self
    self.player = player
    self.dice = [Dice.Dice(6) for _ in range(diceCount)]
    self.rolls = 1
    print(f"{player.name} is taking turn...")

    #turn is initiated by Game each round for each player
    #workflow of a turn consist of 
    '''
      1. rolling dice
      2. player can decide to score with the rolled dice or reroll with keeping selected dice
      3. on third roll -- auto force a score
      4. once scoring decision has been made end turn
    '''

  def handleTurn(self):
    while(self.rolls < 3):
      print(self.rolls)
    pass



  def rollDice(self, index:int) -> None:
    # //roll a single dice w/ given index
    self.dice[index].roll()
    

  def rollAllDice(self) -> None:
    [dice.roll() for dice in self.dice]
    return

  def pickDice(self, indices: str) -> None:
    #
    pass
  
  def makeDecision(self):
    a = Scoring(self.dice, self.player.scoreCard)
    a.printScores()
    pass

  def checkDice(self):
    print(self.dice)
    return




a = Turn(Player.Player('craig',0,[]),5)
a.rollAllDice()
a.checkDice()
a.rollDice(3)
a.checkDice()