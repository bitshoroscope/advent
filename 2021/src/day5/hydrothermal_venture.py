min_x = 0
min_y = 0
max_x = float('-inf')
max_y = float('-inf')


def get_vent():
	with open('../../resources/day5_input.txt') as f:
		lines = f.readlines()
		points = get_points(lines)
		initial_matrix = initialize_matrix()
		for row in points:
			vents = transform_to_sequence(row)
			for vent in vents:
				initial_matrix[vent[0]][vent[1]] +=1
		print_matrix(initial_matrix)
		return points

def print_matrix(matrix):
	s = [[str(e) for e in row] for row in matrix]
	lens = [max(map(len, col)) for col in zip(*s)]
	fmt = '\t'.join('{{:{}}}'.format(x) for x in lens)
	table = [fmt.format(*row) for row in s]
	print('\n'.join(table))

# Get the max coordinate
def set_max_pos(point):
	global max_x, max_y
	if point[0] > max_x:
		max_x = point[0]
	if point[1] > max_y:
		max_y = point[1]
	if max_x > max_y:
		max_y = max_x
	if max_y > max_x:
		max_x = max_y

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
		set_max_pos(ending)
		points.append(positions)
	return points

# REvisar el caso cuando es descendete la secuencia 8,0 -> 0,8
def transform_to_sequence(input):
	start = input[0]
	ending = input[1]
	x_start = start[0]
	y_start = start[1]
	x_ending = ending[0]
	y_ending = ending[1]
	if x_start == x_ending:
		sequence = []
		for i in range(y_start, y_ending+1):
			element = []
			element.append(x_start)
			element.append(i)
			sequence.append(element)
	if y_start == y_ending:
		sequence = []
		for i in range(x_start, x_ending+1):
			element = []
			element.append(i)
			element.append(y_start)
			sequence.append(element)
	return sequence

def initialize_matrix():
	return [[0 for x in range(max_x+1)] for y in range(max_y+1)]

def string_to_list(elem):
	return list(map(int, elem.split(",")))

get_vent()