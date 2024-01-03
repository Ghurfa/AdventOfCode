def collide(stone_1, stone_2, min_xy, max_xy):
    pos_1, vel_1 = stone_1
    pos_2, vel_2 = stone_2

    x1, y1, _ = pos_1
    x2, y2, _ = pos_2
    vx1, vy1, _ = vel_1
    vx2, vy2, _ = vel_2

    # Algebra to justify 

    # (y - y1) = (vy1/vx1)(x - x1)
    # (y - y2) = (vy2/vx2)(x - x2)

    # y = (vy1/vx1)(x - x1) + y1
    # y = (vy2/vx2)(x - x2) + y2

    # (vy1/vx1)(x - x1) + y1 = (vy2/vx2)(x - x2) + y2
    # (vy1/vx1)x - (vy1/vx1) * x1 + y1 = (vy2/vx2)x - (vy2/vx2) * x2 + y2
    # (vy1/vx1)x - (vy2/vx2)x =  (vy1/vx1) * x1 -(vy2/vx2) * x2 + y2 - y1
    # x = ((vy1/vx1) * x1 -(vy2/vx2) * x2 + y2 - y1) / ((vy1/vx1) - (vy2/vx2))
    # x = (vy1 * vx2 * x1 - vy2 * vx1 * x2 + (y2 - y1) * vx1 * vx2) / (vy1 * vx2  - vy2 * vx1)

    x_num = (vy1 * vx2 * x1 - vy2 * vx1 * x2 + (y2 - y1) * vx1 * vx2)
    x_denom = (vy1 * vx2  - vy2 * vx1)
    if x_denom == 0:
        return False
    x = x_num / x_denom
    y = (vy1/vx1) * (x - x1) + y1
    
    correct_dir_1 = (x - x1) / vx1 > 0
    correct_dir_2 = (x - x2) / vx2 > 0

    return x >= min_xy and x <= max_xy and y >= min_xy and y <= max_xy and correct_dir_1 and correct_dir_2
    

def part_2_stuff(stone_1, stone_2):
    pos_1, vel_1 = stone_1
    pos_2, vel_2 = stone_2

    x1, y1, z1 = pos_1
    x2, y2, z2 = pos_2
    vx1, vy1, vz1 = vel_1
    vx2, vy2, vz2 = vel_2


    # Part 2 solution:
    
    # Step 1: Identify two hailstones with parallel trajectories in the XY plane & note their relative starting X- and Y- positions
    # Breakpointing at the below if-statement lets us identify two stones with the trajectory (27, -11) and difference in positions (dx, dy)
    # Since stone 2 is a fixed position relative to stone 1, we know that the velocity of the colliding rock must be a multiple of (dx, dy)
    # Reducing dy/dx to 213/174 lets us guess that the velocity of the rock relative to the parallel stones is (174, 213). The actual
    # xy-velocity is (174 + 27, 213 - 11) = (201, 202)
    
    if vx1 == vx2 and vy1 == vy2:
        dx = x1 - x2
        dy = y1 - y2
        return

    vxr = 174 + 27
    vyr = 213 - 11

    # Step 2: Take any two hailstones with non-parallel trajectories. Let t1 be the time at which the colliding rock collides with hailstone 1,
    # and let t2 be the time at which the rock collides with hailstone 2. We come up with the system of equations below, which reduces through
    # some algebra to the linear equations [a * t1 + b * t2 = c] and [d * t1 + e * t2 = f] where a through f are calculated in the variables below
    
    # (x1 + vx1 * t1) + vxr * (t2 - t1) = x2 + vx2 * t2
    # (y1 + vy1 * t1) + vyr * (t2 - t1) = y2 + vy2 * t2

    a = vx1 - vxr
    b = vxr - vx2
    c = x2 - x1
    d = vy1 - vyr
    e = vyr - vy2
    f = y2 - y1

    # Plugging the numbers above into a matrix calculator and finding the row-reduced echelon form results in values for t1 and t2

    t1 = 711444906273
    t2 = 943556327678

    # Step 3: We now know the positions of collisions 1 and 2 and the time between them, so we can find the missing z-component of the velocity of
    # the colliding rock

    z1_at_ix = z1 + t1 * vz1
    z2_at_ix = z2 + t2 * vz2
    dz = z2_at_ix - z1_at_ix
    dt = t2 - t1
    vzr = dz/dt

    # Step 4: Using the position of the colliding rock at time t1 and the rock's velocity, we calculate the rock's position at t=0 & sum the
    # components of the positions to get the part 2 answer

    x1_at_ix = x1 + t1 * vx1
    y1_at_ix = y1 + t1 * vy1
    z1_at_ix = z1 + t1 * vz1
    x0 = x1_at_ix - vxr * t1
    y0 = y1_at_ix - vyr * t1
    z0 = z1_at_ix - vzr * t1
    print(x0 + y0 + z0)


def main():
    stones = []
    with open("24-input.txt", encoding='UTF-8') as file:
        for line in file:
            pos_str, vel_str = line.strip().split('@')
            pos_str = pos_str.strip()
            vel_str = vel_str.strip()
            pos = [int(x.strip()) for x in pos_str.split(',')]
            vel = [int(x.strip()) for x in vel_str.split(',')]
            stones.append((pos, vel))
    
    score = 0
    for i, stone_1 in enumerate(stones):
        for stone_2 in stones[i + 1:]:
            if collide(stone_1, stone_2, 200000000000000, 400000000000000):
                score += 1
    print(score)

if __name__ == "__main__":
    main()
