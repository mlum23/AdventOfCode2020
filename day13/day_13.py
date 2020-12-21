import math

def part_one(file_name):
    with open(file_name, 'r') as file:
        earliest_time = int(file.readline())
        schedule = file.readline().split(',')
        bus_id = [int(id) for id in schedule if id != 'x']

        bus_time = []

        for bus in bus_id:
            factor = math.ceil(earliest_time / bus)
            bus_time.append(factor * bus)

        earliest_bus = min(bus_time)
        index_earliest_bus = bus_time.index(earliest_bus)
        wait_time = earliest_bus - earliest_time
        print(f'Earliest Bus: {bus_id[index_earliest_bus]}\n'
              f'Wait time: {wait_time}')
        print(f'Bus * wait time = {bus_id[index_earliest_bus] * wait_time}')


def main():
    input_file = './input.txt'
    part_one(input_file)


if __name__ == "__main__":
    main()
