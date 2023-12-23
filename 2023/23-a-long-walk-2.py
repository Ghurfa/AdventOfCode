def get_opposite_dir(dirct):
    if dirct == 'r':
        return 'l'
    elif dirct == 'u':
        return 'd'
    elif dirct == 'l':
        return 'r'
    elif dirct == 'd':
        return 'u'
    
def get_neighbors(coords, in_dirct, grid):
    dirs = 'ruld'
    x, y = coords
    neighbors = [(x + 1, y), (x, y - 1), (x - 1, y), (x, y + 1)]
    ret = []
    for i, dirct in enumerate(dirs):
        if dirct == get_opposite_dir(in_dirct):
            continue
        x, y = neighbors[i]
        if x < 0 or y < 0 or x >= len(grid[0]) or y >= len(grid) or grid[y][x] == '#':
            continue
        ret.append(((x, y), dirct))
    return ret

def get_neighbor(x, y, direct):
    if direct == 'r':
        return (x + 1, y)
    elif direct == 'u':
        return (x, y - 1)
    elif direct == 'l':
        return (x - 1, y)
    elif direct == 'd':
        return (x, y + 1)


def main():
    grid = []
    with open("test-input.txt", encoding='UTF-8') as file:
        for line in file:
            grid.append(line.strip())

    edges = {}
    visited = set()
    visited.add((1, 0))
    queue = [((1, 0), 'd')]
    
    while len(queue) > 0:
        start, start_dir = queue.pop()
        x, y = start

        dist = 1
        curr = get_neighbor(x, y, start_dir)
        dirct = start_dir

        while len(neighbors := get_neighbors(curr, dirct, grid)) == 1:
            curr, dirct = neighbors[0]
            dist += 1
        
        if not(start in edges):
            edges[start] = {start_dir: (curr, dist)}
        else:
            edges[start][start_dir] = (curr, dist)
        if not(curr in edges):
            edges[curr] = {get_opposite_dir(dirct): (start, dist)}
        else:
            edges[curr][get_opposite_dir(dirct)] = (start, dist)
        
        if not(curr in visited):
            visited.add(curr)
        
            for _, neighbor_dirct in neighbors:
                queue.append((curr, neighbor_dirct))

    queue = [(1, 0, 0, set())]
    print(edges)

    bests = [[0] * len(grid[0]) for _ in grid]
    while len(queue) > 0:
        x, y, dist, visited = queue.pop(0)
        if x < 0 or y < 0 or x >= len(grid[0]) or y >= len(grid) or grid[y][x] == '#' or (x, y) in visited:
            continue
        
        visited.add((x, y))
        bests[y][x] = max(bests[y][x], dist)

        for neighbor_letter in edges[(x, y)]:
            coords, edge_len = edges[(x, y)][neighbor_letter]
            queue.append((coords[0], coords[1], dist + edge_len, set(visited)))

    end_score = bests[-1][-2]
    print(end_score)



if __name__ == "__main__":
    main()
