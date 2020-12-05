import math


def calculate(letter, lower_bound, upper_bound, position):
    """
    Returns the bound value for either the upper or lower half.

    This is a helper function for the find_seat function.

    :param letter: the letter F, B, L, or R, as a string.
    :param lower_bound: the lower bound of the range, as an integer.
    :param upper_bound: the upper bound of the range, as an integer.
    :param position: the current position of the whole string, as an integer.
    :return: the modified value for the bound, as an integer.
    """
    lower_bound_letter = ['F', 'L']
    upper_bound_letter = ['B', 'R']
    position_check = [6, 9]

    if letter in lower_bound_letter:
        if position in position_check:
            return lower_bound
        return math.floor((upper_bound + lower_bound) / 2)

    elif letter in upper_bound_letter:
        if position in position_check:
            return upper_bound
        return math.ceil((upper_bound + lower_bound) / 2)


def find_seat(input_file):
    """
    Prints the highest seat ID and our seat ID.

    :param input_file: the name of the file, as a string.
    """
    seat_id = []
    multiplication_constant = 8

    with open(input_file, 'r') as file:
        for line in file:
            current_row = 0
            current_col = 0
            min_row = 0
            max_row = 127

            min_col = 0
            max_col = 7

            line = line.replace('\n', '')
            chars = [char for char in line]

            for i in range(len(chars)):
                if chars[i] == 'F':
                    max_row = calculate(chars[i], min_row, max_row, i)
                    current_row = calculate(chars[i], min_row, max_col, i)
                elif chars[i] == 'B':
                    min_row = calculate(chars[i], min_row, max_row, i)
                    current_row = max_row
                elif chars[i] == 'R':
                    min_col = calculate(chars[i], min_col, max_col, i)
                    current_col = max_col
                elif chars[i] == 'L':
                    max_col = calculate(chars[i], min_col, max_col, i)
                    current_col = min_col

            seat_id.append((current_row * multiplication_constant) + current_col)

    print(f'Highest seat ID: {max(seat_id)}')
    seat_id.sort()

    for i in range(len(seat_id) - 2):
        expected_next_seat = seat_id[i] + 1

        if expected_next_seat != seat_id[i + 1]:
            print(f'Our seat number: {expected_next_seat}')


def main():
    input_file = './input.txt'
    find_seat(input_file)


if __name__ == "__main__":
    main()
