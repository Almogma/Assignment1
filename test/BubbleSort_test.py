import unittest
from src.BubbleSort import BubbleSort


class MyTestCase(unittest.TestCase):
    def test_sort(self):

        #sub_values
        arr_1 = [-1,-10,6,5]
        arr_2 = [-1,3,5,10]
        arr_3 = ['a','y','d']

        #assume
        expected1 = [-10,-1,5,6]
        expected2 = [-1,3,5,10]
        expected3 = ['a','d','y']

        #action
        result1 = BubbleSort.bubbleSort(arr_1)
        result2 = BubbleSort.bubbleSort(arr_2)
        result3 = BubbleSort.bubbleSort(arr_3)


        #expect/assert
        self.assertEqual(result1,expected1)
        self.assertEqual(result2, expected2)
        self.assertEqual(result3, expected3)

    def invalid_input(self):

        #sub_values
        arr_1 = [-1,-10,6,5,'a','z','c']

        # assume
        expected1 = TypeError

        #expect/assert
        self.assertRaises(expected1, BubbleSort.bubbleSort(arr_1))



if __name__ == '__main__':
    unittest.main()
