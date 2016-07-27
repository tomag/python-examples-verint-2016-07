"""
"""
import sys
import player
class InvalidPlayError(Exception):
    def __init__(self, msg):
        super(InvalidPlayError, self).__init__(msg)

class OccupiedTileError(Exception):
    def __init__(self, msg):
        super(OccupiedTileError, self).__init__(msg)
        
class Board(object):
    _emptyPiece = " "

    def __init__(self, boardSize):
        if boardSize < 0: raise ValueError("Board size cannot be less than zero.")

        self._gameOver = True
        self._boardSize = boardSize        

    def start(self, players):
        print "Plyaers: ", len(players)
        if len(players) < 2: raise InvalidPlayError("Cannot start a game with less than 2 players")
        if not all(isinstance(p, player.Player) for p in players): raise InvalidPlayError("All parameters must be players")

        self._board = [[Board._emptyPiece for _ in range(self._boardSize)] for _ in range(self._boardSize)]
        self._gameOver = False
        self._players = players
        self._currPlayerIndex = 0
        self._totalTurns = 0
        self._playersCount = len(players)

    def val(self, row, column):
        self.validateBoardIndex(row, column)
        return self._board[row][column]
        
    def winner(self):
        if self._gameOver: 
            return self._players[self._winnerIndex]
        return None

    def play(self, row, column):
        self.ensureGameInProgress()
        self.validateBoardIndex(row, column)
        self.ensureEmptyTile(row, column)

        self._board[row][column] = self._players[self._currPlayerIndex]._piece
        self._totalTurns += 1
        self.printBoard()
        
        if self.checkWin():
            print "Game Over, {} won".format(self.winner())
        elif self.canContinuePlay():
            print "Game Over, Tie!"
        else:
            self.advancePlayer()

    def canContinuePlay(self):
        if self._totalTurns == self._boardSize**2:
            self._gameOver = True
            return False

    def advancePlayer(self):
        self.ensureGameInProgress()

        self._currPlayerIndex += 1
        if self._currPlayerIndex == self._playersCount:
            self._currPlayerIndex = 0

    def ensureGameInProgress(self):
        if self._gameOver:
            raise InvalidPlayError("Cannot play because there is no game in progress. start() a new game...")

    def ensureEmptyTile(self, row, column):
        row = int(row)
        column = int(column)

        if not (self._board[row][column] == Board._emptyPiece):
            raise OccupiedTileError("Piece can only be placed on an empty tile")

    def validateBoardIndex(self, *indexes):
        for index in indexes:
            if not (type(index) == int):
                raise ValueError("Indexes must be integers")
            if index < 0 or index >= self._boardSize:
                raise ValueError("Index %d is invalid! Index must be between 0-%s" % (index, self._boardSize))

    def checkWin(self):
        if self.checkWinByRow() or self.checkWinByColumn() or self.checkWinByDiagonal(): 
            return True
        return False

    def checkWinByRow(self):        
        for row in range(self._boardSize):            
            firstPiece = self._board[row][0]
            if firstPiece == Board._emptyPiece: continue
            counter = 0
            for col in range(self._boardSize):
                if firstPiece == self._board[row][col]: counter += 1                    
                else: break                    
            if counter == self._boardSize:
                return self.setWinner()
        return False
    
    def checkWinByColumn(self):
        for col in range(self._boardSize):
            firstPiece = self._board[0][col]
            if firstPiece == Board._emptyPiece: continue
            counter = 0
            for row in range(self._boardSize):
                if firstPiece == self._board[row][col]: counter += 1                    
                else: break                    
            if counter == self._boardSize:
                return self.setWinner()
        return False

    def checkWinByDiagonal(self):
        firstPiece = self._board[0][0]
        if not firstPiece == Board._emptyPiece: 
            counter = 0
            for index in range(self._boardSize):
                if firstPiece == self._board[index][index]: counter += 1
                else: break
            if counter == self._boardSize:
                return self.setWinner()

        firstPiece = self._board[0][self._boardSize - 1]
        if firstPiece == Board._emptyPiece: return False

        for index in range(self._boardSize): 
            if not firstPiece == self._board[index][self._boardSize - 1 - index]:
                return False
                
        return self.setWinner()

    def setWinner(self):
        self._winnerIndex = self._currPlayerIndex
        self._gameOver = True
        return True
        
    def printBoard(self):
        for row in range(self._boardSize):
            for col in range(self._boardSize):
                sys.stdout.write(self._board[row][col])
                if not col + 1 == self._boardSize: sys.stdout.write("|")
            print
        print