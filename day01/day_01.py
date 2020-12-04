def text_to_array(file_path):
    """
    Reads a file from file_path and returns its contents in an array.

    :param file_path: a string.
    :precondition: the file contains one integer per line.
    :return: the content of the file, as an array of integers.
    """
    with open(file_path, 'r') as file:
        next(file)
        list_of_numbers = [int(line) for line in file]
        return list_of_numbers


def product_two_numbers(array_of_numbers, total):
    """
    Returns the product of two numbers if their sum is equal to total.

    :param array_of_numbers: an array of integers.
    :param total: an integer.
    :return: the product of two numbers if their sum is equal.
             Otherwise, return None.
    """
    for number in array_of_numbers:
        second_number = total - number
        if second_number in array_of_numbers:
            print(f'First number: {number}\nSecond number: {second_number}')
            return number * second_number


def product_three_numbers(array_of_numbers, total):
    """
    Returns the product of three numbers if their sum is equal to total.

    :param array_of_numbers: an array of integers.
    :param total: an integer.
    :return: the product of three numbers if their sums is equal to total.
             Otherwise, return None.
    """
    for number in array_of_numbers:
        second_number = total - number
        numbers_less_than_second_number = [num for num in array_of_numbers if num < second_number]
        result = product_two_numbers(numbers_less_than_second_number, second_number)
        if result is not None:
            print(f'Third Number: {number}')
            return number * result


def main():
    input_file = 'input.txt'
    total = 2020
    list_of_numbers = text_to_array(input_file)

    # Part 1
    result_two_numbers = product_two_numbers(list_of_numbers, total)

    if result_two_numbers is not None:
        print(f'Product of two numbers that sum to 2020: {result_two_numbers}')
    else:
        print(f'No two numbers add up to {total}')

    print('=' * 20)
    # Part 2
    result_three_numbers = product_three_numbers(list_of_numbers, total)

    if result_three_numbers is not None:
        print(f'Product of three numbers that sum to 2020: {result_three_numbers}')
    else:
        print(f'No three numbers add up to {total}')


if __name__ == "__main__":
    main()
