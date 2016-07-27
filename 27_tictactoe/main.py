from lib import board
from lib import player

def initQuickGame():
    p1 = player.Player("Player 1", player.PieceType.X)
    p2 = player.Player("Player 2", player.PieceType.O)
    theBoard = board.Board(3)
    theBoard.start([p1, p2])
    return theBoard

def initCustomGame():
    print "Please choose the board size:",
    boardSize = int(raw_input())
    print "How many players?",
    playersCount = int(raw_input())
    players = []
    for i in range(playersCount):
        print "Player {} Name:".format(i + 1),
        name = raw_input()
        print "Player {} Piece: (only 1 character allowed)".format(i),
        piece = raw_input()
        p = player.Player(name, piece)
        players.append(p)
    theBoard = board.Board(boardSize)
    theBoard.start(players)
    return theBoard

print "Hello!"

def playGame():
    print "Starting Game!"
    print 
    winner = None
    while not winner:
        print "Player {}. Choose tile to place piece on the board".format(theBoard._currPlayerIndex+1)
        print "(two numbers with space between)"
        position = raw_input()
        position = " ".join(position.split()).split(" ")
        row = int(position[0])
        col = int(position[1])

        try:
            theBoard.play(row, col)
        except board.InvalidPlayError as e:
            print
            print "Error: ", e
            print "Try to play again"
        except board.OccupiedTileError as e:
            print
            print "Tile [{},{}] is already occupied. Choose another tile.".format(row, col)
            print
        winner = theBoard.winner()

while True:
    print "(Q|q)uick or (C|c)ustom game?"
    decision = raw_input()
    while not decision.lower() == 'c' and not decision.lower() == 'q':  
        print "(Q|q)uick or (C|c)ustom game?"
        decision = raw_input()
    theBoard = initCustomGame() if decision.lower() == 'c' else initQuickGame()

    playGame()

    print
    print "Another game? (Y|N)",
    decision = raw_input()
    if decision.lower() == 'n':
        break

print "Bye!"