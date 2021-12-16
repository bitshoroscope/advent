from day5 import hydrothermal_venture as sol

def test_parse_line():
	vent = [[[0,9],[5,9]], [[8,0],[0,8]]]
	input = ['0,9 -> 5,9\n', '8,0 -> 0,8']
	assert vent == sol.get_points(input)