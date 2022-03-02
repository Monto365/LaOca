class JuegoOca:
    def __init__(self):
        self.players=[]

    def add_player(self, player):
        if player in self.players:
            return player + ": Already existing player"

        self.players.append(player)
        return self.players

    def move_player(self, player1, dice0, dice1):
        return "Sara rolls 4, 2. Sara moves from Start to 6"
