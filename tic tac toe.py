# Set up the board
board = [[" ", " ", " "],
         [" ", " ", " "],
         [" ", " ", " "]]

# Set up the player's turn
player = "X"

# Set up the game loop
game_over = False
while not game_over:
    # Display the board
    for row in board:
        print(" ".join(row))
    print()

    #getting coordinates for move
    try:
        row = int(input("Enter row (1-3): "))
        col = int(input("Enter column (1-3): "))
    
    #invalid token handling
    except ValueError:
        print("Please enter a valid number.")
        continue
    
    #invalid range handling  
    if row<1 or row>3 or col<1 or col>3:
        print('please enter a number int the range [1-3]')
        continue
        
    #getting appropriate indexing 
    row-=1 ; col-=1
    if board[row][col] == " ":
        board[row][col] = player
        if player == "X":
            player = "O"
        else:
            player = "X"
    else:
        print("That space is already taken!")

    # Check for a win
    # Horizental and vertical
    for row in range(3):
        if board[row][0] == board[row][1] == board[row][2] and board[row][0] != " ":
            game_over = True
            print(f"Player {board[row][0]} wins!")
    
    for col in range(3):
        if board[0][col] == board[1][col] == board[2][col] and board[0][col] != " ":
            game_over = True
            print(f"Player {board[0][col]} wins!")
    
    #diagonal
    if board[0][0] == board[1][1] == board[2][2] and board[0][0] != " ":
        game_over = True
        print(f"Player {board[0][0]} wins!")
    
    if board[0][2] == board[1][1] == board[2][0] and board[0][2] != " ":
        game_over = True
        print(f"Player {board[0][2]} wins!")
