from Board import Board
import json


class Executive:
    """
        Runs the game by calling Board methods
    """

    #Define member variables
    m_board = Board(5, 5, 2)
    firstMove = True
    m_userID = 0

    def __init__(self, rows, cols, numMines, userID):
        """
            Initialize Executive
            Pre: 
                none
            Post: 
                member variables set to user specified values
            Args: 
                int rows, int cols, int numMines, int userID
            Returns: 
                none
            Raise:
                RuntimeError if board size is invalid or if invalid number of mines
        """
        if rows < 2 or cols < 2 or rows > 30 or cols > 30:
            raise RuntimeError('Invalid board size')
        if numMines < 1 or numMines > rows * cols - 1:
            raise RuntimeError('Invalid number of mines')

        self.m_board = Board(rows, cols, numMines)
        self.firstMove = True
        self.m_userID = userID
        return

    def leftClick(self, row, col):
        """
            Handles left click event - clicking on a new space
            Pre: 
                valid input for row and col
            Post: 
                Modifies board to unhide selected spot (and related)
            Args: 
                int row, int col
            Returns: 
                returns false is user loses game
        """
        # if this is user's first move, still need to set mines
        if self.firstMove is True:
            self.m_board.firstStep(row, col)
            self.firstMove = False
        else:
            if self.m_board.selectSpace(row, col) is True:
                return (False)
 
        return

    def rightClick(self, row, col):
        """
            Handles right click event - toggling flag
            Pre: 
                valid row and col input
            Post: 
                toggles flag and determines if user has won
            Args: 
                int rows, int cols
            Returns: 
                returns -1 if user is out of flags
                returns 0 if flag was successfully planted
                returns 1 if user wins (all mines flagged)
        """       
        try:
            self.m_board.toggleFlagSpace(row, col)
        except:
            return (-1)

        # check if user has won the game (flagged all mines)
        if self.m_board.userWin() is True:
            return 1
        else:
            return 0

    def getUserID(self):
        """
            Gets userID for Executive instance
            Pre: 
                none
            Post: 
                none
            Args: 
                none
            Returns: 
                int userID
        """
        return self.m_userID

    def getJson(self):
        """
            Pass through json
            Pre: 
                none
            Post: 
                none
            Args: 
                none
            Returns: 
                returns json file from board
        """
        return self.m_board.boardToJson()
