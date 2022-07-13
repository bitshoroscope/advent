min_x = float('inf')
min_y = float('inf')
max_x = float('-inf')
max_y = float('-inf')


def get_vent():
  overlaps = 0
  with open('../../resources/day5_input.txt') as f:
    lines = f.readlines()
    points = get_points(lines)
    initial_matrix = initialize_matrix()
    for row in points:
      vents = transform_to_sequence(row)
      for vent in vents:
        initial_matrix[vent[0]][vent[1]] += 1
        if initial_matrix[vent[0]][vent[1]] > 1:
          overlaps += 1
    print_matrix(initial_matrix)
    print(f'min_x:{min_x}, min_y:{min_y}, max_x:{max_x}, max_y:{max_y}')
    return overlaps


def print_matrix(matrix):
  transposed = [*zip(*matrix)]
  for tuple in transposed:
    row = ' '.join(map(str,tuple))
    print(row)

def transpose(matrix):
  return [*zip(*matrix)]

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

def set_min_pos(point):
  global min_x, min_y
  if point[0] < min_x:
    min_x = point[0]
  if point[1] < min_y:
    min_y = point[1]
  if min_x < min_y:
    min_y = min_x
  if min_y < min_x:
    min_x = min_y


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
    set_min_pos(starting)
    points.append(positions)
  return points


def transform_to_sequence(input):
  start = input[0]
  ending = input[1]
  x_start = start[0]
  y_start = start[1]
  x_ending = ending[0]
  y_ending = ending[1]
  sequence = []

  if x_ending < x_start:
    x_ending, x_start = x_start,x_ending
  if y_ending < y_start:
    y_ending, y_start = y_start,y_ending

  #vertical line
  if x_start == x_ending:
    for i in range(y_start, y_ending + 1):
      element = []
      element.append(x_start)
      element.append(i)
      sequence.append(element)
  #horizontal line
  if y_start == y_ending:
    for i in range(x_start, x_ending + 1):
      element = []
      element.append(i)
      element.append(y_start)
      sequence.append(element)
  return sequence


def initialize_matrix():
  return [[0 for x in range(max_x + 1)] for y in range(max_y + 1)]


def string_to_list(elem):
  return list(map(int, elem.split(",")))


print(get_vent())
