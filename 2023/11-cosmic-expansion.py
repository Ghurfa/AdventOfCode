def main():
    lines = []
    with open("11-input.txt", encoding='UTF-8') as file:
        for line in file:
            lines.append(line.strip())

    empty_rows = []
    for y, line in enumerate(lines):
        if all(x == '.' for x in line):
            empty_rows.append(y)
    
    empty_cols = []
    for x in range(0, len(lines[0])):
        if all(line[x] == '.' for line in lines):
            empty_cols.append(x)
    
    expansion_factor = 1000000  # Change this to 2 for part 1
    galaxies = []
    for y, line in enumerate(lines):
        for x, ch in enumerate(line):
            if ch == '#':
                real_x = x + sum(((expansion_factor - 1) if ec < x else 0) for ec in empty_cols)
                real_y = y + sum(((expansion_factor - 1) if er < y else 0) for er in empty_rows)
                galaxies.append((real_x, real_y))

    total = 0
    for i, gal_a in enumerate(galaxies):
        a_x, a_y = gal_a
        for gal_b in galaxies[i + 1:]:
            b_x, b_y = gal_b
            dist = abs(b_x - a_x) + abs(b_y - a_y)
            total += dist
    print(total)

if __name__ == "__main__":
    main()
