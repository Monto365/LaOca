class JuegoOca:
    def __init__(self):
        self.players=[]

    def add_player(self, player):
        if player in self.players:
            return player + ": Already existing player"

        self.players.append(player)
        return self.players
