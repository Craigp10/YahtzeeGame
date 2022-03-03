import Player, Turn, GameCommunication as gc

class Yahtzee():
  def __init__(self, gameCommunication:gc):
    self.self = self
    self.gc = gameCommunication
    self.players = self.getPlayers()
    self.rounds = self.getRounds()
    self.startGame()

  def getPlayers(self) -> list:
    players = []
    player_names = self.gc.stringInputstatement("What are players names? First names and put space in between \n")
    player_names = player_names.split()
    for player in player_names:
        player = Player.Player(player, 0, ["One", "Two", "Three",
                                           "Four", "Five", "Six", "Small Straight", "Big Straight",
                                           "Three of A Kind","Four of A Kind","Full House",
                                           "Yahtzee", "Chance"])
        players.append(player)

    return players

  def getRounds(self) -> list:
    rounds = -1
    while (rounds < 0 or rounds > 13):
      rounds = int(self.gc.numberInputstatement("How many rounds would you like to play? "))
    return rounds

  def startGame(self) -> None:
    turn = 0
    while turn < self.rounds:
        #Turn.Turn()
        for player in self.players:
          # print('p',player)
          turnInt = Turn.Turn(player, 5, self.gc)
          player.updateScore(turnInt.handleTurn())
        turn += 1
    [print(player.name, player.score) for player in self.players]
    self.decideWinner()
    return None

  def decideWinner(self):
    leader = ""
    leaderScore = 0
    for player in self.players:
      if player.score > leaderScore:
        leader = player.name
        leaderScore = player.score
    
    print(f"WINNER {leader} with a score of {leaderScore}")
    return None



newGame = Yahtzee(gc.GameCommunication())