import increment 
import unittest
import time

class TestIncrementFunction(unittest.TestCase):
    '''
    testing increment function
    '''

    def test_1(self):
        self.assertEqual(
            increment.no_decimal_digit(1), 1)

    def test_2(self):
        self.assertEqual(
            increment.no_decimal_digit(9), 2)

    def test_3(self):
        self.assertEqual(
            increment.no_decimal_digit(999919), 6)

    def test_4(self):
        self.assertEqual(
            increment.no_decimal_digit(134), 3)

    def test_5(self):
        self.assertEqual(
            increment.no_decimal_digit(19), 2)
    
    def test_6(self):
        self.assertEqual(
            increment.no_decimal_digit(99), 3)

    def  test_7(self):
        self.assertEqual(
            increment.no_decimal_digit(89), 2)

    def test_8(self):
        self.assertEqual(
            increment.no_decimal_digit(899999999999999999999999999999), 30)

    def test_8(self):
        self.assertEqual(
            increment.no_decimal_digit(0), 1)

    def test_9(self):
        num = pow(10, 2)-1
        print(num)
        self.assertEqual(
            increment.no_decimal_digit(num), 3)

    def setUp(self):
        self.start_time = time.time()

    def tearDown(self):
        self.end_time = time.time()
        print("{} took {}".format(self.id, self.end_time - self.start_time))


if __name__ == '__main__':
    testsuite = unittest.TestLoader().loadTestsFromTestCase(TestIncrementFunction)
    unittest.TextTestRunner(verbosity = 0).run(testsuite)

