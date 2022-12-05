

def read_file():
    file = open("input.txt", "r")
    data = []
    [data.append(l.replace("\n", "")) for l in file]  ## .replace("-", ",")
    return data


def parse_input(raw):
    data = []
    for row in raw:
        temp = row.split(",")
        # print(temp)
        to_append = [temp[0].split("-"), temp[1].split("-")]
        # print(to_append)
        data.append(to_append)
    # print(f"data[0] -> {data[0]}")
    return data


def check_within(pairA, pairB):
    # 6-6 ->         pairA[0] - pairA[1]
    # 4-6 -> pairB[0] -             pairB[1]

    # 6-6 -> pairA[0] -                pairA[1]
    # 4-6 ->      pairB[0] -    pairB[1]

    # print(f"pairA -> {pairA}, pairB -> {pairB}", end=" === ")
    if (pairA[0] >= pairB[0]) and (pairA[1] <= pairB[1]):
        print(True, end=", ")
        return True
    elif (pairA[0] <= pairB[0]) and (pairA[1] >= pairB[1]):
        print(True, end=", ")
        return True
    else:
        print(False, end=", ")
        return False


def part1():
    raw = read_file()
    data = parse_input(raw)
    withins = 0
    for d in data:
        res = check_within([int(x) for x in d[0]], [int(x) for x in d[1]])
        print(res)
        withins += res
    print(f"withins = {withins}")


def check_overlap_fail(pairA, pairB):
    # 6-6 ->         pairA[0] -      pairA[1]
    # 4-6 -> pairB[0] -        pairB[1]

    # 6-6 -> pairA[0] -        pairA[1]
    # 4-6 ->      pairB[0] -        pairB[1]
    # print(f"pairA -> {pairA}, pairB -> {pairB}", end=" === ")
    if (pairA[0] >= pairB[0]) and (pairA[1] >= pairB[1]):
        print(True, end=", ")
        return True
    elif (pairA[0] <= pairB[0]) and (pairA[1] <= pairB[1]):
        print(True, end=", ")
        return True
    else:
        print(False, end=", ")
        return False


def check_overlap(pairA, pairB):
    # 6-6 -> pairA[0] - pairA[1]
    # 4-6 ->                      pairB[0] - pairB[1]

    # 6-6 ->                       pairA[0] - pairA[1]
    # 4-6 -> pairB[0] -  pairB[1]
    # print(f"pairA -> {pairA}, pairB -> {pairB}", end=" === ")
    if (pairA[0] < pairB[0]) and (pairA[1] < pairB[0]):
        print(False, end=", ")
        return False
    elif (pairB[0] < pairA[0]) and (pairB[1] < pairA[0]):
        print(False, end=", ")
        return False
    else:
        print(True, end=", ")
        return True


def part2():
    raw = read_file()
    data = parse_input(raw)
    overlaps = 0
    for d in data:
        curr_pairs = [[int(x) for x in d[0]], [int(x) for x in d[1]]]
        print(curr_pairs, end=",")
        within_res = check_within(curr_pairs[0], curr_pairs[1])
        if within_res:
            overlaps += 1
        else:
            overlaps += check_overlap(curr_pairs[0], curr_pairs[1])
        print()
        # res = check_overlaps(data)
    print(f"overlaps = {overlaps}")


if __name__ == '__main__':
    # part1()
    part2()
