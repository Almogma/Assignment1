import unittest
from src.BubbleSort import BubbleSort


class MyTestCase(unittest.TestCase):
    def test_sort(self):

        #sub_values
        arr_1 = [-1,-10,6,5]
        arr_2 = [-1,3,5,10]
        arr_3 = ['a','y','d']
        arr_4 = (1,5,3)
        arr_5 = map(lambda x: x *2 ,[1, 4, 2])
        arr_6 = filter(lambda x: x > 0, [-1,6,-10,9])

        #assume
        expected1 = [-10,-1,5,6]
        expected2 = [-1,3,5,10]
        expected3 = ['a','d','y']
        expected4 = [1,3,5]
        expected5 = [2, 4, 8]
        expected6 = [6,9]

        #action
        result1 = BubbleSort.bubbleSort(arr_1)
        result2 = BubbleSort.bubbleSort(arr_2)
        result3 = BubbleSort.bubbleSort(arr_3)
        result4 = BubbleSort.bubbleSort(arr_4)
        result5 = BubbleSort.bubbleSort(arr_5)
        result6 = BubbleSort.bubbleSort(arr_6)


        #expect/assert
        self.assertEqual(result1,expected1)
        self.assertEqual(result2, expected2)
        self.assertEqual(result3, expected3)
        self.assertEqual(result4, expected4)
        self.assertEqual(result5, expected5)
        self.assertEqual(result6, expected6)

    def invalid_input(self):

        #sub_values
        arr_1 = [-1,-10,6,5,'a','z','c']
        arr_2 = 3

        # assume
        expected1 = TypeError
        expected2 = -1

        result = BubbleSort.bubbleSort(arr_2)

        #expect/assert
        self.assertRaises(expected2, BubbleSort.bubbleSort(arr_2))





if __name__ == '__main__':
    unittest.main()
