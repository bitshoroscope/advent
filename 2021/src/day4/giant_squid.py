import copy
from functools import reduce


def read_bingo_tables():
    with open('../../resources/day4_tables.txt') as f:
        lines = f.readlines()
        lines = [line.strip() for line in lines]
    lines.append('')
    return lines


def input_to_tables(array):
    tables = []
    table = []
    for element in array:
        if element == '':
            tables.append(table)
            table = []
        else:
            numbers = [int(x) for x in element.split()]
            table.append(numbers)
    return tables

def check_horizontal_winning(row, matrix):
    counter = 0
    for i in range (0,5,1):
        if matrix[row][i] == -1:
            counter +=1
        else:
            break
    return True if counter == 5 else False

def check_vertical_winning(col, matrix):
    counter = 0
    for i in range (0,5,1):
        if matrix[i][col] == -1:
            counter +=1
        else:
            break
    return True if counter == 5 else False


def play_until_win(input, matrix):
    marked_matrix = copy.deepcopy(matrix)
    numbers_elapsed = 0
    for number in input:
        numbers_elapsed += 1
        res = [(index, row.index(number)) for index, row in enumerate(matrix) if number in row]
        if len(res) != 0:
            row, col = res[0]
            marked_matrix[row][col] = -1
            if (check_horizontal_winning(row, marked_matrix) == True or check_vertical_winning(col, marked_matrix) == True):
                break
    return marked_matrix, numbers_elapsed, number


def play_bingo():
    min_plays = float('-inf')
    best_table = []
    best_winner_number = 0
    numbers = [38,54,68,93,72,12,33,8,98,88,21,91,53,61,26,36,18,80,73,47,3,5,55,92,67,52,25,40,56,95,9,62,30,31,85,65,14,2,78,75,15,39,87,27,58,42,60,32,41,83,51,77,10,66,70,4,37,6,89,23,16,49,48,63,94,97,86,64,74,82,7,0,11,71,44,43,50,69,45,81,20,28,46,79,90,34,35,96,99,59,1,76,22,24,17,57,13,19,84,29]
    lines = read_bingo_tables()
    tables = input_to_tables(lines)
    for table in tables:
        winner_table, plays, winner_number = play_until_win(numbers, table)
        # Change with -inf and < to first part
        if plays > min_plays:
            best_table = winner_table
            min_plays = plays
            best_winner_number = winner_number
    flatten_list = [j for sub in best_table for j in sub]
    not_played = [x for x in flatten_list if x != -1]
    total = reduce(lambda x, y: x + y, not_played)
    print(total)
    print(best_table, best_winner_number)
    print(total * best_winner_number)


play_bingo()
