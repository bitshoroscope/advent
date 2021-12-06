def diagnostic():
    with open('../../resources/day3_input.txt') as f:
        lines = f.readlines()
        transposed_lines = transpose_input(lines)
        gamma = ''
        for word in transposed_lines:
            counter_ones, counter_zeros = get_bit_counters(word)
            if(counter_ones > counter_zeros):
                gamma += '1'
            else:
                gamma += '0'
        gamma_rate = int(gamma,2)
        epsilon_rate = int(invert_binary(gamma),2)
        return gamma_rate * epsilon_rate

def get_life_support_rating():
    with open('../../resources/day3_input.txt') as f:
        lines = f.readlines()
        lines = [line.strip() for line in lines]
        transposed_lines_len = len(lines[0])
        filtered_oxy = get_indicator(lines, transposed_lines_len, "filter_oxygen")
        filtered_co2 = get_indicator(lines, transposed_lines_len, "filter_co2")
        return int(filtered_oxy,2) * int(filtered_co2,2)


def get_indicator(filtered_lines, transposed_lines_len, filter_name):
    index = 0
    index_bits = 0
    while index_bits < transposed_lines_len:
        transposed_lines = transpose_input(filtered_lines)
        counter_ones, counter_zeros = get_bit_counters(transposed_lines[index_bits])
        if filter_name == 'filter_oxygen':
            my_filter = '1' if counter_ones >= counter_zeros else '0'
        else:
            my_filter = '0' if counter_zeros <= counter_ones else '1'
        filtered_lines = [line for line in filtered_lines if line[index] == my_filter]
        if len(filtered_lines) == 1:
            break
        else:
            index += 1
        index_bits += 1
    return filtered_lines[0]


def transpose_input(read_lines):
    lines = [line.strip() for line in read_lines]
    transposed_lines = [''.join(chars) for chars in zip(*lines)]
    return transposed_lines


def get_bit_counters(word):
    counter_ones = 0
    counter_zeros = 0
    for bit in word:
        if bit == '0':
            counter_zeros += 1
        elif bit == '1':
            counter_ones += 1
    return counter_ones, counter_zeros


def invert_binary(number):
    res = ''
    for bit in number:
        if bit == '0':
            res += '1'
        elif bit == '1':
            res += '0'
    return res



# print(diagnostic())
print(get_life_support_rating())