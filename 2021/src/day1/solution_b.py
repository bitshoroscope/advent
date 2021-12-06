
def read_data():
    return [int(line.strip()) for line in open('../../resources/day1_input_a.txt', 'r')]

def get_depth_counter(size_chunk=3):
    data = read_data()
    counter = -1
    currentDepth = 0
    for index, value in enumerate(data):
        depth = 0
        nextValues = data[index+1:index + size_chunk]
        depth += value + sum(nextValues)
        if int(depth) > currentDepth:
            counter += 1
        currentDepth = int(depth)
    return counter

print(get_depth_counter())