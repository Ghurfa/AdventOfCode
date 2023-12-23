def main():
    grid = []
    with open("23-input.txt", encoding='UTF-8') as file:
        for line in file:
            grid.append(line.strip())

    queue = [(1, 0, 0, set())]
    
    bests = [[0] * len(grid[0]) for _ in grid]
    while len(queue) > 0:
        x, y, dist, visited = queue.pop(0)
        if x < 0 or y < 0 or x >= len(grid[0]) or y >= len(grid) or grid[y][x] == '#' or (x, y) in visited:
            continue
        
        visited.add((x, y))
        bests[y][x] = max(bests[y][x], dist)

        tile = grid[y][x]
        if tile == '^' or tile == '.':
            queue.append((x, y - 1, dist + 1, set(visited)))
        if tile == '<' or tile == '.':
            queue.append((x - 1, y, dist + 1, set(visited)))
        if tile == '>' or tile == '.':
            queue.append((x + 1, y, dist + 1, set(visited)))
        if tile == 'v' or tile == '.':
            queue.append((x, y + 1, dist + 1, set(visited)))

    end_score = bests[-1][-2]
    print(end_score)

if __name__ == "__main__":
    main()
