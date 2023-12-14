import json

def tilt_north(board):
    for x in range(0, len(board[0])):
        curr_row = 0
        col = [line[x] for line in board]
        for i, ch in enumerate(col):
            if ch == '#':
                curr_row = i + 1
            else:
                board[i][x] = '.'
                if ch == 'O':
                    board[curr_row][x] = 'O'
                    curr_row += 1

def rotate(board):
    cols = []
    for x in range(0, len(board[0])):
        col = [line[x] for line in board]
        col.reverse()
        cols.append(col)
    return cols

def cycle(board):
    for _ in range(0, 4):
        tilt_north(board)
        board = rotate(board)
    return board

def get_load(board):
    score = 0
    for y, line in enumerate(board):
        for ch in line:
            if ch == 'O':
                score += len(board) - y
    return score

def main():
    board = []
    with open("14-input.txt", encoding='UTF-8') as file:
        for line in file:
            board.append([x for x in line.strip()])
    
    # Part 1

    # tilt_north(board)
    # print(get_load(board))


    # Part 2

    memo = []
    i = 0
    while not(json.dumps(board) in memo):
        memo.append(json.dumps(board))
        board = cycle(board)
        i += 1
    found_i = memo.index(json.dumps(board))
    cycle_len = i - found_i
    target = 1000000000
    answer_idx = found_i + (target - found_i) % cycle_len
    print(get_load(json.loads(memo[answer_idx])))
    
if __name__ == "__main__":
    main()
