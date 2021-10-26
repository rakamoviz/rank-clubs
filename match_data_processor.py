import argparse
import sys
import re
import functools
import os

def _calculate_points(score_1, score_2):
	'''
	Calculate the points associated to each score in the parameters

    Parameters:
        score_1 (str):First score
		score_2 (str):Second score

    Returns:
        points_tuple (int, int):Returns the points associated to each score in the parameters
	'''

	if score_1 > score_2:
		return (3, 0)
	elif score_1 == score_2:
		return (1, 1)
	else:
		return (0, 3)

def _accumulate_point(point_table, club, point):
	'''
	Accumulate points for a club into point_table.

    Parameters:
        point_table ({club: point}):dictionary containing points accumulated for each club
		club (str):Club name
		point (int):Point to be added to the club
	'''

	if club in point_table:
		point_table[club] += point
	else:
		point_table[club] = point

def _compare_club_points(club_point_1, club_point_2):
	if club_point_1[1] < club_point_2[1]:
		return -1
	elif club_point_1[1] > club_point_2[1]:	
		return 1
	else:
		if club_point_1[0] > club_point_2[0]:
			return -1
		elif club_point_1[0] < club_point_2[0]:
			return 1
		else:
			return 0

def _rank_club_points(point_table):
	'''
	Rank the clubs according to accumulated points in descending order
	(i.e.: club with biggest points placed first in the result)

    Parameters:
        point_table ({club: point}):dictionary containing points accumulated for each club

	Returns:
        ranking (list((club, point))):Returns a list of tuple of (club, point), in descending order based on point
	'''

	ranked_club_points = list(point_table.items())
	ranked_club_points.sort(key=functools.cmp_to_key(_compare_club_points), reverse=True)
	return ranked_club_points

def _format_ranked_club_points(ranked_club_points):
	'''
	Print the ranking in '{position}. {club}, {point} pts' format

    Parameters:
        ranked_club_points (list((club, point))):a list of tuple of (club, point), in descending order based on point
	'''	
	return ['{}. {}, {} pts'.format(
		index+1, ranked_club_point[0], ranked_club_point[1]
	) for index, ranked_club_point in enumerate(ranked_club_points)]		

def process_match_data(match_data):
	'''
	Process the match data, with the result (ranking) being printed.

    Parameters:
        match_data (str):result of matches between clubs, separated by new line for each match.
	'''	

	point_table = {}
	
	result_pattern = re.compile('([a-zA-Z ]+) (0|[1-9]+), ([a-zA-Z ]+) (0|[1-9]+)')

	for result in match_data.splitlines():
		match = result_pattern.match(result)

		club_1 = match.group(1)
		score_1 = int(match.group(2))

		club_2 = match.group(3)
		score_2 = int(match.group(4))

		(point_1, point_2) = _calculate_points(score_1, score_2)

		_accumulate_point(point_table, club_1, point_1)
		_accumulate_point(point_table, club_2, point_2)

	ranked_club_points = _rank_club_points(point_table)
	
	print(os.linesep.join(
		_format_ranked_club_points(ranked_club_points)
	))
	
def _main():
	parser = argparse.ArgumentParser(description='Calculate ranking')
	parser.add_argument(
		'-f', '--file', 
		type=argparse.FileType('r'), 
		default=sys.stdin, 
		help='''
			file to read match results from.
			If not specified, data will be read from stdin.
			'''
	)
	args = parser.parse_args()
	match_data = args.file.read()
	
	process_match_data(match_data)

if __name__ == '__main__':
	_main()