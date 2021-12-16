from day4 import giant_squid as sol


def test_line_to_matrix():
	input = ['57  7  8 38 31', '17 96  5 12 18', '58 45 81 89  4', '73 51 93 32 10', '74 50 26  0 24', '',
			 '79 67 21 84 71', '25 22 19 80 13', '10 63 90 78 33', '93 50 89 58 87', '91  7 45  6 41', '']
	matrix_array = [
		[[57, 7, 8, 38, 31], [17, 96, 5, 12, 18], [58, 45, 81, 89, 4], [73, 51, 93, 32, 10], [74, 50, 26, 0, 24]],
		[[79, 67, 21, 84, 71], [25, 22, 19, 80, 13], [10, 63, 90, 78, 33], [93, 50, 89, 58, 87], [91, 7, 45, 6, 41]]
	]
	assert matrix_array == sol.input_to_tables(input)


def test_horizontal_winning():
	table = [[-1, -1, -1, -1, -1], [17, 96, 5, 12, 18], [58, 45, 81, 89, 4], [73, 51, 93, 32, 10], [74, 50, 26, 0, 24]]
	assert True == sol.check_horizontal_winning(0, table)

	table = [[1, 2, 3, 4, 5], [-1, -1, -1, -1, -1], [58, 45, 81, 89, 4], [73, 51, 93, 32, 10], [74, 50, 26, 0, 24]]
	assert True == sol.check_horizontal_winning(1, table)

	table = [[1, 2, 3, 4, 5], [1, 2, 3, 4, 5], [58, 45, 81, 89, 4], [73, 51, 93, 32, 10], [-1, -1, -1, -1, -1]]
	assert True == sol.check_horizontal_winning(4, table)

	table = [[1, 2, 3, 4, 5], [1, 2, 3, 4, 5], [58, 45, 81, 89, 4], [73, 51, 93, 32, 10], [-1, -1, -1, -1, 0]]
	assert False == sol.check_horizontal_winning(4, table)


def test_vertical_winning():
	table = [[-1, 2,3,4,5], [-1, 96, 5, 12, 18], [-1, 45, 81, 89, 4], [-1, 51, 93, 32, 10], [-1, 50, 26, 0, 24]]
	assert True == sol.check_vertical_winning(0, table)

	table = [[1, -1, 3, 4, 5], [1, -1, -1, -1, -1], [58, -1, 81, 89, 4], [73, -1, 93, 32, 10], [74, -1, 26, 0, 24]]
	assert True == sol.check_vertical_winning(1, table)

	table = [[1, 2, 3, 4, -1], [1, 2, 3, 4, -1], [58, 45, 81, 89, -1], [73, 51, 93, 32, -1], [-1, -1, -1, -1, -1]]
	assert True == sol.check_vertical_winning(4, table)

	table = [[1, 2, 3, 4, -1], [1, 2, 3, 4, -1], [58, 45, 81, 89, -1], [73, 51, 93, 32, -1], [-1, -1, -1, -1, 0]]
	assert False == sol.check_vertical_winning(4, table)


def test_mark():
	input = [5, 81, 24]
	table = [[57, 7, 8, 38, 31], [17, 96, 5, 12, 18], [58, 45, 81, 89, 4], [73, 51, 93, 32, 10], [74, 50, 26, 0, 24]]
	marked_table = [[57, 7, 8, 38, 31], [17, 96, -1, 12, 18], [58, 45, -1, 89, 4], [73, 51, 93, 32, 10],
					[74, 50, 26, 0, -1]]
	assert marked_table == sol.play_until_win(input, table)
