import numpy as np
import colorama

class Piece:
    COLOR_WHITE = colorama.Fore.WHITE
    COLOR_BLACK = colorama.Fore.BLUE
    SYMBOL = "?"

    def __init__(self, color, square):
        if color == "white":
            self.color = self.COLOR_WHITE
        elif color == "black":
            self.color = self.COLOR_BLACK

        self.square = square
        self.square.piece = self

        self.has_moved = False

    def move(self, new_square):
        self.has_moved = True
        self.square.piece = None
        self.square = new_square
        new_square.piece = self

    def __str__(self):
        s = self.color + self.SYMBOL.ljust(2)
        return s

class Pawn(Piece):
    SYMBOL = "P"

class Rook(Piece):
    SYMBOL = "R"

class Knight(Piece):
    SYMBOL = "N"

class Bishop(Piece):
    SYMBOL = "B"

class Queen(Piece):
    SYMBOL = "Q"

class King(Piece):
    SYMBOL = "K"