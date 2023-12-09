import re


def load_data_from_file():
    # with open('data_example_1.txt', 'r') as file:
    with open('data.txt', 'r') as file:
        lines = file.readlines()
        seeds = list(map(int, re.findall(r'[\d]+', lines[0])))
        lines_where_maps_start = lines[2:]
        maps = []
        current_ranges = []
        for line in lines_where_maps_start:
            fuck_new_line = line.strip('\n')
            if re.search(r'map', fuck_new_line):
                if len(current_ranges):
                    maps.append(current_ranges)
                    current_ranges = []
            else:
                if len(fuck_new_line) > 0:
                    range = [int(num) for num in fuck_new_line.split()]
                    current_ranges.append(range)
        maps.append(current_ranges)
        return seeds, maps


def questions_einz(seeds, maps):
    locations = []
    for current_number in seeds:
        for das_map in maps:
            for dst, src, rng in das_map:
                if src <= current_number < src + rng:
                    idx = current_number - src
                    current_number = dst + idx
                    break
        locations.append(current_number)

    return min(locations)


def question_zwei(seeds, maps):
    # groups = [[seeds[i] + j for j in range(seeds[i + 1])] for i in range(0, len(seeds), 2)] NO!
    # the_champs = []
    # for g in groups:
    #     champen = questions_einz(g, maps)
    #     the_champs.append(champen)
    # return min(the_champs)

    groups = [(seeds[i], seeds[i] + seeds[i + 1] - 1) for i in range(0, len(seeds), 2)]

    maps.reverse()

    location_to_check = 0
    while True:
        current_number = location_to_check
        if not current_number % 10000:
            print(current_number)
        for das_map in maps:
            for src, dst, rng in das_map:
                if src <= current_number < src + rng:
                    idx = current_number - src
                    current_number = dst + idx
                    # print(current_number)
                    break

        for g in groups:
            if g[0] <= current_number < g[1]:
                return location_to_check

        location_to_check += 1


def do_it():
    seeds, maps = load_data_from_file()

    print(f"seeds: {seeds}")

    print(f"Maps:")

    for i, m in enumerate(maps):
        print(f"  Map {i}: {m}")

    answer_1 = questions_einz(seeds, maps)
    print(f"Answer 1: {answer_1}")

    answer_2 = question_zwei(seeds, maps)
    print(f"Answer 2: {answer_2}")


do_it()
