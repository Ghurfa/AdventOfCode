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

    val_ranges = []
    for i in range(0, len(seeds) // 2):
        val_ranges.append((seeds[i * 2], seeds[i * 2 + 1]))
    for mapping in mappings:
        val_ranges_next = []
        while len(val_ranges) > 0:
            val = val_ranges.pop()
            start, val_len = val
            end = start + val_len
            for entry in mapping:
                dest, src, map_len = entry

                # Start in mapping
                if (src <= start) and (src + map_len > start):
                    new_start = dest + (start - src)

                    # End in mapping
                    if (src < end) and (src + map_len >= end):
                        val_ranges_next.append((new_start, val_len))
                        break
                    else:   # End after mapping
                        new_len = src + map_len - start
                        val_ranges_next.append((new_start, new_len))
                        
                        other_start = start + new_len
                        other_len = val_len - new_len
                        val_ranges.append((other_start, other_len))
                        break
                elif (src < end) and (src + map_len >= end):  #end in mapping, start before
                    new_len = end - src
                    new_start = dest
                    val_ranges_next.append((new_start, new_len))

                    other_len = val_len - new_len
                    val_ranges.append((start, other_len))
                    break
                elif (start <= src) and (start + val_len > src):   # Mapping inside val_range
                    seg_0_len = src - start
                    seg_2_len = val_len - seg_0_len - map_len
                    seg_2_start = src + map_len
                    val_ranges.append((start, seg_0_len))
                    val_ranges_next.append((dest, map_len))
                    val_ranges.append((seg_2_start, seg_2_len))
            else:
                val_ranges_next.append((start, val_len))
        val_ranges = val_ranges_next
        val_ranges_next = []
        pass

    result = [a for a, _ in val_ranges]
    print(min(result))

if __name__ == "__main__":
    main()
