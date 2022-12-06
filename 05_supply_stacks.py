def read_stacks(file, stack_count):
    stacks = [[] for i in range(0, stack_count)]
    while (line := file.readline()) and not line[0].isspace():
        for i in range(0, stack_count):
            ch = line[i * 4 + 1]
            if not ch.isspace():
                stacks[i].insert(0, ch)
    return stacks

def do_move_part_1(amt, from_stack, to_stack):
    for _ in range(0, amt):
        to_stack += from_stack.pop()

def do_move_part_2(amt, from_stack, to_stack):
    move_slice = from_stack[-amt:]
    del from_stack[-amt:]
    to_stack += move_slice

def main():
    stack_count = 9
    with open('05input.txt', encoding='UTF-8') as file:
        stacks = read_stacks(file, stack_count)
        while line := file.readline():
            if not line.strip():
                continue
            parts = line.split(' ')
            amt = int(parts[1])
            from_stack_idx = int(parts[3]) - 1
            to_stack_idx = int(parts[5]) - 1

            do_move_part_2(amt, stacks[from_stack_idx], stacks[to_stack_idx])

    answer = ''
    for i in range(0, stack_count):
        answer += stacks[i][-1]
    print(answer)


if __name__ == "__main__":
    main()
