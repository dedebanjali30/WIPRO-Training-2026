import unittest


class TestAssertions(unittest.TestCase):

    def test_equal(self):
        self.assertEqual(10 + 5, 15)

    def test_not_equal(self):
        self.assertNotEqual(10, 20)

    def test_true(self):
        self.assertTrue(10 > 5)

    def test_false(self):
        self.assertFalse(5 > 10)

    def test_in(self):
        self.assertIn("Python", "Python Automation")


if __name__ == "__main__":
    unittest.main()