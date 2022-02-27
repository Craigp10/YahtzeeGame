import Player


class Yahtzee(self):
  def __init__(self):
    self.self = self
    self.players = self.getPlayers(self)
    self.rounds = self.getRounds(self)
    self.startGame(self)

  def getPlayers(self) -> list:
    players = []
    player_names = input("What are players names? First names and put space in between \n")
    player_names = player_names.split()
    for player in player_names:
        player = Player.Player(player, 0, ["One", "Two", "Three",
                                           "Four", "Five", "Six", "Small Straight", "Big Straight",
                                           "Three of A Kind","Four of A Kind","Full House",
                                           "Yahtzee", "Chance"])
        players.append(player)

    return players

  def getRounds(self) -> list:
    rounds = ""
    while (type(rounds) != int or rounds < 0 or rounds > 13):
      rounds = input("How many rounds would you like to play? ")
    return rounds

  def startGame(self) -> None:
    turn = 0
    while turn < self.rounds:
        # for player in self.players:
        #     player.TakeTurn()
        turn += 1
    return None