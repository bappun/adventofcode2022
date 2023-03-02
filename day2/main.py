score_by_result = {
    "LOSE": 0,
    "DRAW": 3,
    "WIN": 6,
}

score_by_shape = {
    "ROCK": 1,
    "PAPER": 2,
    "SCISSORS": 3,
}

letter_to_shape = {
    "A": "ROCK",
    "B": "PAPER",
    "C": "SCISSORS",
    "X": "ROCK",
    "Y": "PAPER",
    "Z": "SCISSORS",
}

letter_to_desired_result = {
    "X": "LOSE",
    "Y": "DRAW",
    "Z": "WIN",
}

result_against_opponent_shape = {
    "ROCK": {
        "ROCK": "DRAW",
        "PAPER": "WIN",
        "SCISSORS": "LOSE",
    },
    "PAPER": {
        "ROCK": "LOSE",
        "PAPER": "DRAW",
        "SCISSORS": "WIN",
    },
    "SCISSORS": {
        "ROCK": "WIN",
        "PAPER": "LOSE",
        "SCISSORS": "DRAW",
    },
}

move_by_desired_result = {
    "LOSE": {
        "ROCK": "SCISSORS",
        "PAPER": "ROCK",
        "SCISSORS": "PAPER",
    },
    "DRAW": {
        "ROCK": "ROCK",
        "PAPER": "PAPER",
        "SCISSORS": "SCISSORS",
    },
    "WIN": {
        "ROCK": "PAPER",
        "PAPER": "SCISSORS",
        "SCISSORS": "ROCK",
    },
}


def get_round_score(opponent_shape, shape):
    result = result_against_opponent_shape[opponent_shape][shape]
    return score_by_result[result] + score_by_shape[shape]


def part1(input):
    final_score = 0
    for encounter in input.split("\n"):
        opponent_shape_letter, shape_letter = encounter.split()

        opponent_shape = letter_to_shape[opponent_shape_letter]
        shape = letter_to_shape[shape_letter]

        final_score += get_round_score(opponent_shape, shape)
    return final_score


def part2(input):
    final_score = 0
    for encounter in input.split("\n"):
        opponent_shape_letter, desired_result_letter = encounter.split()

        desired_result = letter_to_desired_result[desired_result_letter]
        opponent_shape = letter_to_shape[opponent_shape_letter]
        desired_shape = move_by_desired_result[desired_result][opponent_shape]

        final_score += get_round_score(opponent_shape, desired_shape)
    return final_score


with open("input.txt", "r") as f:
    input = f.read().rstrip()

print(f"Part 1: {part1(input)}")
print(f"Part 2: {part2(input)}")
