def main():
    lines = []
    with open("09-input.txt", encoding='UTF-8') as file:
        for line in file:
            lines.append(line.strip())
    
    total = 0
    for line in lines:
        seq = [int(x) for x in line.split(' ') if x != '']
        sex = [seq]

        while True:
            peek = sex[-1]
            deriv = [peek[i + 1] - peek[i] for i in range(0, len(peek) - 1)]
            if all(x == 0 for x in deriv):
                break
            else:
                sex.append(deriv)
        
        accum = 0
        sex.reverse()
        for deriv in sex:
            # Part 1 version
            # accum = deriv[-1] + accum

            # Part 2 version
            accum = deriv[0] - accum
        total += accum
    print(total)
    

if __name__ == "__main__":
    main()
