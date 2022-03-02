class JuegoOca:
    def __init__(self):
        self.players=[]

    def add_player(self, player):
        if player in self.players:
            return player + ": Already existing player"

        self.players.append(player)
        return self.players

    def move_player(self, player, dice0, dice1):
        return player + " rolls " + str(dice0) + ", " + str(dice1) + ". " + player + " moves from Start to " + str(dice0+dice1)


