def main():
    counting_cycles = [20 + 40 * n for n in range(0, 6)]
    x = 1
    total = 0
    screen = [[False] * 40 for _ in range(0, 6)]

    screen[0][0] = True
    with open("10input.txt", encoding='UTF-8') as file:
        cycle_num = 1
        for line in file:
            if cycle_num in counting_cycles:
                total += cycle_num * x

            curr_pixel_x = (cycle_num - 1) % 40
            curr_pixel_y = int((cycle_num - 1)/40)
            if x - 1 <= curr_pixel_x <= x + 1:
                screen[curr_pixel_y][curr_pixel_x] = True

            parts = [l.strip() for l in line.split(' ')]
            if parts[0] == 'noop':
                cycle_num = cycle_num + 1
            elif parts[0] == 'addx':
                cycle_num += 1

                if cycle_num in counting_cycles:
                    total += cycle_num * x

                curr_pixel_x = (cycle_num - 1) % 40
                curr_pixel_y = int((cycle_num - 1)/40)
                if x - 1 <= curr_pixel_x <= x + 1:
                    screen[curr_pixel_y][curr_pixel_x] = True

                cycle_num += 1
                x += int(parts[1])
            else:
                raise Exception()

    for line in screen:
        for pixel in line:
            if pixel:
                print('#', end='')
            else:
                print(' ', end='')
        print()
    print(total)

if __name__ == "__main__":
    main()
