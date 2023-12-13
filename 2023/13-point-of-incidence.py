from typing import Optional

def test_mirror_part_1(pattern: list, m: int):
    for r in range(0, m + 1):
        if m + 1 + r >= len(pattern):
            continue
        this_line = pattern[m - r]
        other_line = pattern[m + 1 + r]
        if this_line != other_line:
            return False
    return True

def test_mirror_part_2(pattern: list, m: int):
    smudged = False
    for r in range(0, m + 1):
        if m + 1 + r >= len(pattern):
            continue
        this_line = pattern[m - r]
        other_line = pattern[m + 1 + r]
        if this_line != other_line:
            if smudged:
                return False
            for i, ch in enumerate(this_line):
                if ch != other_line[i]:
                    if smudged:
                        return False
                    smudged = True
    return smudged

def solve_horz(pattern: list) -> Optional[int]:
    for m in range(0, len(pattern) - 1):
        if test_mirror_part_2(pattern, m):
            return m
    return None

def solve(pattern: list) -> (str, int):
    horz_sol = solve_horz(pattern)
    if horz_sol != None:
        return ('h', horz_sol)

    transpose = [[pattern[i][x] for i in range(0, len(pattern))] for x in range(0, len(pattern[0]))]
    vert_sol = solve_horz(transpose)
    if vert_sol == None:
        raise 'No solution found'
    return ('v', vert_sol)

def main():
    lines = []
    with open("13-input.txt", encoding='UTF-8') as file:
        for line in file:
            lines.append(line.strip())
    
    patterns = []
    cur_pat = []
    for line in lines:
        if line == '':
            patterns.append(cur_pat)
            cur_pat = []
        else:
            cur_pat.append(line)
    if len(cur_pat) > 0:
        patterns.append(cur_pat)
    
    total = 0
    for pattern in patterns:
        sol_type, score = solve(pattern)
        if sol_type == 'v':
            total += score + 1
        else:
            total += 100 * (score + 1)

    print(total)
    
if __name__ == "__main__":
    main()
