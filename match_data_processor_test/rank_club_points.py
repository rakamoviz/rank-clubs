import unittest
import os, sys

p = os.path.abspath('.')
sys.path.insert(1, p)

import match_data_processor

class Test(unittest.TestCase):
	'''
    Test the rank_club_points function from the match_data_processor
    '''

	cases = [
		{
			'name': 'point_table contains tie (FC Awesome and Snakes)', 
			'point_table': {'Lions': 5, 'Snakes': 1, 'Tarantulas': 6, 'FC Awesome': 1, 'Grouches': 0},
			'expected': [
				('Tarantulas', 6),
				('Lions', 5),
				('FC Awesome', 1),
				('Snakes', 1),
				('Grouches', 0)
			]
		},
	]
	
	def test_rank_club_points(self):
		print('\ntest_rank_club_points')

		for case in Test.cases:			
			actual = match_data_processor._rank_club_points(
				case['point_table']
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