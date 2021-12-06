from day1 import solution_a as sol

def test_skip_first_value():
    numbers = [151, 150, 148, 147, 154, 155 ]
    counter = 0
    for number in numbers[1:]:
        print(number)
        counter += 1
    assert counter == 5

def test_assert_counter():
    assert 1139 == sol.get_depth_counter()

def test_expression():
    even_squares = (x * x for x in range(10) if x % 2 == 0)
    print(next(even_squares))