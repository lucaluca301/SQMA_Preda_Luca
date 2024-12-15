import unittest

class TestArithmetic(unittest.TestCase):
    def test_addition(self):
        self.assertEqual(5 + 10, 15, "Addition test failed")

    def test_subtraction(self):
        self.assertEqual(20 - 8, 12, "Subtraction test failed")

if __name__ == "__main__":
    unittest.main()
