

def read_file():
    file = open("input.txt", "r")
    data = []
    [data.append(l.replace("\n", "")) for l in file]
    return data


def get_scores(uniques):
    total = 0
    for unique in uniques:
        value = ord(unique)
        if (value >= 97) and (value <= 122):
            value = value - 96
        elif (value >= 65) and (value <= 90):
            value = value - 38
        # print(unique, value)
        total += value
    return total


def part1():
    backpacks = read_file()
    uniques = []
    for contents in backpacks:
        # print(contents)
        halfway = (int(len(contents)/2))
        half1 = set(contents[0:halfway])
        half2 = set(contents[halfway:])
        # print(half1, half2)
        # print(half1 - half2)
        # print(half1 - (half1 - half2))
        uniques.append(list(half1 - (half1 - half2))[0])
        # print()

    print(uniques)

    total = get_scores(uniques)

    print(f"\n\nTOTAL -> {total}")


def find_common(contents):
    for ele in contents[0]:
        if (ele in contents[1]) and (ele in contents[2]):
            return ele


def part2():
    backpacks = read_file()
    curr_group = backpacks[0:3]
    print(curr_group)
    uniques = []
    for each_three_backpacks in range(0, len(backpacks), 3):
        curr_group = backpacks[each_three_backpacks:each_three_backpacks+3]
        uniques.append(find_common(curr_group))

    print()
    print(uniques)
    total = get_scores(uniques)
    print(total)



if __name__ == '__main__':
    # part1()
    part2()
