import unittest
from calculator import add, subtract, divide

class TestCalculatorMethods(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        print("Starting testing")
        
    def setUp(self):
        print("Starting testcase")
    
    def test_add_positive_number(self):
        self.assertEqual(add(1,3),4)
        
    def test_subtract_mix_numbers(self):
        self.assertEqual(subtract(-1, 2), -3)

    @unittest.skip("This Testcase going to be skip")
    def test_divide_by_zero(self):
        with self.assertRaises(ValueError):
            divide(10,0)

    def tearDown(self):
        print("Ended Testcase")
    
    @classmethod
    def tearDownClass(cls):
            print("Ended Testing")
            

if __name__ == "__main__":
    unittest.main()
