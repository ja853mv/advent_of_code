

class Elf:
    holding = list
    total_cals = int

    def __init__(self, items):
        if type(items[0]) == str:
            for i in range(0, len(items)):
                items[i] = int(items[i])
        self.holding = items
        self.total_cals = sum(items)


def read_file():
    file = open("input.txt", "r")
    data = []
    [data.append(l.replace("\n", "")) for l in file]
    print(data)
    return data


def parse_calories(raw):
    elves = []
    curr = []
    for line in raw:
        if line != '':
            curr.append(line)
        else:
            print(curr)
            elves.append(Elf(curr))
            curr = []

    return elves


def get_fattest_elf(elves):
    fattest_elf = [None, 0]
    for elf in elves:
        if elf.total_cals > fattest_elf[1]:
            fattest_elf = [elf, elf.total_cals]

    return fattest_elf[0]


def get_top3_fattest_elves(elves):
    holdings = []
    for elf in elves:
        holdings.append([elf.holding, elf.total_cals])
    sorted_holdings = sorted(holdings, key=lambda x: x[1], reverse=True)

    return sorted_holdings[0:3]


def main():
    raw_data = read_file()
    elves = parse_calories(raw_data)
    print(f"list {elves[0].holding}, total {elves[0].total_cals}")

    greatest_elf = get_fattest_elf(elves)
    print(f"\nelf holding the greating number of calories: \n{greatest_elf.holding} \n === total {greatest_elf.total_cals} calories === ")

    top3 = get_top3_fattest_elves(elves)
    total = 0
    for each in top3:
        print(each[1])
        total += each[1]
    print(total)


if __name__ == '__main__':
    main()
