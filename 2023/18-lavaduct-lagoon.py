def main():

    # Read in data

    data = []
    with open("18-input.txt", encoding='UTF-8') as file:
        for line in file:
            line = line.strip()
            parts = line.split(' ')
            dirs = 'RDLU'
            
            # For part 1
            # data.append((parts[0], int(parts[1])))
    
            # For part 2
            data.append((dirs[int(parts[2][-2])], int(parts[2][2:-2], 16)))
    
    # Create list of the endpoints of each vertical line

    col_ends = {}
    walker = [0, 0]
    prev_dir = 'U'
    for inst in data:
        direct, steps = inst
        x, y = walker
        if not(y in col_ends):
            col_ends[y] = []
        if direct == 'R':
            if prev_dir == 'U':
                col_ends[y].append((x, True))
            else:
                col_ends[y].append((x, False))
            walker[0] += steps
        elif direct == 'L':
            if prev_dir == 'U':
                col_ends[y].append((x, True))
            else:
                col_ends[y].append((x, False))
            walker[0] -= steps
        elif direct == 'U':
            col_ends[y].append((x, False))
            walker[1] -= steps
        elif direct == 'D':
            col_ends[y].append((x, True))
            walker[1] += steps
        prev_dir = direct

    if walker[0] != 0 or walker[1] != 0:
        raise 'Bad data'
    
    # Find the y-levels of all horizontal lines, in order

    y_levels = [y for y in col_ends]
    y_levels.sort()
    for y in y_levels:
        col_ends[y].sort()

    # Loop through the horizontal lines

    prev_y = 0
    score = 0
    cols = []
    for y in y_levels:

        # Determine the 'accumulated width' of the shape in the section between the current and previous y-level by using
        # the list of columns which are relevant at the current y-level

        is_in = False
        prev_x = 0
        accum_width = 0
        for col in cols:
            if is_in:
                accum_width += col - prev_x + 1
            is_in = not(is_in)
            prev_x = col

        # Add the area of the section to the score

        height = y - prev_y
        score += accum_width * height
        prev_y = y

        # Correct for the the fact that the above area calculation does not include the horizontal lines above sections

        event_list = col_ends[y]
        for i in range(0, len(event_list)//2):
            x_1, is_1_top = event_list[i * 2]
            x_2, is_2_top = event_list[i * 2 + 1]
            wall_x = (x_1 + x_2) / 2
            is_wall_in = sum(1 if x < wall_x else 0 for x in cols) % 2 == 1
            if not(is_wall_in):
                score += x_2 - x_1 + (1 if is_1_top else 0) + (1 if is_2_top else 0) - 1
        
        # Update columns list

        for x, is_top in event_list:
            if is_top:
                cols.append(x)
            else:
                cols.remove(x)
        cols.sort()

    print(score)


if __name__ == "__main__":
    main()
