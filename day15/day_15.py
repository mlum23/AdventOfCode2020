def last_occurrence(value, array_num):
    indices = [i for i in range(len(array_num)) if array_num[i] == value]

    descending_order = indices[::-1]
    return descending_order[0] - descending_order[1]


def num_occurrence(value, array_num):
    occurrence = 0
    for num in array_num:
        if num == value: occurrence += 1

    return occurrence


def part_one(file_name):
    with open(file_name, 'r') as file:
        nums = file.read().split(',')
        nums = [int(num) for num in nums]

        for i in range(len(nums) - 1, 2020):
            if num_occurrence(nums[i], nums) == 1:
                nums.append(0)
            else:
                nums.append(last_occurrence(nums[i], nums))

        print(nums[2019])

def main():
    input_file = './input.txt'
    part_one(input_file)


if __name__ == "__main__":
    main()
