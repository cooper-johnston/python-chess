import numpy as np
import colorama

from pieces import *

class ChessBoard:
    def __init__(self):
        self._init_squares()
        self._init_pieces()

        self.white_to_move = True

    def _init_squares(self):
        indices = np.indices((8, 8)).transpose(1, 2, 0)

        self.squares = np.array([
            [Square(index=i) for i in rank]
            for rank in indices
        ])

    def _init_pieces(self):
        self.black_pieces = [
            Pawn(color="black", square=self.squares[1, i])
            for i in range(8)
        ]
        self.black_pieces += [
            Rook(color="black", square=self.squares[0, 0]),
            Rook(color="black", square=self.squares[0, 7]),
            Knight(color="black", square=self.squares[0, 1]),
            Knight(color="black", square=self.squares[0, 6]),
            Bishop(color="black", square=self.squares[0, 2]),
            Bishop(color="black", square=self.squares[0, 5]),
            Queen(color="black", square=self.squares[0, 3]),
            King(color="black", square=self.squares[0, 4])
        ]

        self.white_pieces = [
            Pawn(color="white", square=self.squares[6, i])
            for i in range(8)
        ]
        self.white_pieces += [
            Rook(color="white", square=self.squares[7, 0]),
            Rook(color="white", square=self.squares[7, 7]),
            Knight(color="white", square=self.squares[7, 1]),
            Knight(color="white", square=self.squares[7, 6]),
            Bishop(color="white", square=self.squares[7, 2]),
            Bishop(color="white", square=self.squares[7, 5]),
            Queen(color="white", square=self.squares[7, 3]),
            King(color="white", square=self.squares[7, 4])
        ]

        self.pieces = self.white_pieces + self.black_pieces

    def __str__(self):
        rank_labels = [str(i) for i in range(8, 0, -1)]
        file_labels = ["a", "b", "c", "d", "e", "f", "g", "h"]
        if not self.white_to_move:
            display_squares = self.squares[::-1, ::-1]
            rank_labels.reverse()
            file_labels.reverse()
        else:
            display_squares = self.squares

        s = ""
        for rank, i in zip(display_squares, rank_labels):
            s += i.ljust(2)
            for square in rank:
                s += str(square)
            s += "\n"
        s += "  " + " ".join(file_labels)

        return s
    
    def play(self):
        while True:
            print(f"\n{self}")

            player_to_move = "white" if self.white_to_move else "black"
            move = input(f"Enter {player_to_move}'s move: ")

            start_square, new_square = self._parse_move(move)
            start_square.piece.move(new_square)

            self.white_to_move = not self.white_to_move

    def _parse_move(self, move): # Will change to use algebraic notation later
        start_square = self._get_square(move[:2])
        new_square = self._get_square(move[2:])

        return start_square, new_square

    def _get_square(self, square_name):
        rank_index = 8 - int(square_name[1])
        file_index = "abcdefgh".find(square_name[0])
        square = self.squares[rank_index, file_index]

        return square

class Square:
    COLOR_LIGHT = colorama.Back.MAGENTA
    COLOR_DARK = colorama.Back.BLACK

    def __init__(self, index):
        self.color = (self.COLOR_LIGHT, self.COLOR_DARK)[index.sum() % 2]
        self.index = index
        self.piece = None

    def __str__(self):
        piece_symbol = str(self.piece) if self.piece is not None else "  "
        s = f"{self.color}{piece_symbol}{colorama.Style.RESET_ALL}"
        return s
    
if __name__ == "__main__":
    colorama.init()

    board = ChessBoard()
    board.play()