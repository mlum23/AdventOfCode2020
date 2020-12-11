def part_one(file_name):
    """
    Returns the number that is not the sum of the 25 numbers before it.

    :param file_name: the name of the file, as a string.
    :return: the number that is not the sum of the 25 numbers before it, as an integer.
    """
    with open(file_name, 'r') as file:
        numbers = file.read().splitlines()
        numbers = [int(num) for num in numbers]

        # Create the initial 25 numbers
        previous_nums = [numbers[i] for i in range(25)]

        for i in range(25, len(numbers)):
            current_num = numbers[i]

            # Find if two numbers sum to current_num
            for prev_num_index in range(len(previous_nums)):
                num = previous_nums[prev_num_index]
                if num < current_num:
                    second_num = current_num - num

                    if second_num in previous_nums:
                        break

                # The 25th number does not match, meaning that the number does not sum up with the last 25 numbers
                if prev_num_index == len(previous_nums) - 1:
                    print(f'Did not find 2 numbers that sum to {current_num}')
                    return current_num

            previous_nums.pop(0)
            previous_nums.append(current_num)


def part_two(file_name, invalid_number):
    """
    Returns the sum of the smallest and largest numbers in the contiguous range.

    :param file_name: the name of the input file, as a string.
    :param invalid_number: the invalid number found in part one, as an integer.
    :return: the sum of the smallest and largest numbers in the contiguous range, as an integer
    """
    starting_index = 0
    index = 0
    result = invalid_number
    nums_sum_to_invalid_num = []
    with open(file_name, 'r') as file:
        numbers = file.read().splitlines()
        numbers = [int(num) for num in numbers]

        while result != 0:
            current_num = numbers[index + starting_index]
            result -= current_num
            index += 1
            nums_sum_to_invalid_num.append(current_num)

            # nums do not sum to the invalid number
            if result < 0:
                result = invalid_number
                nums_sum_to_invalid_num = []
                index = 0
                starting_index += 1

        # Found the numbers that sum to the invalid number
        nums_sum_to_invalid_num.sort()
        lowest_num = nums_sum_to_invalid_num[0]
        highest_num = nums_sum_to_invalid_num[len(nums_sum_to_invalid_num) - 1]
        sum_low_high = lowest_num + highest_num
        print(f'Lowest: {lowest_num}, Highest: {highest_num}, Sum: {sum_low_high}')
        return sum_low_high


def main():
    input_file = './input.txt'
    invalid_number = part_one(input_file)
    part_two(input_file, invalid_number)


if __name__ == "__main__":
    main()
