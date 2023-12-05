def main():
    lines = []
    with open("05-input.txt", encoding='UTF-8') as file:
        for line in file:
            lines.append(line.strip())

    seed_line = lines[0]
    seeds = [int(x) for x in seed_line.split(':')[1].split(' ') if x != '']

    mappings = [[]]
    line_num = 3
    while line_num < len(lines):
        new_mapping_line = lines[line_num]
        if new_mapping_line == '':
            line_num += 2
            mappings.append([])
        else:
            mappings[-1].append([int(x) for x in new_mapping_line.split(' ') if x != ''])
            line_num += 1
    # mappings.pop(-1)

    result = []
    for seed in seeds:
        val = seed
        for mapping in mappings:
            for entry in mapping:
                dest, src, length = entry
                if (src <= val) and (src + length > val):
                    val = dest + (val - src)
                    break
        result.append(val)
    print(min(result))

if __name__ == "__main__":
    main()
