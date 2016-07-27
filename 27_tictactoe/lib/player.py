"""
"""

class PieceType(object):
    X = 'X'
    O = 'O'

class Player(object):

    def __init__(self, name, piece):
        if (len(name) == 0): raise ValueError("Player name must be at least 1 character")
        #if not (piece == PieceType.X or piece == PieceType.O): raise ValueError("Piece must be either 'X' or 'O'. Received: '%s'" % piece)

        self._name = name
        self._piece = piece
    
    def __str__(self):
        return  "{} ({})".format(self._name, self._piece) 

    def __repr__(self):
        return self.__str__()