import re


def load_data_from_file():
    with open('data.txt', 'r') as file:
        lines = file.readlines()
        lines = [line.strip() for line in lines]

        times = list(map(int, lines[0].split()[1:]))
        distances = list(map(int, lines[1].split()[1:]))

        return times, distances

def get_wins_from_race(race_time, distance_to_beat):
    print(f"race_time: {race_time}, distance_to_beat: {distance_to_beat}")
    win_counter = 0
    was_winning = False
    for hold_time in range(0, race_time):
        speed = hold_time
        move_time = race_time - hold_time
        distance = speed * move_time
        win = distance > distance_to_beat

        if not win and was_winning:
            break

        was_winning = win
        if win:
            win_counter += 1
        print(f"hold_time: {hold_time}, speed: {speed}, distance: {distance}")
    return win_counter

def questions_einz(times, distances):
    times_and_distances = list(zip(times, distances))
    answer = 1

    for race_time, distance_to_beat in times_and_distances:
        wins = get_wins_from_race(race_time, distance_to_beat)
        answer *= wins
    return answer


def question_zwei(times, distances):
    total_time = int(''.join(map(str, times)))
    total_distance = int(''.join(map(str, distances)))

    return get_wins_from_race(total_time, total_distance)


def do_it():
    times, distances = load_data_from_file()

    answer_1 = questions_einz(times, distances)
    print(f"Answer 1: {answer_1}")

    answer_2 = question_zwei(times, distances)
    print(f"Answer 2: {answer_2}")


do_it()
