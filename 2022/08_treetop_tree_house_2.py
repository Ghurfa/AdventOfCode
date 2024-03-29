def main():
    lines = []
    with open("08input.txt", encoding='UTF-8') as file:
        for line in file:
            lines.append(line[:-1])

    best = 0
    for x, _ in enumerate(lines[0]):
        for y, line in enumerate(lines):
            height = int(line[x])

            left = 0
            for left in range(x - 1, -1, -1):
                if int(line[left]) >= height:
                    break
            left_score = x - left

            right = 0
            for right in range(x + 1, len(lines[0])):
                if int(line[right]) >= height:
                    break
            right_score = right - x

            top = 0
            for top in range(y - 1, -1, -1):
                if int(lines[top][x]) >= height:
                    break
            top_score = y - top

            bottom = 0
            for bottom in range(y + 1, len(lines)):
                if int(lines[bottom][x]) >= height:
                    break
            bottom_score = bottom - y

            score = left_score * right_score * top_score * bottom_score
            best = max(best, score)

    print(best)


if __name__ == "__main__":
    main()
