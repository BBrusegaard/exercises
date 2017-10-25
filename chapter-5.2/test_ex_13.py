from ex_5_13 import falling_distance
import unittest

class TestFallingDistance(unittest.TestCase):
    
    def test_one_second(self):
        expected = 4.9
        actual = falling_distance(1)
        self.assertEqual(expected, actual)
    
    def test_zero_second(self):
        expected = 0
        actual = falling_distance(0)
        self.assertEqual(expected, actual)
        
unittest.main()