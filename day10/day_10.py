def part_one(file_name):
    with open(file_name, 'r') as file:
        diff_one = 1  # Include 0
        diff_three = 1  # Include the last number + 3
        numbers = file.read().splitlines()
        numbers = [int(num) for num in numbers]
        numbers.sort()

        for i in range(1, len(numbers)):
            diff = numbers[i] - numbers[i - 1]
            if diff == 1:
                diff_one += 1
            else:
                diff_three += 1
        print(numbers)
        print(f'Diff one: {diff_one}, Diff three: {diff_three}')
        print(f'Product of diff_1 and diff_3: {diff_one * diff_three}')

def main():
    input_file = './input.txt'
    part_one(input_file)


if __name__ == "__main__":
    main()
