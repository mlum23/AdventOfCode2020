def part_one(file_path):
    """
    Returns the number of valid passwords.

    Each line in the file must be formatted as below:

    L-U @: password\n

    Where L is the lower-bound integer
          U is an upper-bound integer
          @ is a lowercase letter,
          password is a string with lowercase letters only.

    The password is valid if there are L to U inclusive many @'s in the password.

    :param file_path: the name of the file.
    :return: the number of valid passwords, as an integer.
    """
    num_valid_passwords = 0
    with open(file_path, 'r') as file:
        for line in file:
            context = line.split(' ')
            limit = context[0].split('-')
            min_limit = int(limit[0])
            max_limit = int(limit[1])

            letter = context[1].split(':')[0]
            password = context[2].split('\n')[0]

            count = password.count(letter)

            if min_limit <= count <= max_limit:
                num_valid_passwords += 1

    return num_valid_passwords


def part_two(file_path):
    """
    Returns the number of valid passwords.

    Each line in the file must be formatted as below:

    L-U @: password\n

    Where L is the lower-bound integer
          U is an upper-bound integer
          @ is a lowercase letter,
          password is a string with lowercase letters only.

    The password is valid if there is only one occurrence of @ at the
    L-th position or U-th position of the password.

    :param file_path:
    :return: the number of valid passwords, as an integer.
    """
    num_valid_passwords = 0

    with open(file_path, 'r') as file:
        for line in file:
            context = line.split(' ')
            limit = context[0].split('-')
            min_limit = int(limit[0])
            max_limit = int(limit[1])

            letter = context[1].split(':')[0]
            password = context[2].split('\n')[0]

            if password[min_limit - 1] == letter:
                if password[max_limit - 1] != letter:
                    num_valid_passwords += 1

            else:
                if password[max_limit - 1] == letter:
                    num_valid_passwords += 1

    return num_valid_passwords


def main():
    file_path = './input.txt'

    print(part_one(file_path))
    print(part_two(file_path))


if __name__ == "__main__":
    main()
