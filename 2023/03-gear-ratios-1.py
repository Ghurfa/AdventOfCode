def main():
    chars = []
    with open("03-input.txt", encoding='UTF-8') as file:
        for line in file:
            chars.append(line.strip())

    symbols = []
    for y, line in enumerate(chars):
        for x, ch in enumerate(line):
            if not(ch.isdigit()) and not(ch == '.'):
                symbols.append((x, y))
    
    part_numbers = []
    for y, line in enumerate(chars):
        num = 0
        num_len = 0
        for x, ch in enumerate(line):
            if ch.isdigit():
                num = 10 * num + int(ch)
                num_len += 1
            else:
                if num_len > 0:
                    part_numbers.append((num, num_len, x, y))
                num = 0
                num_len = 0
        else:
            if num_len > 0:
                part_numbers.append((num, num_len, x + 1, y))
            num = 0
            num_len = 0

    total = 0
    for part in part_numbers:
        by_symbol = False
        num, num_len, part_x, part_y = part
        x_min = part_x - num_len - 1
        x_min = max(x_min, 0)
        x_max = min(part_x + 1, len(chars[0])) # excl
        for x in range(x_min, x_max):
            if (part_y > 0):
                ch = chars[part_y - 1][x]
                if not(ch.isdigit()) and (ch != '.'):
                    by_symbol = True
                    break
            if (part_y < len(chars) - 1):
                ch = chars[part_y + 1][x]
                if not(ch.isdigit()) and (ch != '.'):
                    by_symbol = True
                    break
        
        if (part_x < len(chars[0])):
            ch = chars[part_y][part_x]
            if not(ch.isdigit()) and (ch != '.'):
                by_symbol = True
        
        if part_x - num_len - 1 > 0:
            ch = chars[part_y][part_x - num_len - 1]
            if not(ch.isdigit()) and (ch != '.'):
                by_symbol = True
        
        if by_symbol:
            total += num
    print(total)

if __name__ == "__main__":
    main()
