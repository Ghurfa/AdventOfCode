def main():
    winning_num = []
    your_num = []
    with open("04-input.txt", encoding='UTF-8') as file:
        for line in file:
            line = line.strip()
            parts = line.split(':')
            num_parts = parts[1].split('|')
            winning_num_str = num_parts[0].split(' ')
            your_num_str = num_parts[1].split(' ')
            winning_num.append([int(x) for x in winning_num_str if x != ''])
            your_num.append([int(x) for x in your_num_str if x != ''])
    
    total = 0
    for x, win_num in enumerate(winning_num):
        score = 0
        for num in your_num[x]:
            if num in win_num:
                if score == 0:
                    score = 1
                else:
                    score *= 2
        total += score
    print(total)

if __name__ == "__main__":
    main()
