import unittest
from LaOca import JuegoOca


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
        expected = ["Sara", "Juan"]
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

    def test_move_player(self):
        # Arrange
        juego_oca = JuegoOca()
        player1 = "Sara"
        juego_oca.add_player(player1)
        player2 = "Juan"
        juego_oca.add_player(player2)

        expected = "Sara rolls 4, 2. Sara moves from Start to 6"

        # Act
        result = juego_oca.move_player(player1, 4, 2)

        # Assert
        self.assertEqual(expected, result)

    def test_move_player2(self):
        # Arrange
        juego_oca = JuegoOca()
        player1 = "Sara"
        juego_oca.add_player(player1)
        player2 = "Juan"
        juego_oca.add_player(player2)

        expected = "Juan rolls 2, 2. Juan moves from Start to 4"

        # Act
        result = juego_oca.move_player(player2, 2, 2)

        # Assert
        self.assertEqual(expected, result)


if __name__ == '__main__':
    unittest.main()
