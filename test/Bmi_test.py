import unittest
from src.BMI import Bmi_test

class MyTestCase(unittest.TestCase):
    def test_zero_dividing(self):

        #sub_values
        weight_1 = 0
        weight_2 = 0
        weight_3 = 3

        height_1 = 0
        height_2 = 3
        height_3 = 1

        #assume
        expected1 = 0
        expected2 = 0
        expected3 = 3


        #action
        result1 = Bmi_test.Bmi_calc(weight_1, height_1)
        result2 = Bmi_test.Bmi_calc(weight_2, height_2)
        result3 = Bmi_test.Bmi_calc(weight_3, height_3)


        #expect/assert
        self.assertEqual(result1,expected1)
        self.assertEqual(result2, expected2)
        self.assertEqual(result3, expected3)

if __name__ == '__main__':
    unittest.main()
