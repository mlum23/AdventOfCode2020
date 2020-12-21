def check_left_edge(value, map, row, col):
    num_occupied = 0
    right = map[row][col + 1]
    bot_right = map[row + 1][col + 1]
    down = map[row + 1][col]

    possible_directions = [right, bot_right, down]
    if row != 0:
        top_right = map[row - 1][col + 1]
        up = map[row - 1][col + 1]
        possible_directions.extend([top_right, up])

    for val in possible_directions:
        if val == '#':
            num_occupied += 1

    if value == 'L' and num_occupied == 0:
        return '#'
    elif value == '#' and num_occupied >= 4:
        return 'L'
    else:
        return value





def part_one(input_file):
    with open(input_file, 'r') as file:
        map = file.read().split('\n')
        num_occupied = 0
        prev_num_occupied = -1
        new_map = []
        while num_occupied != prev_num_occupied:
            for row in range(len(map)):
                for col in range(len(map[0])):
                    if col == 0:  # Left edge
                        value = check_left_edge(map[row][col], map, row, col)

def main():
    input_file = './input.txt'
    part_one(input_file)


if __name__ == "__main__":
    main()