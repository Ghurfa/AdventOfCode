import re

def main():
    lines = []
    with open("08-input.txt", encoding='UTF-8') as file:
        for line in file:
            lines.append(line.strip())
    
    directions = lines[0]

    maze_lines = lines[2:]
    maze = dict()
    for line in maze_lines:
        parts = line.split(' ')
        maze[parts[0]] = (line[7:10], line[12:15])
    
    steps = 0
    dir_i = 0
    curr = 'AAA'
    while curr != 'ZZZ':
        dir = directions[dir_i]
        dir_val = 1
        if (dir == 'L'):
            dir_val = 0
        curr = maze[curr][dir_val]

        steps += 1
        dir_i += 1
        dir_i %= len(directions)

    # Part 1 solution    
    print(steps)


if __name__ == "__main__":
    main()
