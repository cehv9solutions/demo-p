# Assuming this is your test-calc.py file

# E302: Add an extra blank line here
import unittest


# E302: Add an extra blank line here
class TestCalculator(unittest.TestCase):

    # E305: Add an extra blank line here
    def setUp(self):
        pass
    
    # E305: Add an extra blank line here
    def tearDown(self):
        pass
    
    # E302: Add an extra blank line here
    def test_add(self):
        result = add(3, 5)
        self.assertEqual(result, 8)
    
    # E302: Add an extra blank line here
    def test_subtract(self):
        result = subtract(10, 5)
        self.assertEqual(result, 5)
    

# E302: Add an extra blank line here
if __name__ == '__main__':
    unittest.main()

# W293: Remove any trailing whitespace after the last line
