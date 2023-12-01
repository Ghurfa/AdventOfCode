def main():
    nums = [n for n in range(0, 10)]
    digit_names = ['zero', 'one', 'two', 'three', 'four', 'five', 'six', 'seven', 'eight', 'nine']
    with open("01-input.txt", encoding='UTF-8') as file:
        total = 0
        for line in file:
            firsts_nums = [(n, line.find(str(n))) for n in nums if line.find(str(n)) >= 0]
            firsts_strs = [(n, line.find(str(digit_name))) for (n, digit_name) in enumerate(digit_names) if line.find(str(digit_name)) >= 0]
            firsts = firsts_nums + firsts_strs
            first = min(firsts, key=lambda x: x[1])
            
            lasts_nums = [(n, line.rfind(str(n))) for n in nums if line.rfind(str(n)) >= 0]
            lasts_strs = [(n, line.rfind(str(digit_name))) for (n, digit_name) in enumerate(digit_names) if line.rfind(str(digit_name)) >= 0]
            lasts = lasts_nums + lasts_strs
            last = max(lasts, key=lambda x: x[1])

            val = first[0] * 10 + last[0]
            total += val
        print(total)

if __name__ == "__main__":
    main()
