ORD_LOWERCASE_OFFSET = ord("a") - 1
ORD_UPPERCASE_OFFSET = ord("A") - 1 - 26


def get_priority(item_type):
    if item_type.islower():
        return ord(item_type) - ORD_LOWERCASE_OFFSET
    return ord(item_type) - ORD_UPPERCASE_OFFSET


def get_priority_sum(item_types):
    return sum(get_priority(item_type) for item_type in item_types)


def get_common_item_types(spaces):
    return set.intersection(*spaces)


def part1(input):
    priority_sum = 0
    for rucksack in input.split():
        compartment_size = int((len(rucksack) / 2))
        compartment1 = set(rucksack[:compartment_size])
        compartment2 = set(rucksack[compartment_size:])
        common_types = compartment1 & compartment2
        priority_sum += get_priority_sum(common_types)
    return priority_sum


def part2(input):
    priority_sum = 0
    current_group = []
    for index, rucksack in enumerate(input.split()):
        current_group.append(set(rucksack))
        if (index + 1) % 3 == 0:
            common_types = get_common_item_types(current_group)
            priority_sum += get_priority_sum(common_types)
            current_group = []
    return priority_sum


with open("input.txt", "r") as f:
    input = f.read().rstrip()

print(f"Part 1: {part1(input)}")
print(f"Part 2: {part2(input)}")
