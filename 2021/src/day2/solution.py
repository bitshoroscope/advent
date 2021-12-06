def get_position():
    with open('../../resources/day2_input.txt') as f:
        originalLines = f.readlines()
        cleanedLines = [line.strip() for line in originalLines]
        x = 0
        y = 0
        for instruction in cleanedLines:
            direction, value = instruction.split()
            if direction == 'forward':
                x += int(value)
            elif direction == 'down':
                y += int(value)
            elif direction == 'up':
                y -= int(value)
        return x * y

def get_position_and_aim():
    with open('../../resources/day2_input.txt') as f:
        originalLines = f.readlines()
        cleanedLines = [line.strip() for line in originalLines]
        x = 0
        y = 0
        aim = 0
        for instruction in cleanedLines:
            direction, value = instruction.split()
            if direction == 'forward':
                x += int(value)
                y += aim * int(value)
            elif direction == 'down':
                aim += int(value)
            elif direction == 'up':
                aim -= int(value)
        return x * y

print(get_position())
print(get_position_and_aim())