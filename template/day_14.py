def part_one(file_name):
    with open(file_name, 'r') as file:
        group = file.read().split('\nmask')
        print(group[2])



def main():
    input_file = './input.txt'
    part_one(input_file)


if __name__ == "__main__":
    main()
