def game_loop():
    board = ChessBoard()

    # Initialize the board with pieces
    # ... (code to place pieces on the board)

    while True:
        # Get the user's move input
        move = input("Enter your move (e.g., e2e4): ")

        # Convert the move input into starting and ending positions
        start = (ord(move[0]) - ord('a'), int(move[1]) - 1)
        end = (ord(move[2]) - ord('a'), int(move[3]) - 1)

        # Check if the move is valid
        if board.move_piece(start, end):
            print("Valid move!")
        else:
            print("Invalid move!")