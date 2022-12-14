def main():

    min_x = 0
    max_x = 1000
    max_y = 0
    lines = []
    with open("14input.txt", encoding='UTF-8') as file:
        for line in file:
            parts = line.strip().split(' -> ')
            path = []
            for pair in parts:
                pair_parts = pair.split(',')
                min_x = min(min_x, int(pair_parts[0]))
                max_x = max(max_x, int(pair_parts[0]))
                max_y = max(max_y, int(pair_parts[1]))
                path.append((int(pair_parts[0]), int(pair_parts[1])))
            lines.append(path)
    grid = [[0] * 500 for _ in range(min_x, max_x + 2)]
    
    for path in lines:
        for i, point in enumerate(path[1:], 1):
            prev = path[i - 1]
            curr = prev
            grid[curr[0] - min_x][curr[1]] = 1
            while curr != point:
                if point[0] < curr[0]:
                    curr = (curr[0] - 1, curr[1])
                elif point[0] > curr[0]:
                    curr = (curr[0] + 1, curr[1])
                elif point[1] < curr[1]:
                    curr = (curr[0], curr[1] - 1)
                elif point[1] > curr[1]:
                    curr = (curr[0], curr[1] + 1)
                grid[curr[0] - min_x][curr[1]] = 1

    count = 0
    spawn_pos = (500, 0)
    exit = False
    while not exit:
        grain_pos = spawn_pos
        while True:
            if grain_pos[1] >= max_y + 1:
                grid[grain_pos[0] - min_x][grain_pos[1]] = 1
                break
            elif not grid[grain_pos[0] - min_x][grain_pos[1] + 1]:
                grain_pos = (grain_pos[0], grain_pos[1] + 1)
            elif not grid[grain_pos[0] - min_x - 1][grain_pos[1] + 1]:
                grain_pos = (grain_pos[0] - 1, grain_pos[1] + 1)
            elif not grid[grain_pos[0] - min_x + 1][grain_pos[1] + 1]:
                grain_pos = (grain_pos[0] + 1, grain_pos[1] + 1)
            else:
                grid[grain_pos[0] - min_x][grain_pos[1]] = 1
                if grain_pos == spawn_pos:
                    exit = True
                break
        count += 1
    print(count)

if __name__ == "__main__":
    main()
