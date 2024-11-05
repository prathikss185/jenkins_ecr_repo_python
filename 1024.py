import random
import os

# Directions for moves
UP = 'w'
DOWN = 's'
LEFT = 'a'
RIGHT = 'd'

# Define the grid size
SIZE = 4

def print_board(board):
    os.system('clear')  # Clear the console for better visualization (use 'cls' on Windows)
    for row in board:
        print('\t'.join(map(str, row)))
        print()

def initialize_board():
    board = [[0] * SIZE for _ in range(SIZE)]
    add_random_tile(board)
    add_random_tile(board)
    return board

def add_random_tile(board):
    empty_cells = [(r, c) for r in range(SIZE) for c in range(SIZE) if board[r][c] == 0]
    if empty_cells:
        r, c = random.choice(empty_cells)
        board[r][c] = random.choice([2, 4])

def compress_line(line):
    """Shift non-zero tiles to the left and merge same-valued tiles."""
    new_line = [num for num in line if num != 0]  # Remove zeros
    merged = []
    skip = False
    for i in range(len(new_line) - 1):
        if skip:
            skip = False
            continue
        if new_line[i] == new_line[i + 1]:
            merged.append(new_line[i] * 2)
            skip = True
        else:
            merged.append(new_line[i])
    if len(new_line) > 0 and not skip:
        merged.append(new_line[-1])
    return merged + [0] * (SIZE - len(merged))

def move_left(board):
    """Move all rows to the left and merge tiles where possible."""
    for r in range(SIZE):
        board[r] = compress_line(board[r])

def move_right(board):
    """Move all rows to the right (reverse move_left)."""
    for r in range(SIZE):
        board[r] = list(reversed(compress_line(list(reversed(board[r])))))

def move_up(board):
    """Move all columns up."""
    for c in range(SIZE):
        col = [board[r][c] for r in range(SIZE)]
        new_col = compress_line(col)
        for r in range(SIZE):
            board[r][c] = new_col[r]

def move_down(board):
    """Move all columns down (reverse move_up)."""
    for c in range(SIZE):
        col = [board[r][c] for r in range(SIZE)]
        new_col = list(reversed(compress_line(list(reversed(col)))))
        for r in range(SIZE):
            board[r][c] = new_col[r]

def is_game_over(board):
    """Check if there are no more valid moves."""
    for r in range(SIZE):
        for c in range(SIZE):
            if board[r][c] == 0:
                return False
            if r < SIZE - 1 and board[r][c] == board[r + 1][c]:
                return False
            if c < SIZE - 1 and board[r][c] == board[r][c + 1]:
                return False
    return True

def main():
    board = initialize_board()
    while True:
        print_board(board)
        if is_game_over(board):
            print("Game Over!")
            break
        
        move = input("Use WASD to move (w=up, s=down, a=left, d=right): ").lower()
        if move == UP:
            move_up(board)
        elif move == DOWN:
            move_down(board)
        elif move == LEFT:
            move_left(board)
        elif move == RIGHT:
            move_right(board)
        else:
            print("Invalid move. Use W, A, S, or D.")
            continue
        
        add_random_tile(board)

if __name__ == '__main__':
    main()
