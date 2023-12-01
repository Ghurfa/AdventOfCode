from functools import cmp_to_key

def int_compare(a, b):
    if a < b:
        return 1
    elif a > b:
        return -1
    else:
        return 0

def compare(a, b):
    if isinstance(a, int) and isinstance(b, int):
        return int_compare(a, b)
    elif isinstance(a, list) and isinstance(b, list):
        smaller_len = min(len(a), len(b))
        for i in range(0, smaller_len):
            comp = compare(a[i], b[i])
            if comp != 0:
                return comp
        return int_compare(len(a), len(b))
    elif isinstance(a, int) and isinstance(b, list):
        return compare([a], b)
    elif isinstance(a, list) and isinstance(b, int):
        return compare(a, [b])
    else:
        raise Exception('Bad types')

def parse(val):
    if val[0] == '[':
        ret = list()
        val = val[1:]
        while val[0] != ']':
            (inner_val, val) = parse(val)
            ret.append(inner_val)
            if val[0] == ',':
                val = val[1:]
        val = val[1:]
        return (ret, val)
    else:
        i = 0
        for i, ch in enumerate(val):
            if not ch.isdigit():
                break
        as_int = int(val[:i])
        return (as_int, val[i:])

def main():
    pair_idx = 1
    answer = 0

    all_items = []

    with open('13input.txt', encoding='UTF-8') as file:
        while first := file.readline():
            second = file.readline()
            _ = file.readline()

            (first_parsed, _) = parse(first.strip())
            (second_parsed, _) = parse(second.strip())

            all_items.append(first_parsed)
            all_items.append(second_parsed)

            good_order = (compare(first_parsed, second_parsed) != -1)

            if good_order:
                answer += pair_idx
            pair_idx += 1

    all_items.append([[2]])
    all_items.append([[6]])

    all_items.sort(key=cmp_to_key(compare), reverse=True)

    divider_2 = all_items.index([[2]]) + 1
    divider_6 = all_items.index([[6]]) + 1

    print(answer)
    print(divider_2 * divider_6)




if __name__ == "__main__":
    main()
