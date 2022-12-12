class Monkey:
    def __init__(self, items, operation, div, true_recv, false_recv):
        self.items = items
        self.operation = operation
        self.div = div
        self.true_recv = true_recv
        self.false_recv = false_recv
        self.inspect_count = 0

    def handle_item(self, monkeys):
        if len(self.items) == 0:
            return False

        item = self.items[0]
        self.items = self.items[1:]
        item = self.operation(item)

        item %= 223092870

        self.inspect_count += 1
        if item % self.div == 0:
            monkeys[self.true_recv].items.append(item)
        else:
            monkeys[self.false_recv].items.append(item)
        return True


def main():
    monkey_0 = Monkey([64, 89, 65, 95], lambda x: x * 7, 3, 4, 1)
    monkey_1 = Monkey([76, 66, 74, 87, 70, 56, 51, 66], lambda x: x + 5, 13, 7, 3)
    monkey_2 = Monkey([91, 60, 63], lambda x: x * x, 2, 6, 5)
    monkey_3 = Monkey([92, 61, 79, 97, 79], lambda x: x + 6, 11, 2, 6)
    monkey_4 = Monkey([93, 54], lambda x: x * 11, 5, 1, 7)
    monkey_5 = Monkey([60, 79, 92, 69, 88, 82, 70], lambda x: x + 8, 17, 4, 0)
    monkey_6 = Monkey([64, 57, 73, 89, 55, 53], lambda x: x + 1, 19, 0, 5)
    monkey_7 = Monkey([62], lambda x: x + 4, 7, 3, 2)

    test_0 = Monkey([79, 98], lambda x: x * 19, 23, 2, 3)
    test_1 = Monkey([54, 65, 75, 74], lambda x: x + 6, 19, 2, 0)
    test_2 = Monkey([79, 60, 97], lambda x: x * x, 13, 1, 3)
    test_3 = Monkey([74], lambda x: x + 3, 17, 0, 1)
    # monkeys = [test_0, test_1, test_2, test_3]
    monkeys = [monkey_0, monkey_1, monkey_2, monkey_3, monkey_4, monkey_5, monkey_6, monkey_7]


    for _ in range(0, 10000):
        for monkey in monkeys:
            while monkey.handle_item(monkeys):
                pass

    counts = [m.inspect_count for m in monkeys]
    counts.sort()
    print(counts[-2] * counts[-1])

if __name__ == "__main__":
    main()
