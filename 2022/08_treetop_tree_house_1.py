def main():
    lines = []
    with open("08input.txt", encoding='UTF-8') as file:
        for line in file:
            lines.append(line[:-1])

    counted = set()

    # Lefts
    for y, line in enumerate(lines):
        max_height = -1
        for x, ch in enumerate(line):
            if int(ch) > max_height:
                max_height = int(ch)
                counted.add((x, y))

    # Rights
    for y, line in enumerate(lines):
        max_height = -1
        for x, ch in reversed(list(enumerate(line))):
            if int(ch) > max_height:
                max_height = int(ch)
                counted.add((x, y))

    # Tops
    for x in range(0, len(lines[0])):
        max_height = -1
        for y, line in enumerate(lines):
            ch = line[x]
            if int(ch) > max_height:
                max_height = int(ch)
                counted.add((x, y))

    # Bottoms
    for x in range(0, len(lines[0])):
        max_height = -1
        for y, line in reversed(list(enumerate(lines))):
            ch = line[x]
            if int(ch) > max_height:
                max_height = int(ch)
                counted.add((x, y))

    print(len(counted))


if __name__ == "__main__":
    main()
