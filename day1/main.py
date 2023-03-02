from heapq import nlargest


def get_calories_by_elf(input):
    return [
        sum([int(calorie) for calorie in list_str.split()])
        for list_str in input.split("\n\n")
    ]


def part1(input):
    return max(get_calories_by_elf(input))


def part2(input):
    return sum(nlargest(3, get_calories_by_elf(input)))


with open("input.txt", "r") as f:
    input = f.read().rstrip()

print(f"Part 1: {part1(input)}")
print(f"Part 2: {part2(input)}")
