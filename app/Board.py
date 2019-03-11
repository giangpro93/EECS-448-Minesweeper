from BoardSpace import BoardSpace, getSpace, showSpace, getRawSpace
import random
import json


class Board:
    """
    Board class contains the 2D array of BoardSpaces to hold game info
    Handles all things related to the game and is called by executive
    """

    # initializes the board
    def __init__(self, rows, cols, mines):
        """
        Initializes Board object
        Pre: 
            valid parameters
        Post: 
            Initializes member variables based on user input 
        Args: 
            int numRows, int numCols, int numMines
        Returns: 
            No return
        """

        self.m_rows = rows
        self.m_cols = cols
        self.m_numMines = mines
        self.m_numFlags = mines
        self.m_numMinesFlagged = 0
        self.m_board = []
        for r in range(0, rows):
            self.m_board.append([])
            for c in range(0, cols):
                self.m_board[r].append(BoardSpace())

    # prints board to terminal(currently)

    def printBoard(self):
        """
        prints board to console
        Pre: 
            valid board instantiated
        Post: 
            board written to console
        Args: 
            No Arguments
        Returns: 
            No return
        """

        for x in range(0, self.m_rows):
            for y in range(0, self.m_cols):
                print(getSpace(self.m_board[x][y]), end=' ')
            print()

    # shows either bomb or number of spaces around bomb
    def showBoard(self):
        """
        prints board to console, showing space detail
        Pre: 
            valid board instantiated
        Post: 
            board written to console
        Args: 
            No Arguments
        Returns: 
            No return
        """

        for x in range(0, self.m_rows):
            for y in range(0, self.m_cols):
                print(showSpace(self.m_board[x][y]), end='')
            print()

    # shows flags on the board
    def showFlags(self):
        """
        prints board to console, showing flags
        Pre: 
            valid board instantiated
        Post: 
            board written to console
        Args: 
            No Arguments
        Returns: 
            No return
        """

        for x in (self.m_rows-1):
            for y in (self.m_cols-1):
                if self.m_board[x][y].isFlagged():
                    print("f")
                else:
                    print("0")
            print('\0')

    # takes first step, then places all bombs
    def firstStep(self, xpos, ypos):
        """
        Handles user's first move, setting mines and calculating nearby spaces
        Pre: 
            valid x and y coordinates
        Post: 
            mines set and nearby spaces calculated
        Args: 
            int xpos (row), int ypos (column)
        Returns: 
            No return
        """

        self.placeBombs(xpos, ypos)
        self.calculateNearby()
        self.selectSpace(xpos, ypos)

    # places all mines around the first space stepped on
    def placeBombs(self, xpos, ypos):
        """
        Places mines randomly around map
        Pre: 
            valid x and y coordinates, numMines
        Post: 
            mines set randomly around map
        Args: 
            int xpos (row), int ypos (column)
        Returns: 
            none
        """

        # initializes a 1D array to randomly place bombs in indicies
        maxIndex = self.m_cols * self.m_rows
        mineIndex = [False] * (maxIndex-1)

        # initializes a certian number of mines
        for x in range(0, self.m_numMines):
            mineIndex[x] = True

        # shuffle the array to achieve randomness
        random.shuffle(mineIndex)

        # copy 1D array into 2D array, adjusting for xpos,ypos
        collision = 0
        for i in range(0, self.m_rows):
            for j in range(0, self.m_cols):
                if i == xpos and j == ypos:
                    collision = 1
                elif (mineIndex[j+(i*self.m_cols)-collision]):
                    self.m_board[i][j].isMine = True

    def calculateNearby(self):
        """
        Calculates quantity of nearby mines for all mines
        Pre: 
            initialized boardspaces
        Post: 
            each boardspace in board object now knows have many mines surround it
        Args: 
            none
        Returns: 
            none
        """

        for i in range(0, self.m_rows):
            for j in range(0, self.m_cols):
                if not self.m_board[i][j].isMine:
                    self.m_board[i][j].numMines = self.calcAround(i, j)

    def calcAround(self, xpos, ypos):
        """
        Determines nearby quantity of mines for a single board space
        Pre: 
            valid x and y coordinates
        Post: 
            individual boardspace knows how many mines surround it
        Args: 
            int xpos (row), int ypos (column)
        Returns: 
            integer representing nearby mine count
        """

        count = 0
        for x in range(max(xpos - 1, 0), min(xpos + 2, self.m_rows)):
            for y in range(max(ypos - 1, 0), min(ypos + 2, self.m_cols)):
                if ((x != xpos or y != ypos) and self.m_board[x][y].isMine):
                    count += 1

        return count

    def recUnhide(self, xpos, ypos):
        """
        Recursively unhide spaces until there are mines surrounding it
        Pre: 
            valid x and y coordinates
        Post: 
            Boardspaces are unhidden until there are nearby mines
        Args: 
            int xpos (row), int ypos (column)
        Returns: 
            No return
        """

        if self.m_board[xpos][ypos].numMines == 0 and self.m_board[xpos][ypos].isHidden:
            self.m_board[xpos][ypos].isHidden = False
            for x in range(max(xpos - 1, 0), min(xpos + 2, self.m_rows)):
                for y in range(max(ypos - 1, 0), min(ypos + 2, self.m_cols)):
                    if x != xpos or y != ypos:
                        self.recUnhide(x, y)
        self.m_board[xpos][ypos].isHidden = False

    # -------------------------
    # methods for Executive to call (excluding initialize)

    # toggleFlag Space if valid
    def toggleFlagSpace(self, row, col):
        """
        Toggles flag on/off
        Pre: 
            valid x and y coordinates, has flags remaining
        Post: 
            Boardspace flag toggled on/off
        Args: 
            int xpos (row), int ypos (column)
        Returns: 
            No return
        Raise: 
            RuntimeError if no flags remain
        """

        # check if we can flag the space
        if not self.m_board[row][col].isFlagged and self.m_numFlags > 0:
            self.m_board[row][col].isFlagged = True
            self.m_numFlags -= 1
            # if the space is a mine, update correctedly flagged count
            if self.m_board[row][col].isMine:
                self.m_numMinesFlagged += 1
        # check if space is already flagged, then remove
        elif self.m_board[row][col].isFlagged:
            self.m_board[row][col].isFlagged = False
            self.m_numFlags += 1
            # if the space is a mine, update correctedly flagged count
            if self.m_board[row][col].isMine:
                self.m_numMinesFlagged -= 1

        # throw an exception if you're out of flags
        else:
            raise RuntimeError("Out of flags")

    # user clicks a spot
    # returns true if a mine is hit, else false
    def selectSpace(self, row, col):
        """
        Select a space to reveal
        Pre: 
            valid x and y coordinates
        Post: 
            Either loses game (mine hit) or unhides selected boardspace
        Args: 
            int xpos (row), int ypos (column)
        Returns: 
            True if mine is hit, else False
        """

        # if the selected space is a mine
        if self.m_board[row][col].isFlagged:
            return False
        if self.m_board[row][col].isMine:
            return True
        else:
            # check if this spot is adjacent to other mines
            # if not, reveal 8 surrounding spaces in recursive function
            self.recUnhide(row, col)

            # return false
            return False

    # check if the user has flagged all mines - true if user has won, else false
    def userWin(self):
        """
        Check if the user has flagged all mines, which is victory
        Pre: 
            none
        Post: 
            none
        Args: 
            none
        Returns: 
            True if user has won, else False
        """

        if self.m_numMines == self.m_numMinesFlagged:
            return True
        else:
            return False

    def boardToJson(self):
        """
        Generates json to pass to front-end
        Pre: 
            none
        Post: 
            json file generated
        Args: 
            none
        Returns: 
            json file with all board information
 
        """

        myBoard = {}
        space = 0
        for x in range(0, self.m_rows):
            for y in range(0, self.m_cols):
                myBoard.update({space: getSpace(self.m_board[x][y])})
                space += 1
        return myBoard


    def cheatModeBoardToJson(self):
        myBoard = {}
        space = 0
        for x in range(0, self.m_rows):
            for y in range(0, self.m_cols):
                myBoard.update({space: getRawSpace(self.m_board[x][y])})
                space += 1
        return myBoard


    # end of Executive call function
    # ------------------------------
