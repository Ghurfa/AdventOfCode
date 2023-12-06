def main():
    times = [56, 71, 79, 99]
    dists = [334, 1135, 1350, 2430]

    res = []
    for i, time in enumerate(times):
        ways = 0
        for j in range(0, time):
            if j * (time - j) > dists[i]:
                ways += 1
        res.append(ways)
    answer = res[0] * res[1] * res[2] * res[3]
    
    # Part 1 answer
    print(answer)
    
    
    # Part two:
    # Solve for the two values of x
    # -x^2 - (56717999) * x - (334113513502430) > 0

if __name__ == "__main__":
    main()
