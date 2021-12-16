class Point(object):
	def __init__(self, x, y):
		self.x = x
		self.y = y


def get_vent():
	with open('../../resources/day5_input.txt') as f:
		lines = f.readlines()
		points = get_points(lines)
		return points


def get_points(lines):
	pairs = [line.strip() for line in lines]
	points_pair = [pair.split(" -> ") for pair in pairs]
	points = []
	for elem in points_pair:
		positions = []
		starting = string_to_list(elem[0])
		ending = string_to_list(elem[1])
		positions.append(starting)
		positions.append(ending)
		points.append(positions)
	return points


def string_to_list(elem):
	return list(map(int, elem.split(",")))
