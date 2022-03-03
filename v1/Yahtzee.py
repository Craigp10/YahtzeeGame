



import Player as Player, time



class Yahtzee:
    '''This is my game object, it holds all the functions to run a single game of Yahtzee'''
    def __init__(self,players):
        self.self = self
        self.players = players
      
    def GameStart(self):
        '''Start the game'''
        turn = 0
        game = 'inProgress'
        rounds = 0
        while (1 > rounds or rounds > 13):
            rounds = int(input('How many rounds would you like to play? 1 to 13 \n'))
        else:
            self.gameInProgress(self.players,rounds)

        return None

    def gameInProgress(self, players, rounds):
        '''Flow of game via while & for loop'''
        turn = 0
        while turn < rounds:
            for player in players:
                player.TakeTurn()
            turn += 1
        return None

    def decideWinner(self):
        '''decides who the winner is by comparing scores of the player objects'''
        print('Calculating Winner ...')
        time.sleep(3)
        leader = {'name':'','score':0}
        tied_players = []
        for player in self.players:
            if self.tie(leader,player):
                tied_players.extend((leader,player))
                continue
            elif player.score > leader['score']:
                leader = {'name':player.name,
                         'score':player.score}
                tied_players = []
        if len(tied_players) > 0:
            print("WE HAVE A TIE, PLAY ROCK PAPER SCISSORS!")
            leader['name'] = input("Who won? Be honest! \n")
        print(f"{leader['name']} is the winner! Congrats!")

        return None


    def tie(self,leader,player):
        '''Check if players are tie on score'''
        return leader['score'] == player.score


    def __str__(self):
        return ("We have a new game")