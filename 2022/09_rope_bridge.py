def new_tail_pos(head_pos, tail_pos):
    (head_x, head_y) = head_pos
    (tail_x, tail_y) = tail_pos
    if head_x == tail_x and head_y > tail_y + 1:
        return (head_x, tail_y + 1)
    elif head_x == tail_x and head_y < tail_y - 1:
        return (head_x, tail_y - 1)
    elif head_y == tail_y and head_x > tail_x + 1:
        return (tail_x + 1, tail_y)
    elif head_y == tail_y and head_x < tail_x - 1:
        return (tail_x - 1, tail_y)
    elif abs(head_y - tail_y) <= 1 and abs(head_x - tail_x) <= 1:
        return tail_pos
    else:
        x_delta = 1 if head_x > tail_x else -1
        y_delta = 1 if head_y > tail_y else -1
        return (tail_x + x_delta, tail_y + y_delta)


def main():
    lines = []
    with open("09input.txt", encoding='UTF-8') as file:
        for line in file:
            lines.append(line[:-1])

    tail_positions = set()

    length = 10
    positions = [(0, 0)] * length
    for line in lines:
        parts = line.split(' ')
        direction = parts[0]
        steps = int(parts[1])
        for i in range(0, steps):
            head = positions[0]
            if direction == 'U':
                positions[0] = (head[0], head[1] + 1)
            elif direction == 'D':
                positions[0] = (head[0], head[1] - 1)
            elif direction == 'L':
                positions[0] = (head[0] - 1, head[1])
            elif direction == 'R':
                positions[0] = (head[0] + 1, head[1])
            for i, _ in enumerate(positions[1:], 1):
                positions[i] = new_tail_pos(positions[i - 1], positions[i])
            tail_positions.add(positions[-1])
    print(len(tail_positions))



if __name__ == "__main__":
    main()
