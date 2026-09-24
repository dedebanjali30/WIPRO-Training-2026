import unittest


class TestSetupTeardown(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        print("\n=== SETUP CLASS ===")

    @classmethod
    def tearDownClass(cls):
        print("=== TEARDOWN CLASS ===")

    def setUp(self):
        print("Starting test")

    def tearDown(self):
        print("Finished test")

    def test_one(self):
        self.assertEqual(5 + 5, 10)

    def test_two(self):
        self.assertEqual(10 - 5, 5)


if __name__ == "__main__":
    unittest.main()