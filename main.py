import random

def create_board():
    return [[' ' for _ in range(7)] for _ in range(6)]

def print_board(board):
    print("  " + "     ".join([chr(65 + i) for i in range(7)]))  # A, B, C, D, E, F, G for columns
    print("  " + "+-----" * 7 + '+')
    for row in range(6):
        print(str(row + 1) + " " + '|  ' + '  |  '.join(board[row]) + '  |')
        print("  " + "+-----" * 7 + '+')

def is_valid_location(board, row, col):
    return board[row][col] == ' '

def drop_piece(board, row, col, piece):
    board[row][col] = piece

def winning_move(board, piece):
    for c in range(4):
        for r in range(6):
            if (board[r][c] == piece and board[r][c+1] == piece and
                board[r][c+2] == piece and board[r][c+3] == piece):
                return True
    for c in range(7):
        for r in range(3):
            if (board[r][c] == piece and board[r+1][c] == piece and
                board[r+2][c] == piece and board[r+3][c] == piece):
                return True
    for c in range(4):
        for r in range(3):
            if (board[r][c] == piece and board[r+1][c+1] == piece and
                board[r+2][c+2] == piece and board[r+3][c+3] == piece):
                return True
    for c in range(4):
        for r in range(3, 6):
            if (board[r][c] == piece and board[r-1][c+1] == piece and
                board[r-2][c+2] == piece and board[r-3][c+3] == piece):
                return True

def is_full(board):
    return all(board[r][c] != ' ' for r in range(6) for c in range(7))

def get_computer_move(board):
    valid_moves = [(r, c) for r in range(6) for c in range(7) if is_valid_location(board, r, c)]
    return random.choice(valid_moves)

def play_game():
    board = create_board()
    game_over = False
    turn = 0

    print("Welcome to Connect Four!")
    print("Instructions:")
    print("1. Player 1 uses '🔵' and Player 2 (computer) uses '🔴'.")
    print("2. Players take turns to drop their piece into any valid location on the board using coordinates (e.g., A1, B5).")
    print("3. The first player to align four pieces horizontally, vertically, or diagonally wins.")
    print("4. If the board is full and no one has won, the game ends in a draw.")
    print("Let's begin!\n")
    print_board(board)
    
    while not game_over:
        try:
            if turn == 0:
                piece = '🔵'
                print("Player 1's turn")
                move_input = input("Select a location (e.g., A1, B5): ").upper()
                col = ord(move_input[0]) - 65  # Convert A-G to 0-6
                row = int(move_input[1]) - 1    # Convert 1-6 to 0-5
            else:
                piece = '🔴'
                print("Computer's turn")
                row, col = get_computer_move(board)
                move_input = chr(65 + col) + str(row + 1)
                print(f"Computer selected location: {move_input}")

            if col < 0 or col > 6 or row < 0 or row > 5:
                print("Invalid location. Please choose a location within the board (A1 to G6).")
                continue

            if is_valid_location(board, row, col):
                drop_piece(board, row, col, piece)

                if winning_move(board, piece):
                    print_board(board)
                    if turn == 0:
                        print("Player 1 wins!")
                    else:
                        print("Computer wins!")
                    game_over = True

                if is_full(board):
                    print_board(board)
                    print("The game is a draw!")
                    game_over = True

                print_board(board)
            else:
                print("Location occupied! Try a different location.")
            
            turn += 1
            turn %= 2

        except (ValueError, IndexError):
            print("Invalid input. Please enter a valid location (e.g., A1, B5).")

if __name__ == "__main__":
    play_game()
