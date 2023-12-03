import re

number_word_dict = {"one": 1,
                    "two": 2,
                    "three": 3,
                    "four": 4,
                    "five": 5,
                    "six": 6,
                    "seven": 7,
                    "eight": 8,
                    "nine": 9, }

def generate_regex_expression(find_dem_words):
    welcome_this_is_da_beginning = '(?=(\d'
    for_every_ending_is_mega_starter = '))'
    seperator = '|'

    exp = welcome_this_is_da_beginning

    for word in find_dem_words:
        exp += seperator + word

    exp += for_every_ending_is_mega_starter
    return re.compile(exp)


def string_to_number(convert_this_shit):
    if convert_this_shit in number_word_dict:
        return number_word_dict[convert_this_shit]
    return int(convert_this_shit)


def line_to_number(line, regex):
    numbers = re.findall(regex, line)
    first = string_to_number(numbers[0])
    last = string_to_number(numbers[-1])
    return first * 10 + last


file1 = open('keys.txt', 'r')
lines = file1.readlines()

sum = 0

number_words = list(number_word_dict.keys())
reg_exp = generate_regex_expression(number_words)

for line in lines:
    n = line_to_number(line, reg_exp)
    print("line: " + line + " number: " + str(n))
    sum += n

print(sum)
