

class JuegoOca:
    def __init__(self):
        self.players=[]
        self.positions=[]


    def add_player(self, player):
        if player in self.players:
            return player + ": Already existing player"

        self.players.append(player)
        self.positions.append(0)
        return self.players

    def move_player(self, player, dice0, dice1):
        to_str = player + " rolls " + str(dice0) + ", " + str(dice1) + ". " + player + " moves from " + self.get_position(player) + " to " + str(dice0 + dice1 + self.positions[self.players.index(player)])

        self.positions[self.players.index(player)] = dice0 + dice1

        if self.positions[self.players.index(player)] == 63:
            to_str += ". " + player + " Wins!!"

        return to_str

    def get_position(self,player):
        result = self.positions[self.players.index(player)]
        if result == 0:
            return "Start"
        return str(result)

