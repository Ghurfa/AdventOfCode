def main():
    with open("02-input.txt", encoding='UTF-8') as file:
        total = 0
        i = 1
        for line in file:
            maxes = {
                'red': 0,
                'green': 0,
                'blue': 0
            }
            line = line.split(':')[1].strip()
            pulls = [ x.strip() for x in line.split(';')]
            for pull in pulls:
                for single_pull in pull.split(','):
                    single_pull = single_pull.strip()
                    parts = [x.strip() for x in single_pull.split(' ')]
                    if int(parts[0]) > maxes[parts[1]]:
                        maxes[parts[1]] = int(parts[0])
            
            power = maxes['red'] * maxes['green'] * maxes['blue']
            total += power

        print(total)

if __name__ == "__main__":
    main()
