import unittest

from bowling.game import Game


class TestGame(unittest.TestCase):
    def setUp(self):
        self.g = Game()

    def test_two_throws_no_mark(self):
        self.g.add(5)
        self.g.add(4)
        self.assertEqual(9, self.g.score())

    def test_four_throws_no_mark(self):
        self.g.add(5)
        self.g.add(4)
        self.g.add(7)
        self.g.add(2)
        self.assertEqual(18, self.g.score())
        self.assertEqual(9, self.g.score_for_frame(1))
        self.assertEqual(18, self.g.score_for_frame(2))

    def test_simple_spare(self):
        self.g.add(3)
        self.g.add(7)
        self.g.add(3)
        self.assertEqual(13, self.g.score_for_frame(1))

    def test_simple_frame_after_spare(self):
        self.g.add(3)
        self.g.add(7)
        self.g.add(3)
        self.g.add(2)
        self.assertEqual(13, self.g.score_for_frame(1))
        self.assertEqual(18, self.g.score_for_frame(2))
        self.assertEqual(18, self.g.score())

    def test_simple_strike(self):
        self.g.add(10)
        self.g.add(3)
        self.g.add(6)
        self.assertEqual(19, self.g.score_for_frame(1))
        self.assertEqual(28, self.g.score())

    def test_perfect_game(self):
        for i in range(12):
            self.g.add(10)

        self.assertEqual(300, self.g.score())

    def test_end_of_array(self):
        for i in range(9):
            self.g.add(0)
            self.g.add(0)

        self.g.add(2)
        self.g.add(8)
        self.g.add(10)
        self.assertEqual(20, self.g.score())

    def test_sample_game(self):
        self.g.add(1)
        self.g.add(4)
        self.g.add(4)
        self.g.add(5)
        self.g.add(6)
        self.g.add(4)
        self.g.add(5)
        self.g.add(5)
        self.g.add(10)
        self.g.add(0)
        self.g.add(1)
        self.g.add(7)
        self.g.add(3)
        self.g.add(6)
        self.g.add(4)
        self.g.add(10)
        self.g.add(2)
        self.g.add(8)
        self.g.add(6)
        self.assertEqual(133, self.g.score())

    def test_heart_break(self):
        for i in range(11):
            self.g.add(10)
        self.g.add(9)
        self.assertEqual(299, self.g.score())

    def test_tenth_frame_spare(self):
        for i in range(9):
            self.g.add(10)
        self.g.add(9)
        self.g.add(1)
        self.g.add(1)
        self.assertEqual(270, self.g.score())


if __name__ == '__main__':
    unittest.main()
