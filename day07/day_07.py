def part_one(bags_list, search):
    found_list = []
    for bag in bags_list:
        separate = bag.split(' bags contain')
        bag_type = separate[0]
        bag_content = separate[1]
        if search in bag_content:
            found_list.append(bag_type)  # Append the result
            found_list.extend(part_one(bags_list, bag_type))  # Search its content
    return found_list


def part_two(bags_list, search):
    result = 0
    for bag in bags_list:
        separate = bag.split(' bags contain')
        bag_search = separate[0]

        if search in bag_search:
            contents = separate[1:]
            contents = contents[0].split(',')

            for content in contents:
                # base case
                if 'no other bags' in content:
                    print(f'{search} does not contain any bags!')
                    return 1

                other_bag = content.split(None, 1)
                quantity = int(other_bag[0])
                bag_type = other_bag[1].split(' bag')[0]
                print(other_bag)

                print(f'Inside {search}:There are {quantity} {bag_type}')

                result += quantity * part_two(bags_list, bag_type)
                if search == 'shiny gold':
                    result += quantity
                print(f'Inside {search}: Result after adding {quantity} {bag_type}: {result}')



    return result

def main():
    input_file = './input.txt'
    with open(input_file, 'r') as file:
        bags = [line for line in file]

    result = part_one(bags, 'shiny gold')
    result_unique = set()
    for r in result:
        result_unique.add(r)

    print(f'Part one: {len(result_unique)}')
    print(part_two(bags, 'shiny gold'))


if __name__ == "__main__":
    main()
