import max_sum_of_no_adjacents as sum

def test_empty():
  assert 0 == sum.maxSubsetSumNoAdjacent([])

def test_single_element():
  value = 5
  assert value == sum.maxSubsetSumNoAdjacent([value])

def test_normal_array():
  assert 33 == sum.maxSubsetSumNoAdjacent([7,10,12,7,9,14])
  assert 28 == sum.maxSubsetSumNoAdjacent([7,10,12,7,9,6])
