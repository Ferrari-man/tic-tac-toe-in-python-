import sys

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