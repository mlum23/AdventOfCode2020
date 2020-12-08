ACC_CHANGE_VALUE = 1
NOP_CHANGE_VALUE = 1
INITIAL_INDEX = 0
INITIAL_ACC = 0


def part_one(file_name):
    """
    Prints the accumulator total before instruction is executed a second time.

    :param file_name: the name of the file which contains the instructions, as a string.
    """
    acc = INITIAL_ACC
    index = INITIAL_INDEX
    visited_indices = []
    with open(file_name, 'r') as file:
        instructions = file.read().split('\n')
        while index not in visited_indices:
            visited_indices.append(index)
            instruction = instructions[index].split(' ')
            argument = instruction[0]
            value = int(instruction[1].replace('+', ''))
            if argument == 'acc':
                acc += value
                index += ACC_CHANGE_VALUE
            elif argument == 'nop':
                index += NOP_CHANGE_VALUE
            elif argument == 'jmp':
                index += value

    print(f'Accumulator value before any '
          f'instruction is executed a second time: {acc}')


def part_two(file_name):
    """
    Finds the accumulator total after swapping exactly one of jmp and nop and
    it does not cause an infinite loop.

    If the instruction is jmp, change it to nop, and vice versa.

    :param file_name: the name of the file, as a string.
    """
    acc = INITIAL_ACC
    index = INITIAL_INDEX
    visited_indices = []
    swap_successful = False

    with open(file_name, 'r') as file:
        instructions = file.read().split('\n')
        while index not in visited_indices:
            visited_indices.append(index)

            instruction = instructions[index].split(' ')
            argument = instruction[0]
            value = int(instruction[1].replace('+', ''))
            if argument == 'acc':
                acc += value
                index += ACC_CHANGE_VALUE
            elif argument == 'nop':
                if not swap_successful:
                    already_visited = visited_indices.copy()  # Create a deep copy for running swapped version
                    swap_worked = run_swapped(instructions, already_visited, index + value, acc)

                    # If the swap did not work, update as usual
                    # Otherwise, treat nop as jmp
                    if not swap_worked:
                        index += NOP_CHANGE_VALUE
                    else:  # The swap algorithm worked, so no need to keep iterating
                        break
                else:
                    index += NOP_CHANGE_VALUE
            elif argument == 'jmp':
                if not swap_successful:
                    already_visited = visited_indices.copy()  # Create a deep copy for running swapped version
                    swap_worked = run_swapped(instructions, already_visited, index + NOP_CHANGE_VALUE, acc)

                    # If the swap did not work, update as usual
                    # Otherwise, treat jmp as nop
                    if not swap_worked:
                        index += value
                    else:  # The swap algorithm worked, so no need to keep iterating
                        break
                else:
                    index += value

            if index >= len(instructions):
                break


def run_swapped(instructions, already_visited_temp, index, acc):
    """
    Returns True if no infinite loop. False otherwise.

    This is a helper function for part_two.
    It runs starting from the place where we swapped jmp with nop, and vice versa

    :param instructions: the set of instructions, as an array of strings.
    :param already_visited_temp: an array of indices (instructions) that has
                                 already been executed, as an array of integers.
    :param index: the swapped index, as an integer
    :param acc: the accumulator total, as an integer
    :return: True if the set of instructions does not cause an infinite loop.
             False otherwise.
    """
    while index not in already_visited_temp:
        already_visited_temp.append(index)
        instruction = instructions[index].split(' ')
        argument = instruction[0]
        value = int(instruction[1].replace('+', ''))

        if argument == 'acc':
            acc += value
            index += ACC_CHANGE_VALUE
        elif argument == 'nop':
            index += NOP_CHANGE_VALUE
        elif argument == 'jmp':
            index += value

        if index >= len(instructions):  # Success
            print(f'Changing instruction at {index} worked!')
            print(f'Accumulator total: {acc}')
            return True

    return False


def main():
    input_file = './input.txt'
    part_one(input_file)
    part_two(input_file)


if __name__ == "__main__":
    main()
