def skip(word: str) -> str:
    first_unknown = word.find('?')
    first_hash = word.find('#')
    if first_unknown == -1 and first_hash == -1:
        return ''
    elif first_unknown == -1:
        return word[first_hash:]
    elif first_hash == -1:
        return word[first_unknown:]
    else:
        return word[min(first_unknown, first_hash):]

def solve_if_hash(word: str, groups: list) -> int:
    first_gr = groups[0]
    if all(x in '#?' for x in word[:first_gr]):
        if len(word) == first_gr:
            return 1 if len(groups) == 1 else 0
        elif word[first_gr] in '.?':
            return solve_with_memo(word[first_gr + 1:], groups[1:])
        else:
            return 0
    else:
        return 0

memo = {}
def solve_with_memo(word: str, groups: list) -> int:
    if (word, str(groups)) in memo:
        return memo[(word, str(groups))]
    val = solve_prob(word, groups)
    memo[(word, str(groups))] = val
    return val

def solve_prob(word: str, groups: list) -> int:
    if len(groups) == 0:
        return 0 if '#' in word else 1
    
    first_gr = groups[0]
    word = skip(word)
    if len(word) < first_gr:
        return 0
    
    if word[0] == '#':
        return solve_if_hash(word, groups)
    else:  # question mark
        if_hash = solve_if_hash(word, groups)
        if_dot = solve_with_memo(word[1:], groups)
        return if_hash + if_dot


def main():
    lines = []
    with open("12-input.txt", encoding='UTF-8') as file:
        for line in file:
            lines.append(line.strip())
    
    problems = [(line.split(' ')[0], [int(x) for x in line.split(' ')[1].split(',')]) for line in lines]
    
    # Part 1
    # solutions = [solve_with_memo(word, groups) for word, groups in problems] 

    # Part 2
    solutions = [solve_with_memo('?'.join([word] * 5), groups * 5) for word, groups in problems]

    print(sum(solutions))
    
if __name__ == "__main__":
    main()
