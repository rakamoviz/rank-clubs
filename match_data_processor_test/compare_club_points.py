import unittest
import os, sys

p = os.path.abspath('.')
sys.path.insert(1, p)

import match_data_processor

class Test(unittest.TestCase):
	'''
    Test the compare_club_points function from the match_data_processor
    '''

	cases = [
		{
			'name': 'club_1 has bigger point than club_2', 
			'club_point_1': ('Tarantulas', 6),
			'club_point_2': ('Lions', 5),
			'expected': 1
		},
	]
	
	def test_rank_club_points(self):
		print('\ntest_compare_club_points')

		for case in Test.cases:			
			actual = match_data_processor._compare_club_points(
				case['club_point_1'], case['club_point_2']
			)
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