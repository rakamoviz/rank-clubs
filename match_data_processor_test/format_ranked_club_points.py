import unittest
import os, sys

p = os.path.abspath('.')
sys.path.insert(1, p)

import match_data_processor

class Test(unittest.TestCase):
	'''
    Test the format_ranked_club_points function from the match_data_processor
    '''

	cases = [
		{
			'name': 'success case (only case)', 
			'ranked_club_points':  [
				('Tarantulas', 6),
				('Lions', 5),
				('FC Awesome', 1),
				('Snakes', 1),
				('Grouches', 0)
			],
			'expected': [
				'1. Tarantulas, 6 pts',
				'2. Lions, 5 pts',
				'3. FC Awesome, 1 pts',
				'4. Snakes, 1 pts',
				'5. Grouches, 0 pts'
			]
		},
	]
	
	def test_format_ranked_club_points(self):
		print('\ntest_format_ranked_club_points')

		for case in Test.cases:			
			actual = match_data_processor._format_ranked_club_points(
				case['ranked_club_points']
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