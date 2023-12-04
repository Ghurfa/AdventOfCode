def main():
    winning_num = []
    your_num = []
    with open("test-input.txt", encoding='UTF-8') as file:
        for line in file:
            line = line.strip()
            parts = line.split(':')
            num_parts = parts[1].split('|')
            winning_num_str = num_parts[0].split(' ')
            your_num_str = num_parts[1].split(' ')
            winning_num.append([int(x) for x in winning_num_str if x != ''])
            your_num.append([int(x) for x in your_num_str if x != ''])
    
    cards = [1 for x in range(0, len(winning_num))]
    for x, win_num in enumerate(winning_num):
        match_count = 0
        for num in your_num[x]:
            if num in win_num:
                match_count += 1
        for i in range(0, match_count):
            cards[x + i + 1] += cards[x]
    print(sum(cards))

if __name__ == "__main__":
    main()
