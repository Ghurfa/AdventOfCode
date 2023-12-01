def neighbors(pos, bounds):
    (x, y) = pos
    (max_x, max_y) = bounds
    if x > 0:
        yield (x - 1, y)
    if x < max_x - 1:
        yield (x + 1, y)
    if y > 0:
        yield (x, y - 1)
    if y < max_y - 1:
        yield (x, y + 1)

def main():
    grid = []
    start_location = (-1, -1)
    end_location = (-1, -1)

    with open("12input.txt") as file:
        for y, line in enumerate(file):
            stripped = line.strip()
            ln = []
            for x, char in enumerate(stripped):
                ln.append(char)
                if char == 'S':
                    start_location = (x, y)
                elif char == 'E':
                    end_location = (x, y)
            if len(ln) > 0:
                grid.append(ln)

    bounds = (len(grid[0]), len(grid))

    # queue = [(start_location, 0)]
    queue = [(end_location, 0)]
    visited = set()
    answer = -1
    while True:
        (curr, curr_dist) = queue.pop(0)

        if curr in visited:
            continue

        visited.add(curr)
        curr_char = grid[curr[1]][curr[0]]
        curr_height = 0 if curr_char == 'S' else \
                     (25 if curr_char == 'E' else ord(curr_char) - ord('a'))
        for neighbor in neighbors(curr, bounds):
            neighbor_char = grid[neighbor[1]][neighbor[0]]
            neighbor_height = 0 if neighbor_char == 'S' else \
                            (25 if neighbor_char == 'E' else ord(neighbor_char) - ord('a'))
            # if not(neighbor in visited) and (neighbor_height <= curr_height + 1):
            if not(neighbor in visited) and (curr_height <= neighbor_height + 1):
                queue.append((neighbor, curr_dist + 1))
                # if neighbor == end_location:
                if neighbor_char == 'a':
                    answer = curr_dist + 1
                    break
        if answer != -1:
            break

    print(answer)

if __name__ == "__main__":
    main()
