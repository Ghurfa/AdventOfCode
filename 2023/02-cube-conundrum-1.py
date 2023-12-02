def main():
    maxes = {
        'red': 12,
        'green': 13,
        'blue': 14
    }
    with open("02-input.txt", encoding='UTF-8') as file:
        total = 0
        i = 1
        for line in file:
            line = line.split(':')[1].strip()
            pulls = [ x.strip() for x in line.split(';')]
            for pull in pulls:
                bad = False
                for single_pull in pull.split(','):
                    single_pull = single_pull.strip()
                    parts = [x.strip() for x in single_pull.split(' ')]
                    if int(parts[0]) > maxes[parts[1]]:
                        bad = True
                        break
                if bad:
                    break
            else:
                total += i
            i += 1

        print(total)

if __name__ == "__main__":
    main()
