NUFFIN = '   '


def read_file():
    file = open("input.txt", "r")
    data = []
    [data.append(l.replace("\n", "")) for l in file]
    return data


def get_midpoint(raw):
    print("===== get midpoint: ")
    for r in range(0, len(raw)):
        if raw[r] == '':
            return r


def convert_stacks_to_queues(grid):
    end = -1
    while grid[-1][end] == ' ':
        end -= 1
    stacks = int(grid[-1][end])
    curr_max_depth = len(grid)
    print(f"stacks -> {stacks}, curr_max_depth -> {curr_max_depth}")

    new_vertical = []
    for row in grid[:-1]:
        row += NUFFIN + NUFFIN
        print(row)
        temp = []
        for grabbed_count in range(0, stacks):
            temp.append(row[grabbed_count*4:(grabbed_count*4)+3])
        new_vertical.append(temp)

    [print(n) for n in new_vertical]
    return stacks, curr_max_depth, new_vertical


def parse_instruction(instruction):
    print(instruction)
    split_instr = instruction.split(" ")
    print(split_instr)


def do_one_instruction(stacks, grid, instruction):
    parse_instruction(instruction)
    split_instr = instruction.split(" ")
    move_count = int(split_instr[1])
    src_stack = int(split_instr[3]) - 1
    dst_stack = int(split_instr[5]) - 1
    print(f"{move_count}, {src_stack}, {dst_stack}")

    for count in range(0, move_count):
        print(f"MOVE {count}")
        ## Get src item
        src_item_depth = 0
        try:
            while grid[src_item_depth][src_stack] == NUFFIN:
                src_item_depth += 1
        except:
            src_item_depth = -1
        print(f"grid[src_item_depth][src_stack] -> {grid[src_item_depth][src_stack]}")

        ## Get landing spot
        dst_item_depth = 0
        print(grid[dst_item_depth][dst_stack])
        if grid[dst_item_depth][dst_stack] == NUFFIN:
            try:
                while grid[dst_item_depth][dst_stack] == NUFFIN:
                    dst_item_depth += 1
                dst_item_depth -= 1
            except:
                dst_item_depth = -1
            print(f"grid[dst_item_depth][dst_stack] -> {grid[dst_item_depth][dst_stack]}")
            grid[dst_item_depth][dst_stack] = grid[src_item_depth][src_stack]
            grid[src_item_depth][src_stack] = NUFFIN
        else:
            print(f"grid[dst_item_depth][dst_stack] -> {grid[dst_item_depth][dst_stack]}, need to add new top row")
            ## Create new blank top row
            new_top_row = []
            [new_top_row.append('   ') for i in range(stacks)]

            ## "move" items
            new_top_row[dst_stack] = grid[src_item_depth][src_stack]
            grid[src_item_depth][src_stack] = NUFFIN

            ## Copy onto new grid
            new_grid = [new_top_row]
            [new_grid.append(row) for row in grid]
            grid = new_grid

    # print("NEW GRID AFTER 1 ITERATTION")
    # print(new_top_row)
    # [print(n) for n in grid]

    return grid


def part1():
    raw = read_file()
    # [print(r) for r in raw]
    midpoint = get_midpoint(raw)
    print(midpoint)
    grid = raw[0:midpoint]
    instructions = raw[midpoint+1:]
    print("===== check midpoint")
    print("---")
    [print(r) for r in grid]
    print("---")
    # [print(r) for r in instructions]
    # print("---")
    print("===== convert_stacks_to_queues")
    stacks, curr_max_depth, parsed_data = convert_stacks_to_queues(grid)
    print("===== do_one_instruction")
    new_grid = parsed_data
    for instr in instructions:
        new_grid = do_one_instruction(stacks, new_grid, instr)
        print("NEW GRID:")
        [print(n) for n in new_grid]
        print("=====\n")

    ## STILL NEED TO PRINT TOP OF EACH STACK AS A SINGLE STRING, BUT HAVE SUBMITTED CORRECT ANSWER


def part2():
    pass


if __name__ == '__main__':
    part1()
    part2()

