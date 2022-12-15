from enum import Enum


class Colors(Enum):  # The two colors a piece can have
    black = 1
    white = 0


class Direction(Enum):  # different directions a piece can move
    north = 1
    northeast = 2
    east = 3
    southeast = 4
    south = 5
    southwest = 6
    west = 7
    northwest = 8


class Title(Enum): #name of the pieces
    king = 1
    queen = 2
    bishop = 3
    knight = 4
    rook = 5
    pawn = 6


class Position: # A postion with respective to a board who's starting point is (0,0) and ends in (8,8)
    def __init__(self, i: int, j: int):
        self.coordinates = None
        self.x = i
        self.y = j

    def show(self):
        self.coordinates = [self.x, self.y]
        print(self.coordinates)


class ChessFigure:
    def __init__(self, color: Colors, title: Title, position: Position):
        self.hasMoved = False
        self.color = color
        self.title = title
        self.position = position

    def move(self, *args):
        print("moved")
        self.hasMoved = True


class Rook(ChessFigure):
    def __init__(self, color, position):
        super().__init__(color, Title.rook, position)

    def move(self, i, isRow):  # here "i" denotes the jumps taken by rook
        if isRow:
            self.position.x += i
        else:
            self.position.y += i


class Knight(ChessFigure):
    def __init__(self, color, position):
        super().__init__(color, Title.knight, position)

    def move(self, directionA: Direction, directionB: Direction): #for the knight to move one has to decide the main direction out if north,west,south and east and also if its taking the right ot left side respective to the initial direction.
        if directionA == Direction.north and directionB == Direction.northeast:
            self.position.x += 1
            self.position.y += 2
            self.hasMoved = True
        if directionA == Direction.east and directionB == Direction.northeast:
            self.position.x += 2
            self.position.y += 1
            self.hasMoved = True
        if directionA == Direction.east and directionB == Direction.southeast:
            self.position.x += 2
            self.position.y -= 1
            self.hasMoved = True
        if directionA == Direction.south and directionB == Direction.southeast:
            self.position.x += 1
            self.position.y -= 2
            self.hasMoved = True
        if directionA == Direction.south and directionB == Direction.southwest:
            self.position.x -= 1
            self.position.y -= 2
            self.hasMoved = True
        if directionA == Direction.west and directionB == Direction.southwest:
            self.position.x -= 2
            self.position.y -= 1
            self.hasMoved = True
        if directionA == Direction.west and directionB == Direction.northwest:
            self.position.x -= 2
            self.position.y += 1
            self.hasMoved = True
        if directionA == Direction.north and directionB == Direction.northwest:
            self.position.x -= 1
            self.position.y += 2
            self.hasMoved = True
        else:
            print("invalid move for knight")

    def beat(self, victim: ChessFigure):

        if self.hasMoved and self.position == victim.position: #for a piece to beat it should be in the range of movement and if beat the position of the victim piece is transferred to the moved piece.
            print(self.title.name, " has beat ", victim.title.name)


class Bishop(ChessFigure):
    def __init__(self, color, position):
        super().__init__(color, Title.bishop, position)
        self.moves = None

    def move(self, i, direction: Direction):  # here "i" denotes the jumps taken, "i" can be negative steps too
        for direction.value in [2, 4, 6, 8]: # These values correspond to the enum values defined
            self.position.y += i
            self.position.x += i
        else:
            print("invalid move for Bishop")

    def beat(self, victim: ChessFigure):

        if self.hasMoved and self.position == victim.position:
            print(self.title.name, " has beat ", victim.title.name)


