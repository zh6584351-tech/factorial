import unittest
from factorial_app import factorial


class TestFactorial(unittest.TestCase):
    def test_zero(self):
        self.assertEqual(factorial(0), 1)

    def test_one(self):
        self.assertEqual(factorial(1), 1)

    def test_positive_numbers(self):
        self.assertEqual(factorial(5), 120)
        self.assertEqual(factorial(6), 720)

    def test_negative_raises_value_error(self):
        with self.assertRaises(ValueError):
            factorial(-1)

    def test_invalid_type_raises_type_error(self):
        with self.assertRaises(TypeError):
            factorial(3.5)
        with self.assertRaises(TypeError):
            factorial(True)


if __name__ == "__main__":
    unittest.main()