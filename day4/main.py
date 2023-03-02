def get_sections(input):
    sections = []
    for line in input.split():
        sections.append(
            [
                [int(limit) for limit in section.split("-")]
                for section in line.split(",")
            ]
        )
    return sections


def part1(input):
    sections = get_sections(input)
    included_sections_sum = 0
    for section in sections:
        min1, max1 = section[0]
        min2, max2 = section[1]
        included_sections_sum += (
            (min1 <= min2) and (max2 <= max1) or (min2 <= min1) and (max1 <= max2)
        )
    return included_sections_sum


def part2(input):
    sections = get_sections(input)
    included_sections_sum = 0
    for section in sections:
        min1, max1 = section[0]
        min2, max2 = section[1]
        included_sections_sum += (max1 >= min2) and (min1 <= max2)
    return included_sections_sum


with open("input.txt", "r") as f:
    input = f.read().rstrip()

print(f"Part 1: {part1(input)}")
print(f"Part 2: {part2(input)}")