class Pawn(ChessFigure):
    def __init__(self, color, position):
        super().__init__(color, Title.pawn, position)

    def move(self, leap=False): # a leap is if the player decides to take two jumps
        if self.hasMoved and leap == True:
            self.position.y += 2
        else:
            self.position.y += 1

    def beat(self, victim: ChessFigure):

        if victim.position.x == self.position.x + 1 and victim.position.y == self.position.y + 1: #if the paw decides to beat the chessfigure to the northeast
            print(self.title.name, " has beat ", victim.title.name)
            self.position = victim.position
        elif victim.position.x == self.position.x - 1 and victim.position.y == self.position.y + 1: #if the paw decides to beat the chessfigure to the northwest
            print(self.title.name, " has beat ", victim.title.name)
            self.position = victim.position


class Queen(ChessFigure):
    def __init__(self, color, position):
        super().__init__(color, Title.queen, position)

    def move(self, direction: Direction, jumps: int, *args):

        if direction.value == 1: #each value corresponds to the enum for directions
            self.position.y += jumps
        elif direction.value == 2:
            self.position.x += jumps
            self.position.y += jumps
        elif direction.value == 3:
            self.position.x += jumps
        elif direction.value == 4:
            self.position.x += jumps
            self.position.y -= jumps
        elif direction.value == 5:
            self.position.y -= jumps
        elif direction.value == 6:
            self.position.x -= jumps
            self.position.y -= jumps
        elif direction.value == 7:
            self.position.x -= jumps
        elif direction.value == 8:
            self.position.x -= jumps
            self.position.y += jumps

    def beat(self, victim: ChessFigure):

        if self.hasMoved and self.position == victim.position:
            print(self.title.name, " has beat ", victim.title.name)


class King(ChessFigure):
    def __init__(self, color, position, isCasstled=False):
        super().__init__(color, Title.king, position)
        self.isCasstled = isCasstled

    def castle(self, rook: Rook, direction: Direction):

        if rook.hasMoved == False and self.hasMoved == False:
            self.isCasstled = True
            if direction == Direction.east: #castling to the right side
                rook.position.x -= 2
                self.position.x += 2
            elif direction == Direction.west: #castling to the left side
                rook.position.x += 3
                self.position.x -= 2

    def move(self, direction: Direction):

        if direction.value == 1:
            self.position.y += 1
        elif direction.value == 2:
            self.position.x += 1
            self.position.y += 1
        elif direction.value == 3:
            self.position.x += 1
        elif direction.value == 4:
            self.position.x += 1
            self.position.y -= 1
        elif direction.value == 5:
            self.position.y -= 1
        elif direction.value == 6:
            self.position.x -= 1
            self.position.y -= 1
        elif direction.value == 7:
            self.position.x -= 1
        elif direction.value == 8:
            self.position.x -= 1
            self.position.y += 1

    def beat(self, victim: ChessFigure):

        if self.hasMoved and self.position == victim.position:
            print(self.title.name, " has beat ", victim.title.name)


class ChessBoard:

    def __init__(self):
        self.rookList = [
            Rook(Colors.white, Position(1, 1)),
            Rook(Colors.white, Position(1, 8)),
            Rook(Colors.black, Position(8, 1)),
            Rook(Colors.black, Position(8, 8))]
        self.kingList = [
            Knight(Colors.white, Position(1, 2)),
            Knight(Colors.white, Position(1, 7)),
            Knight(Colors.black, Position(8, 2)),
            Knight(Colors.black, Position(8, 7))]
        self.bishopList = [
            Bishop(Colors.white, Position(1, 3)),
            Bishop(Colors.white, Position(1, 6)),
            Bishop(Colors.black, Position(8, 3)),
            Bishop(Colors.black, Position(8, 6))]
        self.queenList = [
            Queen(Colors.white, Position(1, 5)),
            Queen(Colors.black, Position(8, 5))]
        self.KingList = [
            King(Colors.white, Position(1, 4)),
            King(Colors.black, Position(8, 4))]
        self.pawnList = []
        for i in range(8):
            self.pawnList.append(Pawn(Colors.white, Position(2, i + 1)))
        for i in range(8):
            self.pawnList.append(Pawn(Colors.black, Position(7, i + 1)))



