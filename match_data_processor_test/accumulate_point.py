import unittest
import os, sys

p = os.path.abspath('.')
sys.path.insert(1, p)

import match_data_processor

class Test(unittest.TestCase):
	'''
    Test the accumulate_point function from the match_data_processor
    '''

	cases = [
		{
			'name': 'point_table is empty', 
			'club': 'Tarantulas', 
			'point': 2,
			'point_table': {},
			'expected': {'Tarantulas': 2}
		},
		{
			'name': 'point_table already has point for a club', 
			'club': 'Tarantulas', 
			'point': 1,
			'point_table': {'Tarantulas': 2},
			'expected': {'Tarantulas': 3}
		},	
		{
			'name': 'point_table already has point for several clubs', 
			'club': 'Tarantulas', 
			'point': 1,
			'point_table': {'Tarantulas': 2, 'Lions': 5},
			'expected': {'Tarantulas': 3, 'Lions': 5}
		},				
	]
	
	def test_accumulate_point(self):
		print('\ntest_accumulate_point')

		for case in Test.cases:			
			match_data_processor._accumulate_point(
				case['point_table'], case['club'], case['point']
			)
			self.assertEqual(
				case['expected'],
				case['point_table'],
				'failed case {} expected {}, actual {}'.format(
					case['name'], case['expected'], case['point_table']
				)
			)
			print('  case {}: checked'.format(case['name']))

if __name__ == '__main__':
    unittest.main()