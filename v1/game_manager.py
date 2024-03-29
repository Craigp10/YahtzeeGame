
import Yahtzee as Yahtzee

import Player as Player



def createPlayers():
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

def main():
    '''Main - runs this game'''
    players = createPlayers()
    rounds = 0
    while(rounds < 1 or rounds > 13):
      rounds = int(input("how many rounds do you want to play?"))
    print('Our players for the game! ',players, ' will be playing ', rounds)
    # print("Unless you're picking a score to score with, please only enter #'s for rounds and dice")
    new_game = Yahtzee.Yahtzee(players,rounds)
    new_game.GameStart()
    new_game.decideWinner()

    return None

if __name__ == "__main__":
    main()