import unittest
from String_Calculator import Calculator

class TestCalculator(unittest.TestCase):
    def setUp(self):
        self.SUM1 = Calculator()

    def test_empty_string(self):
        self.assertEqual(self.SUM1.Calculate_Sum(""), 0)
    
    def test_single_number(self):
        self.assertEqual(self.SUM1.Calculate_Sum("1"), 1)
    
    def test_two_numbers(self):
        self.assertEqual(self.SUM1.Calculate_Sum("1,5"), 6)
    
    def test_multiple_numbers(self):
        self.assertEqual(self.SUM1.Calculate_Sum("1\n2,3"), 6)
    
    def test_custom_delimiter(self):
        self.assertEqual(self.SUM1.Calculate_Sum("//;\n1;2"), 3)
    
    def test_negative_numbers(self):
        with self.assertRaises(ValueError) as context:
            self.SUM1.Calculate_Sum("1,2,-3,4")
        self.assertIn("Negative numbers not allowed", str(context.exception))
    
    
if __name__ == "__main__":
    unittest.main()