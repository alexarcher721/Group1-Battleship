class Board:

    def __init__(self):
        """
        This constructs the full board, initialized to be empty of ships. 
        It contains a 2D self.waterGrid, waterGrid. Locations marked as '0' are water, 
        and these will be changed to S wherever there is a ship, and to * to 
        mark locations of hits. The S and * locations are obtained from two lists,
        shipSpots and shots, both of which are initialized to be empty.
        """
        
        self.shipObjects = [] # this is a list of ship objects. They will be checked to determine which ship is hit, and update ship coord, sunk variables
        self.shiplengths=[]
        self.waterGrid = [['O' for col in range(10)] for row in range(9)] # initialize board to be all 'O'
        self.oppGrid = [['*' for col in range(10)] for row in range(9)] # initialize board to be all '*'
        self.spots=0
        self.points=0
        self.allsunk=False
    def printBoard(self):
        """
        This method prints the waterGrid self.waterGrid with a border to mark coordinates
        (A-J for columns and 1-9 for rows). 
        I think we need TWO of these methods, printMyBoard, printOpponentBoard??
        Instruction #4 indicates that: players should be able to see their own board
        and all their ships, and also of course the opponent's board because that helsp determine
        where to fire (ships are hidden unless a spot is revealed via a hit). So 
        the difference is:
        printMyBoard shows all the ships, printOpponentBoard shows only locations shot at and
        whether or not they hit a shipSpot. We do not need to mark on the board if the
        ship is sunk or not (tho this is in the ship's bool variable) because the player knows.
        Each ship is the same size (depending on the number of ships each player gets).
        """
        topOfBoard = [' ', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J']
        # print top of board
        for i in topOfBoard:
            print(" ", end="")
            print(i, "", end = "")
        print()

        # print the rest of the board
        for row in range(9):
            print(row+1, " ", end = " ")
            for col in range(10):
                print(self.waterGrid[row][col], " ", end = "")
            print()

 
        # waterGrid will be updated as the game progresses, by createShip() and hits()
        # so original "O" is replaced with S for ship, * for hit, X for hit on a ship
        
    ##documentation for a method
    # @brief checks if ship placement would be valid
    # @param startx: x position in self.waterGrid
    # @param starty: y position in self.waterGrid
    # @param orient: orientation of ship orientation of ship:
    #       (L=left of start, R=right of start, U=up from start, D=down from start)
    # @param length: length of ship
    # @post returns true if ship placement works
    def printOpp(self):
        topOfBoard = [' ', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J']
        # print top of board
        for i in topOfBoard:
            print(" ", end="")
            print(i, "", end = "")
        print()

        # print the rest of the board
        for row in range(9):
            print(row+1, " ", end = " ")
            for col in range(10):
                print(self.oppGrid[row][col], " ", end = "")
            print()
    def isShipValid(self, orient, startx, starty, length):
        start = 0
        bool=True
        if orient == ('L' or 'l'):
            while start < length:
                if self.waterGrid[starty][startx-start] != 'O' and self.waterGrid[starty][startx-start] != "*":
                    bool=False
                start=start+1
        elif orient == ('R' or 'r'):
            while start < length:
                if self.waterGrid[starty][startx+start] != 'O' and self.waterGrid[starty][startx+start] != "*":
                    bool=False
                start=start+1
        elif orient == ('U' or 'u'):
            while start < length:
                if self.waterGrid[starty-start][startx] != 'O' and self.waterGrid[starty-start][startx] != "*":
                    bool=False
                start=start+1
        elif orient == ('D' or 'd'):
            while start < length:
                if self.waterGrid[starty+start][startx] != 'O' and self.waterGrid[starty+start][startx] != "*":
                    bool=False
                start=start+1
        return bool
    ##documentation for a method
    # @brief creates a ship
    # @param startx: x position in self.waterGrid
    # @param starty: y position in self.waterGrid
    # @param orient: orientation of ship orientation of ship:
    #       (L=left of start, R=right of start, U=up from start, D=down from start)
    # @param length: length of ship
    # @post none
    def createShip(self, startx, starty, orient, length,shipnumber): 
        start = 0
        shipcoords=[]
        self.shiplengths.append(length)
        if orient == ('L'):
            while start < length:
                self.waterGrid[starty][startx-start] = shipnumber
                shipcoords.append((starty,startx-start))
                start=start+1
                self.spots=self.spots+1
        elif orient == 'R':
            while start < length:
                self.waterGrid[starty][startx+start] = shipnumber
                shipcoords.append((starty,startx+start))
                start=start+1
                self.spots=self.spots+1
        elif orient == 'U':
            while start < length:
                self.waterGrid[starty-start][startx] = shipnumber
                shipcoords.append((starty-start,startx))
                start=start+1
                self.spots=self.spots+1
        elif orient == 'D':
            while start < length:
                self.waterGrid[starty+start][startx] = shipnumber
                shipcoords.append((starty+start,startx))
                start=start+1
                self.spots=self.spots+1
        self.shipObjects.append(shipcoords)
        self.points=self.points+1
    def hit(self, y, x):
        row = len(self.shipObjects)
        temp=self.spots
        for z in range(row):
            for w in range(len(self.shipObjects[z])):
                if self.shipObjects[z][w] == (y,x):
                    self.waterGrid[y][x] = "x"
                    self.oppGrid[y][x] = "x"
                    self.spots=self.spots-1
                    self.shiplengths[z]=self.shiplengths[z]-1
                    if self.shiplengths[z] == 0:
                        print("Ship is sunk!")
                        self.points=self.points-1
        if temp == self.spots:
            self.oppGrid[y][x] = "m"
    def score(self,opp):
        print("Player Ships Remaining:"+str(self.points))
        print("Opponent Ships Remaining:"+str(opp.points))
        if self.points == 0:
            print("Player 1 Won!")
            self.allsunk=True
        elif opp.points == 0:
            print("Player 2 Won!")
            opp.allsunk=False
