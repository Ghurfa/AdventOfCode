def main():
    lines = []
    with open("08input.txt", encoding='UTF-8') as file:
        for line in file:
            lines.append(line[:-1])

    counted = set()
    # Lefts
    left_tree_count = 0
    for i, line in enumerate(lines):
        max_height = -1
        for j, ch in enumerate(line):
            if int(ch) > max_height:
                max_height = int(ch)
                left_tree_count += 1
                counted.add((j, i))
                
    # Rights
    right_tree_count = 0
    for i, line in enumerate(lines):
        max_height = -1
        for j, ch in enumerate(line[::-1]):
            if int(ch) > max_height:
                max_height = int(ch)
                right_tree_count += 1
                counted.add((len(line) - j - 1, i))
    
    # Tops
    top_tree_count = 0
    for x in range(0, len(lines[0])):
        max_height = -1
        for y, line in enumerate(lines):
            ch = line[x]
            if int(ch) > max_height:
                max_height = int(ch)
                top_tree_count += 1
                counted.add((x, y))
    # Bottoms
    bottom_tree_count = 0
    for x in range(0, len(lines[0])):
        max_height = -1
        for y, line in reversed(list(enumerate(lines))):
            ch = line[x]
            if int(ch) > max_height:
                max_height = int(ch)
                bottom_tree_count += 1
                counted.add((x, y))
                

    print(len(counted))
        

if __name__ == "__main__":
    main()
