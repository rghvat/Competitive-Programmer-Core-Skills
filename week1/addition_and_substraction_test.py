import addition_and_substraction
import unittest

class AddSub(unittest.TestCase):
    '''
    '''
    def test_1(self):
        self.assertEqual(
            addition_and_substraction.add_sub(2, 1, 3), 3
            )

    def test_2(self):
        self.assertEqual(
            addition_and_substraction.add_sub(2, 0, 3), -1
            )

    def test_3(self):
        self.assertEqual(
            addition_and_substraction.add_sub(0, 0, 0), 0
            )

    # def test_4(self):
    #     self.assertEqual(
    #         addition_and_substraction.add_sub(4, 1, 999),
    #         )
    # 1 0 1000

    def test_5(self):
        self.assertEqual(
            addition_and_substraction.add_sub(1, 0, 1000), 1999
            )

    def test_6(self):
        self.assertEqual(
            addition_and_substraction.add_sub(1, 1, 1000), -1
            )

if __name__ == '__main__':
    unittest.main()