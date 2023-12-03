import re

symbol_coords = []
numbers = []
gear_coords = []


class NumberInfo:
    def __init__(self, value, x_start, x_end, y):
        self.value = value
        self.x_start = x_start
        self.x_end = x_end
        self.y = y
        self.coord_list = self.create_coord_list()

    def create_coord_list(self):
        coords = []
        for x in range(self.x_start, self.x_end+1):
            coords.append((x, self.y))
        return coords


def load_data_from_file():
    find_symbol_pattern = re.compile(r'[^a-zA-Z0-9.\s]')
    find_gear_pattern = re.compile(r'\*')
    find_number_pattern = re.compile(r'\d+')

    with open('data.txt', 'r') as file:
        for y, line in enumerate(file):
            for symbol_match in re.finditer(find_symbol_pattern, line):
                symbol_coords.append((symbol_match.start(), y))

            for gear_match in re.finditer(find_gear_pattern, line):
                gear_coords.append((gear_match.start(), y))

            for number_match in re.finditer(find_number_pattern, line):
                numbers.append(NumberInfo(int(number_match.group()), number_match.start(), number_match.end() - 1, y))


def is_coord_touching_symbol(coord, symbol_coords):
    c_x, c_y = coord
    for x in range(c_x - 1, c_x + 2):
        for y in range(c_y - 1, c_y + 2):
            if x == c_x and y == c_y:
                continue
            # print(f"{x}, {y}")

            if (x, y) in symbol_coords:
                # print(f"{(x, y)} is in symbol coords")
                return True
            # else:
                # print(f"{(x, y)} is not in symbol coords")

    return False


def is_coord_touching_number(coord, number):
    c_x, c_y = coord
    for x in range(c_x - 1, c_x + 2):
        for y in range(c_y - 1, c_y + 2):
            if x == c_x and y == c_y:
                continue

            if (x, y) in number.coord_list:
                return True

    return False


def point_on_the_doll_where_the_number_touched_you(number, symbol_coords):
    for digit_x in range(number.x_start, number.x_end+1):
        if is_coord_touching_symbol((digit_x, number.y), symbol_coords):
            return True
    return False


def ding_dong_song(gear_coord, number_list):
    touching_numbers = []

    for number in number_list:
        if is_coord_touching_number(gear_coord, number):
            touching_numbers.append(number)

    return touching_numbers


load_data_from_file()

answer_1 = 0

print("Symbol coords:")
for c in symbol_coords:
    print(f"  {c}")

print("Numbers:")
for n in numbers:
    isTouching = point_on_the_doll_where_the_number_touched_you(n, symbol_coords)
    print(f"  val: {n.value} x: {n.x_start}-{n.x_end} y: {n.y}")
    print(f"  is touching: {isTouching}")
    if isTouching:
        answer_1 += n.value

print(f"Answer 1: {answer_1}")

answer_2 = 0

for g in gear_coords:
    touches = ding_dong_song(g, numbers)
    if len(touches) == 2:
        answer_2 += touches[0].value * touches[1].value

print(f"Answer 2: {answer_2}")
