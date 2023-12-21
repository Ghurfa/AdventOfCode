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
    
    goal_dist = 26501365                        # Change to 64 for part 1
    grid_width = len(grid[0])
    grid_height = len(grid)

    mid = start[0]
    dist_to_edge = start[0] + 1

    even_reachable = count_reachable(grid, (0, 0), 4 * grid_width)
    odd_reachable = count_reachable(grid, (0, 1), 4 * grid_width)

    cardinal_starts = [(0, mid), (mid, grid_height - 1), (grid_width - 1, mid), (mid, 0)]
    far_cardinal_dist = (goal_dist - dist_to_edge)
    far_cardinal_scores = [count_reachable(grid, cardinal_starts[i], far_cardinal_dist % grid_width) for i in range(0, 4)]

    center_reachable = even_reachable if (goal_dist % 2 == 0) else odd_reachable

    far_remaining_dist = far_cardinal_dist % grid_width
    far_meta_dist = (goal_dist - far_remaining_dist - dist_to_edge) // grid_width

    if far_meta_dist < 0:
        score = count_reachable(grid, start, goal_dist)
    else:            
        cardinal_reachables = sum(far_cardinal_scores)
        if far_meta_dist > 0:
            almost_far_scores = [count_reachable(grid, cardinal_starts[i], (far_cardinal_dist % grid_width) + grid_width) for i in range(0, 4)]
            cardinal_reachables += sum(almost_far_scores)

            sc_type_2_parity_count = (far_meta_dist - 1) // 2
            sc_type_1_parity_count = (far_meta_dist - 1) - sc_type_2_parity_count

            cardinal_reachables += 4 * (sc_type_1_parity_count * odd_reachable + sc_type_2_parity_count * even_reachable)

        corners = [(0, grid_height - 1), (grid_width - 1, grid_height - 1), (grid_width - 1, 0), (0, 0)]
        quadrants_score = 0
        
        y_meta = 0
        x_meta = far_meta_dist + 2
        done = False
        while True:
            while 2 * dist_to_edge + (y_meta + x_meta) * grid_width > goal_dist:
                x_meta -= 1
                if x_meta < 0:
                    done = True
                    break
            if done:
                break

            remaining_dist = goal_dist - 2 * dist_to_edge - (y_meta + x_meta) * grid_width

            peripheral_scores = [count_reachable(grid, corner, remaining_dist) for corner in corners]
            line_score = sum(peripheral_scores)

            inner_meta_count = x_meta
            if x_meta > 0:
                almost_peripheral_scores = [count_reachable(grid, corner, remaining_dist + grid_width) for corner in corners]
                line_score += sum(almost_peripheral_scores)
                inner_meta_count = x_meta - 1
            
            type_2_parity_count = inner_meta_count // 2
            type_1_parity_count = inner_meta_count - type_2_parity_count
            if y_meta % 2 == 0:
                line_score += 4 * (type_1_parity_count * odd_reachable + type_2_parity_count * even_reachable)
            else:
                line_score += 4 * (type_1_parity_count * even_reachable + type_2_parity_count * odd_reachable)
            
            quadrants_score += line_score
            y_meta += 1
            x_meta += 2

        score = center_reachable + cardinal_reachables + quadrants_score
    print(score)

if __name__ == "__main__":
    main()
