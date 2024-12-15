import unittest

class TestStringOperations(unittest.TestCase):
    def test_string_concatenation(self):
        first_name = "John"
        last_name = "Doe"
        self.assertEqual(first_name + " " + last_name, "John Doe", "Concatenation test failed")

    def test_string_length(self):
        sample = "Jenkins"
        self.assertEqual(len(sample), 7, "String length test failed")

if __name__ == "__main__":
    unittest.main()
