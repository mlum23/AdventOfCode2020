def part_one(input_file):
    with open(input_file, 'r') as file:
        commands = file.read().split('\n')
        directions = ['E', 'S', 'W', 'N']
        east_west_val = 0
        north_south_val = 0

        direction_index = 0  # initially east

        for command in commands:
            direction = command[0]
            value = int(command[1:])
            print(direction_index)
            print(f'{direction}, {value}, {directions[direction_index]}')
            if direction == 'F':
                if direction_index % 2 == 0:
                    if directions[direction_index] == 'E':
                        east_west_val += value
                    else:
                        east_west_val -= value
                else:
                    if directions[direction_index] == 'N':
                        north_south_val += value
                    else:
                        north_south_val -= value

            elif direction == 'R':
                if value == 90:
                    direction_index = (direction_index + 1) % 4
                elif value == 180:
                    direction_index = (direction_index + 2) % 4
                elif value == 270:
                    direction_index = (direction_index + 3) % 4

            elif direction == 'L':
                if value == 90:
                    direction_index = direction_index - 1
                elif value == 180:
                    direction_index = direction_index - 2
                elif value == 270:
                    direction_index = direction_index - 3
                if direction_index < 0:
                    direction_index = 4 - abs(direction_index)

            elif direction == 'E':
                east_west_val += value

            elif direction == 'W':
                east_west_val -= value

            elif direction == 'N':
                north_south_val += value

            elif direction == 'S':
                north_south_val -= value

            print(f'East/West: {east_west_val}\n'
                  f'North/South: {north_south_val}')


    print(f'East/West: {abs(east_west_val)}\n'
          f'North/South: {abs(north_south_val)}\n'
          f'Manhattan Distance: {abs(north_south_val) + abs(east_west_val)}')


def part_two(input_file):
    with open(input_file, 'r') as file:
        commands = file.read().split('\n')
        directions = ['E', 'S', 'W', 'N']
        east_west_val = 0
        north_south_val = 0

        east_waypoint = 10
        north_waypoint = 1

        direction_index = 0  # initially east
        for command in commands:
            direction = command[0]
            value = int(command[1:])

            print(f'{direction}, {value}, {directions[direction_index]}')

            if direction == 'F':
                east_west_val += value * east_waypoint
                north_south_val += value * north_waypoint

            elif direction == 'R':
                if value == 90:
                    direction_index = (direction_index + 1) % 4
                    current_direction = directions[direction_index]
                    temp_east = east_waypoint
                    east_waypoint = north_waypoint
                    north_waypoint = temp_east

                elif value == 180:
                    direction_index = (direction_index + 2) % 4

                elif value == 270:
                    direction_index = (direction_index + 3) % 4
                    temp_east = east_waypoint
                    east_waypoint = north_waypoint
                    north_waypoint = temp_east

                if current_direction == 'S':
                    north_waypoint = -north_waypoint
                elif current_direction == 'W':
                    east_waypoint = -east_waypoint

            elif direction == 'L':
                if value == 90:
                    direction_index = direction_index - 1
                    temp_east = east_waypoint
                    east_waypoint = north_waypoint
                    north_waypoint = temp_east

                elif value == 180:
                    direction_index = direction_index - 2

                elif value == 270:
                    direction_index = direction_index - 3
                    temp_east = east_waypoint
                    east_waypoint = north_waypoint
                    north_waypoint = temp_east
                if direction_index < 0:
                    direction_index = 4 - abs(direction_index)

                if directions[direction_index] == 'S' and north_waypoint > 0:
                    north_waypoint = -north_waypoint
                elif directions[direction_index] == 'W' and east_waypoint > 0:
                    east_west_val = -east_waypoint

            elif direction == 'E':
                east_waypoint += value

            elif direction == 'W':
                east_waypoint -= value

            elif direction == 'N':
                north_waypoint += value

            elif direction == 'S':
                north_waypoint -= value

            print(f'East/West: {east_west_val}\n'
                  f'North/South: {north_south_val}\n'
                  f'East waypoint: {east_waypoint}\n'
                  f'North waypoint: {north_waypoint}\n')


    print(f'East/West: {abs(east_west_val)}\n'
          f'North/South: {abs(north_south_val)}\n'
          f'Manhattan Distance: {abs(north_south_val) + abs(east_west_val)}')



def main():
    input_file = './input.txt'
    # input_file = './sample.txt'
    # part_one(input_file)
    part_two(input_file)


if __name__ == "__main__":
    main()
