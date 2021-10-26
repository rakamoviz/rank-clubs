import unittest
import calculate_points
import accumulate_point
import compare_club_points
import rank_club_points
import format_ranked_club_points

def _run():
	suite = unittest.TestSuite()
	result = unittest.TestResult()
	_addTests(suite)
	runner = unittest.TextTestRunner()
	print(runner.run(suite))

def _addTests(suite):
	suite.addTest(unittest.makeSuite(calculate_points.Test))
	suite.addTest(unittest.makeSuite(accumulate_point.Test))
	suite.addTest(unittest.makeSuite(compare_club_points.Test))
	suite.addTest(unittest.makeSuite(rank_club_points.Test))
	suite.addTest(unittest.makeSuite(format_ranked_club_points.Test))

_run()