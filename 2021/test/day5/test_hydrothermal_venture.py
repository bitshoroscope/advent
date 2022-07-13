from day5 import hydrothermal_venture as sol


def test_parse_line():
  vent = [[[0, 9], [5, 9]], [[8, 0], [0, 8]]]
  input = ['0,9 -> 5,9\n', '8,0 -> 0,8']
  assert vent == sol.get_points(input)


def test_sequence_generator():
  input = [[0, 9], [5, 9]]
  sequence = sol.transform_to_sequence(input)
  assert sequence == [[0, 9], [1, 9], [2, 9], [3, 9], [4, 9], [5, 9]]

  input = [[0, 1], [0, 5]]
  sequence = sol.transform_to_sequence(input)
  assert sequence == [[0, 1], [0, 2], [0, 3], [0, 4], [0, 5]]
