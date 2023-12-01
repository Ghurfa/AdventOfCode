class Block:
    def __init__(self, squares: list[(int, int)]):
        self.squares = squares

    def try_move(self, delta_x, delta_y, board: list[list[bool]]) -> bool:
        for (square_x, square_y) in self.squares:
            if square_y + delta_y < 0 or square_x + delta_x < 0 or square_x + delta_x >= 7:
                return False
            while square_y + delta_y >= len(board):
                board.append([False] * 7)
            if board[square_y + delta_y][square_x + delta_x]:
                return False
        self.squares = [(x + delta_x, y + delta_y) for (x, y) in self.squares]
        return True

    def top_block(self) -> int:
        return max(y for (x, y) in self.squares)

    def bottom_block(self) -> int:
        return min(y for (x, y) in self.squares)

    def add_to_board(self, board: list[list[bool]], board_tops: list[int]) -> int: # returns pop amount
        for (x, y) in self.squares:
            if board[y][x]:
                raise Exception()
            board[y][x] = True
            if y > board_tops[x]:
                board_tops[x] = y
        truncation_amt = min(board_tops) + 1
        for x in range(0, 7):
            board_tops[x] -= truncation_amt
        for _ in range(truncation_amt):
            board.pop(0)
        return truncation_amt

def make_block(block_type: int, bottom: int) -> Block:
    if block_type == 0:
        return Block([(2, bottom), (3, bottom), (4, bottom), (5, bottom)])
    elif block_type == 1:
        return Block([(2, bottom + 1), (3, bottom), (3, bottom + 1), (3, bottom + 2), (4, bottom + 1)])
    elif block_type == 2:
        return Block([(2, bottom), (3, bottom), (4, bottom), (4, bottom + 1), (4, bottom + 2)])
    elif block_type == 3:
        return Block([(2, bottom), (2, bottom + 1), (2, bottom + 2), (2, bottom + 3)])
    elif block_type == 4:
        return Block([(2, bottom), (2, bottom + 1), (3, bottom), (3, bottom + 1)])
    else:
        raise Exception()

def tops_eq(a: list[int], b: list[int]) -> bool:
    for i in range(7):
        if a[i] != b[i]:
            return False
    return True

def main():
    jet_dirs = list() # true if right
    with open("testinput.txt", encoding='UTF-8') as file:
        line = file.readline().strip()
        for ch in line:
            if ch == '<':
                jet_dirs.append(-1)
            elif ch == '>':
                jet_dirs.append(1)
            else:
                raise Exception()
    tops = [-1] * 7
    jet_idx = 0
    piece_idx = 0
    piece_count = 2022
    truncated_amt = 0
    board = []
    while piece_idx < piece_count:
        block = make_block(piece_idx % 5, max(tops) + 4)

        while True:
            jet_delta_x = jet_dirs[jet_idx % len(jet_dirs)]
            jet_idx += 1

            block.try_move(jet_delta_x, 0, board)
            could_fall = block.try_move(0, -1, board)
            if not could_fall:
                truncated_amt += block.add_to_board(board, tops)
                break
        piece_idx += 1

    
    print(max(tops) + 1 + truncated_amt)


if __name__ == "__main__":
    main()
