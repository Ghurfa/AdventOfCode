import json

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

def create_graph():
    grid = []
    with open("23-input.txt", encoding='UTF-8') as file:
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

    for x in edges:
        print(f'{x}: {edges[x]}')

def insert_falses(pattern, num_falses, start_at = 0):
    if num_falses <= 0:
        yield pattern
        return
    for i in range(start_at, len(pattern) + 1):
        copy = list(pattern)
        copy.insert(i, False)
        for pat in insert_falses(copy, num_falses - 1, i + 1):
            yield pat

def connect_patterns(prev_pat, next_pat, horz_edges, vert_edges, row):
    if prev_pat[3] and all(next_pat[i] for i in [2, 4, 5]):
        pass
    out_path_num = 1
    out_pat = []
    pat_score = sum(edge for i, edge in enumerate(vert_edges[row]) if next_pat[i])
    prev_next_links = {}
    col = 0
    curr_connection = None
    while col < 6:
        next_connects = next_pat[col]
        prev_connects = prev_pat[col] != 0
        if curr_connection == None:
            if next_connects and prev_connects:
                if prev_pat[col] in prev_next_links:
                    out_pat.append(prev_next_links[prev_pat[col]])
                else:
                    prev_next_links[prev_pat[col]] = out_path_num
                    out_pat.append(prev_next_links[prev_pat[col]])
                    out_path_num += 1
            elif next_connects:
                if col >= 5:
                    raise 'Should be unreachable'
                pat_score += horz_edges[row][col]
                out_pat.append(out_path_num)
                curr_connection = (True, out_path_num)
            elif prev_connects:
                if col >= 5:
                    raise 'Should be unreachable'
                pat_score += horz_edges[row][col]
                out_pat.append(0)
                curr_connection = (False, prev_pat[col])
            else:
                out_pat.append(0)
        else:
            is_other_cxn_next, other_cxn_num = curr_connection
            if next_connects and prev_connects:
                return None
            if next_connects:
                if is_other_cxn_next:
                    if other_cxn_num != out_path_num:
                        raise 'Unreachable'
                    out_pat.append(out_path_num)
                    out_path_num += 1
                else:
                    if other_cxn_num in prev_next_links:
                        out_pat.append(prev_next_links[other_cxn_num])
                    else:
                        prev_next_links[other_cxn_num] = out_path_num
                        out_pat.append(out_path_num)
                        out_path_num += 1
                curr_connection = None
            elif prev_connects:
                out_pat.append(0)
                if is_other_cxn_next:
                    if prev_pat[col] in prev_next_links:
                        out_pat = [(prev_next_links[prev_pat[col]] if x == other_cxn_num else x) for x in out_pat]
                    else:
                        prev_pat[col] = other_cxn_num
                        out_path_num += 1
                else:
                    if prev_pat[col] == other_cxn_num:
                        return None
                    prev_pat = [(other_cxn_num if x == prev_pat[col] else x) for x in prev_pat]
                    
                curr_connection = None
            else:
                out_pat.append(0)
                pat_score += horz_edges[row][col]
        col += 1
    if curr_connection != None or len(out_pat) != 6:
        raise 'Unreachable'
    
    return (out_pat, pat_score)

def solve_grid():
    horz_edges = [[126, 222, 274, 114, 418],
                  [140, 66, 196, 84, 166],
                  [76, 98, 162, 70, 164],
                  [18, 224, 92, 126, 48],
                  [42, 214, 58, 138, 112],
                  [464, 176, 140, 170, 166]]
    vert_edges = [[122, 92, 56, 154, 136, 0],
                  [170, 162, 186, 136, 170, 240],
                  [310, 140, 150, 148, 132, 280],
                  [334, 134, 252, 214, 66, 126],
                  [0, 202, 60, 86, 150, 236],
                  [0, 0, 0, 0, 0, 121]]
    
    patterns = [x for x in insert_falses([True], 5)]
    patterns += [x for x in insert_falses([True] * 3, 3)]
    patterns += [x for x in insert_falses([True] * 5, 1)]

    incoming_patterns = [([1, 0, 0, 0, 0, 0], 137)]

    for row in range(0, 6):
        next_pats = patterns if row < 5 else [[False] * 5 + [True]]

        bests = {}
        for prev_pat, prev_pat_score in incoming_patterns:
            for next_pat in next_pats:
                connection_result = connect_patterns(prev_pat, next_pat, horz_edges, vert_edges, row)
                if connection_result == None:
                    continue
                pattern, score = connection_result
                hashed_pattern = json.dumps(pattern)
                if hashed_pattern in bests:
                    bests[hashed_pattern] = max(bests[hashed_pattern], score + prev_pat_score)
                else:
                    bests[hashed_pattern] = score + prev_pat_score
        
        incoming_patterns = [(json.loads(x), bests[x]) for x in bests]
    print(incoming_patterns)

def main():
    solve_grid()


if __name__ == "__main__":
    main()
