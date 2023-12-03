class Game:
    def __init__(self, *handfuls):
        self.handfuls = handfuls

    def get_highest(self, color):
        highest = 0
        for h in self.handfuls:
            if color in h.colors:
                count = h.colors[color]
                highest = max(highest, count)

        return highest

    def get_lowest(self, color):
        lowest = 999
        for h in self.handfuls:
            if color in h.colors:
                count = h.colors[color]
                lowest = min(lowest, count)

        return lowest

    def is_color_in_limit(self, color, limit):
        return self.get_highest(color) <= limit

    def is_colors_in_limit(self, **limits_to_test):
        for key in limits_to_test:
            if not self.is_color_in_limit(key, limits_to_test[key]):
                return False
        return True

    def the_power_of_love(self, *colors):
        result = 1
        for c in colors:
            result *= self.get_highest(c)
        return result


class Handful:
    def __init__(self, **colors):
        self.colors = colors


def load_data_from_file():
    games = []

    with open('data.txt', 'r') as file:
        for line in file:
            game_data = line.split(":")[1].strip()
            handful = game_data.split(';')
            rounds = []
            for handful_content in handful:
                colors = {}
                for color_and_count in handful_content.split(','):
                    color_and_count = color_and_count.strip().split()
                    color = color_and_count[1]
                    count = int(color_and_count[0])
                    colors[color] = count
                rounds.append(Handful(**colors))
            games.append(Game(*rounds))

    return games


limits = {"red": 12,
          "green": 13,
          "blue": 14, }
color_keys = list(limits.keys())

games = load_data_from_file()

answer_1 = 0
answer_2 = 0

for i, game in enumerate(games, 1):
    print(f"Game {i}:")
    for j, handful in enumerate(game.handfuls, 1):
        print(f"  Round {j}: {handful.colors}")
    if game.is_colors_in_limit(**limits):
        answer_1 += i
    print(f"highest red {game.get_highest('red')}")
    print(f"Is game possible: {game.is_colors_in_limit(**limits)}")

    answer_2 += game.the_power_of_love(*color_keys)

print(f"answer einz: {answer_1}")
print(f"answer zwei: {answer_2}")
