import unittest
import os, sys

p = os.path.abspath('.')
sys.path.insert(1, p)

import match_data_processor

class Test(unittest.TestCase):
	'''
    Test the calculate_points function from the match_data_processor
    '''

	cases = [
		{
			'name': 'score_1 is bigger than score_2', 
			'score_1': 3, 
			'score_2': 1,
			'expected': (3, 0)
		},
		{
			'name': 'score_1 is equal to score_2', 
			'score_1': 2, 
			'score_2': 2,
			'expected': (1, 1)
		},
		{
			'name': 'score_1 is less than score_2', 
			'score_1': 1, 
			'score_2': 3,
			'expected': (0, 3)
		}
	]
	
	def test_calculate_points(self):
		print('\ntest_calculate_points')

		for case in Test.cases:			
			actual = match_data_processor._calculate_points(case['score_1'], case['score_2'])
			self.assertEqual(
				case['expected'],
				actual,
				'failed case {} expected {}, actual {}'.format(
					case['name'], case['expected'], actual
				)
			)
			print('  case {}: checked'.format(case['name']))

if __name__ == '__main__':
    unittest.main()