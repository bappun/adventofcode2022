from collections import defaultdict


def nsplit(n, string):
    """Splits a string into chunks, while ignoring the following character after the split."""
    chunks = []
    current_chunk = ""
    for index, character in enumerate(string):
        if (index + 1) % (n + 1) == 0:
            chunks.append(current_chunk)
            current_chunk = ""
            continue
        current_chunk += character
    if current_chunk:
        chunks.append(current_chunk)
    return chunks


def get_stacks(stacks_input):
    stacks = defaultdict(list)
    for stack_line in reversed(stacks_input.split("\n")[:-1]):
        print(stack_line)
        for index, crate in enumerate(nsplit(3, stack_line)):
            if crate.strip():
                stacks[index].append(crate)
    return stacks


def apply_moves(stacks, moves_input):
    for move in moves_input.split("\n"):
        pass
    return stacks


def part1(input):
    stacks_input, moves_input = input.split("\n\n")
    # print(f"{stacks_input=}, {moves_input=}")
    stacks = get_stacks(stacks_input)
    print(stacks_input, stacks)
    stacks = apply_moves(stacks, moves_input)


def part2(input):
    pass


with open("input.txt", "r") as f:
    input = f.read().rstrip()


print(f"Part 1: {part1(input)}")
print(f"Part 2: {part2(input)}")
