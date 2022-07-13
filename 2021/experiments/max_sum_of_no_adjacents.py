# Find de max sum of three not adjacents numbers in an array


def maxSubsetSumNoAdjacent(array):
  if not len(array):
    return 0
  elif len(array) == 1:
    return array[0]
  max_sums = [array[0], max(array[0], array[1])]
  for i in range(2, len(array)):
    max_sums.append(max(max_sums[i - 1], max_sums[i - 2] + array[i]))
  return max_sums[-1]



