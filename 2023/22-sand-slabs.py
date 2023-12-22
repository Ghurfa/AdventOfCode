import copy

def get_blocks(brick):
    start, end = brick
    
    yield start

    sames = [start[i] == end[i] for i in range(0, 3)]
    if not(all(sames)):
        curr = list(start)
        dim_of_block = sames.index(False)
        delta = 1 if start[dim_of_block] < end[dim_of_block] else -1
        while curr[dim_of_block] != end[dim_of_block]:
            curr[dim_of_block] += delta
            yield curr

def simulate(top_grid, bricks, ignore_brick=None):
    supports = []
    for i, brick in enumerate(bricks):
        if i == ignore_brick:
            supports.append([])
            continue
        curr_supports = []
        for block in get_blocks(brick):
            x, y, z = block
            column = top_grid[y][x]
            
            idx_in_col = column.index((z, i))
            if idx_in_col > 0:
                block_below = column[idx_in_col - 1]
                block_below_z, block_below_id = block_below
                if block_below_id != i and block_below_id != ignore_brick:
                    curr_supports.append(block_below)
        
        supports.append(curr_supports)

    dropped = [False for brick in bricks]

    if ignore_brick != None:
        dropped[ignore_brick] = True

    stack = []
    while False in dropped:
        if len(stack) == 0:
            stack.append(dropped.index(False))
        
        curr = stack[-1]
        curr_supports = supports[curr]
        for z, support in curr_supports:
            if not(dropped[support]):
                stack.append(support)
                break
        else:
            drop_amount = -1
            for block in get_blocks(bricks[curr]):
                x, y, z = block
                if drop_amount == -1:
                    drop_amount = z
                column = top_grid[y][x]
                
                idx_in_col = column.index((z, curr))
                if idx_in_col > 0:
                    block_below = column[idx_in_col - 1]
                    block_below_z, block_below_id = block_below
                    if block_below_id != curr:
                        dist_to_below = z - block_below_z
                        drop_amount = min(drop_amount, dist_to_below - 1)
            
            for block in get_blocks(bricks[curr]):
                x, y, z = block
                top_grid[y][x].remove((z, curr))
                top_grid[y][x].append((z - drop_amount, curr))
                top_grid[y][x].sort()
            start, end = bricks[curr]
            start[2] -= drop_amount
            end[2] -= drop_amount
            stack.pop(-1)
            dropped[curr] = True

def grid_equals(grid_1, grid_2):
    for y in range(0, 10):
        for x in range(0, 10):
            col_1 = grid_1[y][x]
            col_2 = grid_2[y][x]
            if col_1 != col_2:
                return False
    return True

def count_diff_bricks(bricks_1, bricks_2):
    score = 0
    for i, brick in enumerate(bricks_1):
        if brick != bricks_2[i]:
            score += 1
    return score

def main():
    bricks = []
    with open("22-input.txt", encoding='UTF-8') as file:
        for line in file:
            line = line.strip()
            endpoint_strs = line.split('~')
            endpoints = [[int(y) for y in x.split(',')] for x in endpoint_strs]
            bricks.append(endpoints)

    top_grid = [[[] for _ in range(0, 10)] for _ in range(0, 10)]

    for i, brick in enumerate(bricks):
        start, end = brick
        sames = [start[i] == end[i] for i in range(0, 3)]
        start_x, start_y, start_z = start
        
        # Add start
        top_grid[start_y][start_x].append((start_z, i))

        # Add rest
        if not(all(sames)):
            curr = list(start)
            dim_of_block = sames.index(False)
            delta = 1 if start[dim_of_block] < end[dim_of_block] else -1
            while curr[dim_of_block] != end[dim_of_block]:
                curr[dim_of_block] += delta
                top_grid[curr[1]][curr[0]].append((curr[2], i))
    
    for y in range(0, 10):
        for x in range(0, 10):
            top_grid[y][x].sort()


    # Simulate dropping
    simulate(top_grid, bricks)

    # Failed solution 1: Determine the "dependency" of each brick & count the bricks that are not depended on by another brick

    dependencies = [None for brick in bricks]
    for i, brick in enumerate(bricks):
        curr_supports = []
        for block in get_blocks(brick):
            x, y, z = block
            column = top_grid[y][x]
            
            idx_in_col = column.index((z, i))
            if idx_in_col > 0:
                block_below = column[idx_in_col - 1]
                block_below_z, block_below_id = block_below
                if block_below_id != i:
                    curr_supports.append(block_below)
        
        if len(curr_supports) == 1:
            dependencies[i] = curr_supports[0][1]
        elif len(curr_supports) > 1:
            curr_supports.sort()
            highest = curr_supports[-1]
            second_highest = curr_supports[-2]
            if highest[0] != second_highest[0]:
                dependencies[i] = highest[1]
    
    removable_bricks = [i for i in range(0, len(bricks)) if not(i in dependencies)]
    print(len(removable_bricks))

    # Solution 2: Remove brick & simulate bricks dropping to see if the grid has changed

    removable_bricks_2 = []
    fallen_bricks_counts = []
    for i, brick in enumerate(bricks):
        grid_copy = copy.deepcopy(top_grid)
        bricks_copy = copy.deepcopy(bricks)
        for block in get_blocks(brick):
            x, y, z = block
            col = grid_copy[y][x]
            col.remove((z, i))
        grid_copy_2 = copy.deepcopy(grid_copy)
        simulate(grid_copy, bricks_copy, i)
        if grid_equals(grid_copy, grid_copy_2):
            removable_bricks_2.append(i)
        fallen_bricks_counts.append(count_diff_bricks(bricks, bricks_copy))
        
    print(len(removable_bricks_2))
    print(sum(fallen_bricks_counts))


if __name__ == "__main__":
    main()
