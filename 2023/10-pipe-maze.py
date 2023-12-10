def main():
    lines = []
    with open("10-input.txt", encoding='UTF-8') as file:
        for line in file:
            lines.append(line.strip())
    
    connections = []
    start = (0, 0)
    for y, line in enumerate(lines):
        cxn_line = []
        for x, char in enumerate(line):
            if char == '|':
                cxn_line.append('ud')
            elif char == '-':
                cxn_line.append('lr')
            elif char == 'L':
                cxn_line.append('ur')
            elif char == 'J':
                cxn_line.append('lu')
            elif char == '7':
                cxn_line.append('ld')
            elif char == 'F':
                cxn_line.append('dr')
            elif char == 'S':
                start = (x, y)
                cxn_line.append('lu') # For 10-input
            else:
                cxn_line.append('')
        connections.append(cxn_line)

    distances = { start: 0}
    
    queue = [start]
    visited = [start]
    while len(queue) > 0:
        curr = queue.pop(0)
        curr_x, curr_y = curr
        curr_cxn = connections[curr_y][curr_x]
        if curr_x > 0:
            left_pos = (curr_x - 1, curr_y)
            left_cxn = connections[curr_y][curr_x - 1]
            if ('l' in curr_cxn) and ('r' in left_cxn) and not (left_pos in visited):
                queue.append(left_pos)
                visited.append(left_pos)
                distances[left_pos] = distances[curr] + 1
        if curr_x < (len(connections[0]) - 1):
            right_pos = (curr_x + 1, curr_y)
            right_cxn = connections[curr_y][curr_x + 1]
            if ('r' in curr_cxn) and ('l' in right_cxn) and not (right_pos in visited):
                queue.append(right_pos)
                visited.append(right_pos)
                distances[right_pos] = distances[curr] + 1
        if curr_y > 0:
            up_pos = (curr_x, curr_y - 1)
            up_cxn = connections[curr_y - 1][curr_x]
            if ('u' in curr_cxn) and ('d' in up_cxn) and not (up_pos in visited):
                queue.append(up_pos)
                visited.append(up_pos)
                distances[up_pos] = distances[curr] + 1
        if curr_y < (len(connections) - 1):
            down_pos = (curr_x, curr_y + 1)
            down_cxn = connections[curr_y + 1][curr_x]
            if ('d' in curr_cxn) and ('u' in down_cxn) and not (down_pos in visited):
                queue.append(down_pos)
                visited.append(down_pos)
                distances[down_pos] = distances[curr] + 1
    
    
    # Part 1 answer

    # dist_vals = [distances[x] for x in distances]
    # print(max(dist_vals))

    
    inside_count = 0
    for y, line in enumerate(lines):
        pipe_count = 0
        x = 0
        while x < len(line):
            ch = line[x]
            curr = (x, y)
            if curr in visited:
                if ch == '|':
                    pipe_count += 1
                    x += 1
                elif ch == 'L':
                    while (x, y) in visited:
                        x += 1
                        if line[x - 1] == '7':
                            pipe_count += 1
                            break
                        elif line[x - 1] in 'SJ':
                            break
                elif ch == 'F':
                    while (x, y) in visited:
                        x += 1
                        if line[x - 1] in 'SJ':
                            pipe_count += 1
                            break
                        elif line[x - 1] == '7':
                            break
            elif (pipe_count % 2) == 1:
                inside_count += 1
                x += 1
            else:
                x += 1
    
    # Part 2 answer
    print(inside_count)

if __name__ == "__main__":
    main()
