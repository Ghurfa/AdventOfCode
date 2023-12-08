import re

def main():
    lines = []
    with open("08-input.txt", encoding='UTF-8') as file:
        for line in file:
            lines.append(line.strip())
    
    directions = lines[0]
    print(len(directions))

    maze_lines = lines[2:]
    names = []
    maze = dict()
    for i, line in enumerate(maze_lines):
        name = line.split(' ')[0]
        names.append(name)
        parts = line.split(' ')
        maze[parts[0]] = (line[7:10], line[12:15])
    
    steps = 0
    dir_i = 0
    currs = [x for x in names if x[2] == 'A']
    done = False
    while not(done):
        dir = directions[dir_i]
        dir_val = 1
        if (dir == 'L'):
            dir_val = 0

        done = True
        for i, curr in enumerate(currs):
            currs[i] = maze[curr][dir_val]
            if currs[i][2] != 'Z':
                done = False
            else:
                # This is used to find the number of steps for a runner to first reach a 'Z' node
                # as well as the number of steps between each runner found its next 'Z' node. Conveniently,
                # each runner only returned to the same 'Z' node instead of visiting other 'Z' nodes, and
                # the period of repetition was always equal to the initial number of steps. We can plug the
                # periods into a Least Common Multiple calculator to get the answer for part 2
                print((i, steps))

        steps += 1
        dir_i += 1
        dir_i %= len(directions)
    


if __name__ == "__main__":
    main()
