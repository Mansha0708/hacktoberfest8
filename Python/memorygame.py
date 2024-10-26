import random

def create_board(size):
    numbers = list(range(1, (size * size // 2) + 1)) * 2
    random.shuffle(numbers)
    return [numbers[i:i + size] for i in range(0, len(numbers), size)]

def display_board(board, revealed):
    for i in range(len(board)):
        row = ""
        for j in range(len(board[i])):
            if revealed[i][j]:
                row += f"{board[i][j]} "
            else:
                row += "X "
        print(row)
    print()

def check_for_match(board, first, second):
    return board[first[0]][first[1]] == board[second[0]][second[1]]

def memory_game(size):
    board = create_board(size)
    revealed = [[False] * size for _ in range(size)]
    pairs_found = 0
    total_pairs = (size * size) // 2

    while pairs_found < total_pairs:
        display_board(board, revealed)
        first = tuple(map(int, input("Enter the coordinates of the first card (row col): ").split()))
        revealed[first[0]][first[1]] = True
        display_board(board, revealed)

        second = tuple(map(int, input("Enter the coordinates of the second card (row col): ").split()))
        revealed[second[0]][second[1]] = True
        display_board(board, revealed)

        if check_for_match(board, first, second):
            print("It's a match!")
            pairs_found += 1
        else:
            print("Not a match. Try again.")
            revealed[first[0]][first[1]] = False
            revealed[second[0]][second[1]] = False

    print("Congratulations! You've found all pairs!")

if __name__ == "__main__":
    board_size = int(input("Enter the board size (even number, e.g., 4 for 4x4): "))
    memory_game(board_size)
