def get_num_tress_in_path(file_name, right_slope, down_slope):
    """
    Returns the number of tress in the path.

    This is a generalized function for both part 1 and 2 of the problem.
    For the full problem description: https://adventofcode.com/2020/day/3

    :param file_name: the path of the file, as a string.
    :param right_slope: the right slope, as an integer.
    :param down_slope: the down slope, as an integer
    :return: the number of trees in the path, as an integer.
    """
    tree_count = 0
    right_index = right_slope

    with open(file_name, 'r') as file:
        flight_map = [line.replace('\n', '') for line in file]
        last_row = len(flight_map)
        right_max = len(flight_map[0])

        for down_index in range(down_slope, last_row, down_slope):
            if flight_map[down_index][right_index] == '#':
                tree_count += 1

            right_index += right_slope

            if right_index >= right_max:
                right_index = right_index % right_max

    return tree_count


def main():
    file = './input.txt'

    path_1 = get_num_tress_in_path(file, 1, 1)
    path_2 = get_num_tress_in_path(file, 3, 1)
    path_3 = get_num_tress_in_path(file, 5, 1)
    path_4 = get_num_tress_in_path(file, 7, 1)
    path_5 = get_num_tress_in_path(file, 1, 2)

    print(f'Path 1: {path_1} trees\n'
          f'Path 2: {path_2} trees\n'
          f'Path 3: {path_3} trees\n'
          f'Path 4: {path_4} trees\n'
          f'Path 5: {path_5} trees\n'
          f'Product of each path: {path_1 * path_2 * path_3 * path_4 * path_5}')


if __name__ == "__main__":
    main()
