import unittest

from bowling.frame import Frame


class TestFrame(unittest.TestCase):
    def test_score_no_throws(self):
        f = Frame()
        self.assertEqual(0, f.get_score())

    def test_add_one_throw(self):
        f = Frame()
        f.add(5)
        self.assertEqual(5, f.get_score())


if __name__ == '__main__':
    unittest.main()
