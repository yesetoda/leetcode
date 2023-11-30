class ChessBoard:
    def __init__(self):
        self.board = [[None for _ in range(8)] for _ in range(8)]

    def place_piece(self, piece, x, y):
        self.board[y][x] = piece

    def move_piece(self, start, end):
        # Retrieve the piece at the starting position
        piece = self.board[start[1]][start[0]]

        # Remove the piece from the starting position
        self.board[start[1]][start[0]] = None

        # Place the piece at the ending position
        self.board[end[1]][end[0]] = piece