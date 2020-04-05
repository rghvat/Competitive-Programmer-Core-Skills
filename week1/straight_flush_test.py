import straight_flush
import unittest

class StraightFlush(unittest.TestCase):
	'''
	'''
	def test_1(self):
		'''
		'''
		self.assertEqual(
			straight_flush.flush('2H', '3H', '9H', '5H', 'AH'), 'NO'
			)

if __name__ == '__main__':
	unittest.main()