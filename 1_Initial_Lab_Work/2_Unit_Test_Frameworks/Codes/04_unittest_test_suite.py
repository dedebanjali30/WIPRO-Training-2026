import unittest


class TestAddition(unittest.TestCase):

    def test_addition(self):
        self.assertEqual(10 + 20, 30)


class TestSubtraction(unittest.TestCase):

    def test_subtraction(self):
        self.assertEqual(20 - 10, 10)


class TestMultiplication(unittest.TestCase):

    def test_multiplication(self):
        self.assertEqual(5 * 5, 25)


# Create a test suite
suite = unittest.TestSuite()

suite.addTest(
    TestAddition("test_addition")
)

suite.addTest(
    TestSubtraction("test_subtraction")
)

suite.addTest(
    TestMultiplication("test_multiplication")
)


# Run the test suite
runner = unittest.TextTestRunner(verbosity=2)
runner.run(suite)