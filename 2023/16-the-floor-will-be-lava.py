def energize(energized: list, lines: list, curr):
    heads = [curr]
    while len(heads) > 0:
        x, y, dir_x, dir_y = heads.pop()
        if x < 0 or y < 0 or x >= len(lines[0]) or y >= len(lines) or (dir_x, dir_y) in energized[y][x]:
            continue
        
        energized[y][x][(dir_x, dir_y)] = True
        if lines[y][x] == '|':
            if dir_x != 0:
                heads.append((x, y + 1, 0, 1))
                heads.append((x, y - 1, 0, -1))
            else:
                heads.append((x, y + dir_y, dir_x, dir_y))
        elif lines[y][x] == '-':
            if dir_y != 0:
                heads.append((x + 1, y, 1, 0))
                heads.append((x - 1, y, -1, 0))
            else:
                heads.append((x + dir_x, y, dir_x, dir_y))
        elif lines[y][x] == '/':
            if dir_x == 1:
                heads.append((x, y - 1, 0, -1))
            elif dir_x == -1:
                heads.append((x, y + 1, 0, 1))
            elif dir_y == 1:
                heads.append((x - 1, y, -1, 0))
            elif dir_y == -1:
                heads.append((x + 1, y, 1, 0))
        elif lines[y][x] == '\\':
            if dir_x == 1:
                heads.append((x, y + 1, 0, +1))
            elif dir_x == -1:
                heads.append((x, y - 1, 0, -1))
            elif dir_y == 1:
                heads.append((x + 1, y, 1, 0))
            elif dir_y == -1:
                heads.append((x - 1, y, -1, 0))
        else:
            heads.append((x + dir_x, y + dir_y, dir_x, dir_y))

def main():
    lines = []
    with open("16-input.txt", encoding='UTF-8') as file:
        for line in file:
            lines.append(line.strip())
    
    energized = [[{} for _ in range(0, len(lines[0]))] for _ in range(len(lines))]
    energize(energized, lines, (0, 0, 1, 0))
    part_1_score = sum(sum(1 if len(x) > 0 else 0 for x in line) for line in energized)
    print(part_1_score)

    part_2_score = 0
    for y in range(0, len(lines)):
        energized = [[{} for _ in range(0, len(lines[0]))] for _ in range(len(lines))]
        energize(energized, lines, (0, y, 1, 0))
        score = sum(sum(1 if len(x) > 0 else 0 for x in line) for line in energized)
        best = max(best, score)
    for y in range(0, len(lines)):
        energized = [[{} for _ in range(0, len(lines[0]))] for _ in range(len(lines))]
        energize(energized, lines, (len(lines[0]) - 1, y, -1, 0))
        score = sum(sum(1 if len(x) > 0 else 0 for x in line) for line in energized)
        best = max(best, score)
    for x in range(0, len(lines[0])):
        energized = [[{} for _ in range(0, len(lines[0]))] for _ in range(len(lines))]
        energize(energized, lines, (x, 0, 0, 1))
        score = sum(sum(1 if len(x) > 0 else 0 for x in line) for line in energized)
        best = max(best, score)
    for x in range(0, len(lines[0])):
        energized = [[{} for _ in range(0, len(lines[0]))] for _ in range(len(lines))]
        energize(energized, lines, (len(lines) - 1, 0, 0, -1))
        score = sum(sum(1 if len(x) > 0 else 0 for x in line) for line in energized)
        best = max(best, score)
    print(part_2_score)


    
if __name__ == "__main__":
    main()
