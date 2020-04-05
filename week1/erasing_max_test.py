import erasing_max
import unittest

class removeElement(unittest.TestCase):
    '''
    assertListEqual order matters
    assertCountEqual order doesnot matter
    '''

    def test_1(self):
        self.assertListEqual(
            erasing_max.erasing_maximum([1, 3, 2]), 
            [1, 2])

    def test_2(self):
        self.assertListEqual(
            erasing_max.erasing_maximum([4, 1, 4, 2, 4, 3, 4]), 
            [4, 1, 4, 2, 3, 4])


    def test_3(self):
        self.assertListEqual(
            erasing_max.erasing_maximum([1, 2, 3, 4, 5, 6, 7, 8, 9, 10]),
            [1, 2, 3, 4, 5, 6, 7, 8, 9])

    def test_4(self):
        self.assertListEqual(
            erasing_max.erasing_maximum([3, 3, 3]), 
            [3, 3])

    def test_5(self):
        self.assertListEqual(
            erasing_max.erasing_maximum(
            [11, 18, 16, 1, 10, 18, 13, 12, 14, 17, 3, 2, 4, 7, 15, 5, 8, 9, 18, 6]),
            [11, 18, 16, 1, 10, 18, 13, 12, 14, 17, 3, 2, 4, 7, 15, 5, 8, 9,  6])


if __name__ == '__main__':
    unittest.main()