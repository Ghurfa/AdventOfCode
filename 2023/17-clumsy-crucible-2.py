import heapq

def main():
    lines = []
    with open("17-input.txt", encoding='UTF-8') as file:
        for line in file:
            lines.append(line.strip())

    queue = [(0, 0, 0, 'r', 0, 'r'), (0, 0, 0, 'd', 0, 'd')]
    visited = set()
    visited.add((0, 0, '', 0))

    while True:
        curr = heapq.heappop(queue)
        score, x, y, direction, step_count, let = curr

        if (x, y) == (9, 4):
            pass
        right_edge = x == len(lines[0]) - 1
        bottom_edge = y == len(lines) - 1
        
        if right_edge and bottom_edge and step_count >= 4:
            print(score)
            break
        
        left_edge = x == 0
        top_edge = y == 0

        neighbors = {   'l': (left_edge, x - 1, y),
                        'r': (right_edge, x + 1, y),
                        'u': (top_edge, x, y - 1),
                        'd': (bottom_edge, x, y + 1) }
        
        for neighbor_let in neighbors:
            if step_count < 4 and neighbor_let != let:
                continue
            if ((neighbor_let == 'l' and let == 'r') or
                (neighbor_let == 'r' and let == 'l') or
                (neighbor_let == 'd' and let == 'u') or
                (neighbor_let == 'u' and let == 'd')):
                continue

            condition, neighbor_x, neighbor_y = neighbors[neighbor_let]
            if condition:
                continue
            
            n_score = score + int(lines[neighbor_y][neighbor_x])

            if direction == neighbor_let:
                if step_count + 1 <= 10 and not((neighbor_x, neighbor_y, neighbor_let, step_count + 1) in visited):
                    heapq.heappush(queue, (n_score, neighbor_x, neighbor_y, neighbor_let, step_count + 1, neighbor_let))
                    visited.add((neighbor_x, neighbor_y, neighbor_let, step_count + 1))
            elif not((neighbor_x, neighbor_y, neighbor_let, 1) in visited):
                heapq.heappush(queue, (n_score, neighbor_x, neighbor_y, neighbor_let, 1, neighbor_let))
                visited.add((neighbor_x, neighbor_y, neighbor_let, 1))
            


if __name__ == "__main__":
    main()
