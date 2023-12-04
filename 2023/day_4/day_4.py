def load_data_from_file():
    with open('data_example_1.txt', 'r') as file:
        cards = []
        for line in file:
            line_w_o_the_card_name_shit = line.split(":")[1].strip()
            numberz_linez = line_w_o_the_card_name_shit.split(" | ")

            winning = [int(num) for num in numberz_linez[0].split()]
            mine = [int(num) for num in numberz_linez[1].split()]
            card_content = [winning, mine]

            cards.append(card_content)
        return cards


def get_number_of_matches(card):
    intersects = set(card[0]).intersection(set(card[1]))
    return len(intersects)


def questions_einz(cards):
    sum = 0
    for card in cards:
        if matching := get_number_of_matches(card):
            print(matching)
            sum += 2 ** (matching - 1)
    return sum


def question_zwei(cards):
    card_len = len(cards)
    card_amounts = [1 for _ in range(card_len)]
    for i in range(card_len):
        if matching := get_number_of_matches(cards[i]):
            amount = card_amounts[i]
            for k in range(i + 1, min(i + 1 + matching, card_len)):
                card_amounts[k] += amount
    return sum(card_amounts)


card_data = load_data_from_file()

answer_1 = questions_einz(card_data)
print(f"Answer 1: {answer_1}")

answer_2 = question_zwei(card_data)
print(f"Answer 2: {answer_2}")
