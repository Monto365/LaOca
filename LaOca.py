import unittest

class JuegoOca:
    def __init__(self):
        self.players=[]

    def add_player(self, player):
        if player in self.players:
            return "Sara: Already existing player"

        self.players.append(player)
        return self.players


class TestJuegoOca(unittest.TestCase):
    def test_add_first_player(self):
        # Arrange
        juego_oca = JuegoOca()
        expected = ["Sara"]

        # Act
        player = "Sara"
        result = juego_oca.add_player(player)

        # Assert
        self.assertEqual(expected, result)

    def test_add_second_player(self):
        # Arrange
        juego_oca = JuegoOca()
        expected = ["Sara","Juan"]
        player1 = "Sara"
        juego_oca.add_player(player1)

        # Act
        player2 = "Juan"
        result = juego_oca.add_player(player2)

        # Assert
        self.assertEqual(expected, result)

    def test_player_already_exists(self):
        # Arrange
        juego_oca = JuegoOca()
        expected = "Sara: Already existing player"
        player = "Sara"
        juego_oca.add_player(player)

        # Act
        same_player = "Sara"
        result = juego_oca.add_player(same_player)

        # Assert
        self.assertEqual(expected, result)

if __name__ == '__main__':
    unittest.main()
#comentario