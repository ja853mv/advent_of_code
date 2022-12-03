

def read_file():
    file = open("input.txt", "r")
    data = []
    [data.append(l.replace("\n", "")) for l in file]
    return data


def parse_input(raw_in):
    out = []
    for each in raw_in:
        out.append(each.split(" "))
    return out


def get_winner(opp, me):
    opp_choice = ["A", "B", "C"]
    me_choice = ["X", "Y", "Z"]
    beat_chain = ["rock", "paper", "scissors"]
    print(opp, me, end=" -> ")
    if opp_choice.index(opp) == me_choice.index(me):
        print("draw")
        return 3 + me_choice.index(me)+1
    elif (opp_choice.index(opp) +1)%3 == me_choice.index(me):
        print("win")
        return 6 + me_choice.index(me)+1
    else:
        print("lose")
        return 0 + me_choice.index(me)+1


def calc_score(strategies):
    total_score = 0
    for strat in strategies:
        total_score += (get_winner(strat[0], strat[1]))
    print(f"\n\ntotal_score -> {total_score}")


def part1():
    raw = read_file()
    print(raw)
    parsed = parse_input(raw)
    print(parsed)
    calc_score(parsed)


def get_move(opp, res):
    opp_choice = ["A", "B", "C"]
    # OPP R P S R P S
    #  ME S R P S R P LOSE

    #  ME P S R P S R  WIN
    #  ME R P S  DRAW

    if res == "X":
        to_play = opp_choice[(opp_choice.index(opp) + 2) % 3]
        print(f"{opp}, lose, play {to_play}, points = {0} + {opp_choice.index(to_play)+1}")
        return 0 + opp_choice.index(to_play) + 1
    elif res == "Y":
        to_play = opp
        print(f"{opp}, draw, play {to_play}, points = {3} + {opp_choice.index(to_play)+1}")
        return 3 + opp_choice.index(to_play) + 1
    elif res == "Z":
        to_play = opp_choice[(opp_choice.index(opp) + 1) % 3]
        print(f"{opp}, win, play {to_play}, points = {6} + {opp_choice.index(to_play)+1}")
        return 6 + opp_choice.index(to_play) + 1


def part2():
    raw = read_file()
    strategies = parse_input(raw)
    total_score = 0
    for strat in strategies:
        total_score += get_move(strat[0], strat[1])

    print(f"\n\nTOTAL -> {total_score}")


if __name__ == '__main__':
    # part1()
    part2()
