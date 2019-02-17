from Board import Board
import json


class Executive:

    '''Define member variables'''
    m_board = Board(5, 5, 2)
    firstMove = True
    m_userID = 0

    def __init__(self, rows, cols, numMines, userID):
        if rows < 2 or cols < 2:
            raise RuntimeError('Invalid board size')
        if numMines < 1 or numMines > rows * cols - 1:
            raise RuntimeError('Invalid number of mines')

        self.m_board = Board(rows, cols, numMines)
        self.firstMove = True
        self.m_userID = userID
        return

    def leftClick(self, row, col):
        '''returns false is user loses game
            returns true if user made a valid move
        '''
        # if this is user's first move, still need to set mines
        if self.firstMove is True:
            self.m_board.firstStep(row, col)
            self.firstMove = False
        else:
            if self.m_board.selectSpace(row, col) is True:
                return (False)
        return

    def rightClick(self, row, col):
        '''returns -1 if user is out of flags
            returns 0 if flag was successfully planted
            returns 1 if user wins (all mines flagged)
        '''
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
        return self.m_userID
