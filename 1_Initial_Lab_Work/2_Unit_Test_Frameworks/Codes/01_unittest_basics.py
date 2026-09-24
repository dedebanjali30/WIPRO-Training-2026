import unittest


class TestBasic(unittest.TestCase):

    def test_addition(self):
        result = 10 + 20
        self.assertEqual(result, 30)


if __name__ == "__main__":
    unittest.main()