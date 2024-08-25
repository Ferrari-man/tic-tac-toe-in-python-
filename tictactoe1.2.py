import sys
# Function to check if the player wins
def check_win(player):
    winning_combinations = [
        [0, 1, 2], [3, 4, 5], [6, 7, 8],  # Rows
        [0, 3, 6], [1, 4, 7], [2, 5, 8],  # Columns
        [0, 4, 8], [2, 4, 6]  # Diagonals
    ]
    for combination in winning_combinations:
        if all(board[i] == player for i in combination):
            return True
    return False

# Function to check if there is a draw
def check_draw():
    return all(cell != ' ' for cell in board)

# Initialize the board
board = [' ' for _ in range(9)]

# Function to handle user input
def get_user_input():
    try:
        return int(input("Enter a position (1-9): "))
    except ValueError:
        sys.exit("Invalid input. Exiting...")

# Function to print the board
def print_board():
    for i in range(0, 9, 3):
        print(f"{board[i]} | {board[i+1]} | {board[i+2]}")
        if i < 6:
            print("--+---+--")

# Function to play the game
def play_game():
    current_player = 'X'
    while True:
        print_board()
        position = get_user_input()
        if position < 1 or position > 9:
            print("Invalid move. Try again.")
            continue
        position -= 1
        if board[position] == ' ':
            board[position] = current_player
            if check_win(current_player):
                print_board()
                print(f"Player {current_player} wins!")
                break
            if check_draw():
                print_board()
                print("Game is over. It's a draw!")
                sys.exit()
            # Switch the current player
            current_player = 'O' if current_player == 'X' else 'X'
        else:
            print("Invalid move. Try again.")

# Start the game
play_game()
def check_win(player):
    winning_combinations = [
        [0, 1, 2], [3, 4, 5], [6, 7, 8],  # Rows
        [0, 3, 6], [1, 4, 7], [2, 5, 8],  # Columns
        [0, 4, 8], [2, 4, 6]  # Diagonals
    ]
    for combination in winning_combinations:
        if all(board[i] == player for i in combination):
            return True
    return False

# Function to check if there is a draw
def check_draw():
    return all(cell != ' ' for cell in board)

# Initialize the board
board = [' ' for _ in range(9)]

# Function to handle user input
def get_user_input():
    try:
        return int(input("Enter a position (1-9): "))
    except ValueError:
        sys.exit("Invalid input. Exiting...")

# Function to print the board
def print_board():
    for i in range(0, 9, 3):
        print(f"{board[i]} | {board[i+1]} | {board[i+2]}")
        if i < 6:
            print("--+---+--")

# Function to play the game
def play_game():
    current_player = 'X'
    while True:
        print_board()
        position = get_user_input()
        if position < 1 or position > 9:
            print("Invalid move. Try again.")
            continue
        position -= 1
        if board[position] == ' ':
            board[position] = current_player
            # Switch the current player
            current_player = 'O' if current_player == 'X' else 'X'
        else:
            print("Invalid move. Try again.")

# Start the game
play_game()