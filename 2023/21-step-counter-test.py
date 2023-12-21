# Test program used to check the results of the main solution
# Works by literally duplicating the grid and running the normal part 1 solution on it

memo = {}

def count_reachable(grid, start, goal_dist):
    if goal_dist < 0:
        return 0

    if (start, goal_dist) in memo:
        return memo[(start, goal_dist)]
    even_visited = set()
    odd_visited = set()
    queue = [(start, 0)]
    while len(queue) > 0:
        node, dist = queue.pop(0)
        if dist > goal_dist:
            continue
        if node in even_visited or node in odd_visited:
            continue
        x, y = node
        if x < 0 or x >= len(grid[0]) or y < 0 or y >= len(grid):
            continue
        if grid[y][x] == '#':
            continue
        if dist % 2 == 0:
            even_visited.add(node)
        else:
            odd_visited.add(node)
        
        queue.append(((x - 1, y), dist + 1))
        queue.append(((x + 1, y), dist + 1))
        queue.append(((x, y - 1), dist + 1))
        queue.append(((x, y + 1), dist + 1))

    answer = len(even_visited) if (goal_dist % 2 == 0) else len(odd_visited)

    meta_counts = [[0] * 15 for _ in range(0, 15)]
    for node in odd_visited:
        x, y = node
        meta_x = (x - (x % 131)) // 131
        meta_y = (y - (y % 131)) // 131
        meta_counts[meta_y][meta_x] += 1
    
    for arr in meta_counts:
        print(','.join(str(x).zfill(4) for x in arr))
    memo[(start, goal_dist)] = answer
    return answer

def main():
    grid = []
    start = (-1, -1)
    with open("21-input.txt", encoding='UTF-8') as file:
        for y, line in enumerate(file):
            grid.append(line.strip())
            for x, ch in enumerate(line):
                if ch == 'S':
                    start = (x, y)
    
    n = 15
    mega_grid = [line * n for line in grid]
    mega_grid *= n

    goal_dist = 589
    actual_mid = start[0] + (n // 2) * len(grid)
    score = count_reachable(mega_grid, (actual_mid, actual_mid), goal_dist)
    print(score)

if __name__ == "__main__":
    main()
