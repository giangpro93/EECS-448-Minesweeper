from Board.py import Board #import BoardSpace, getSpace, showSpace

class Executive:

    '''Define member variables'''
    m_rows = 0
    m_cols = 0
    m_numMines = 0
    gameOver = False
    wonGame = False
    m_board = 8
    firstMove = True
    



    def __init__(self, rows, cols, numMines):
        if rows < 2 or cols < 2:
            raise RuntimeError('Invalid board size')
        if numMines < 1 or numMines > rows * cols - 1:
            raise RuntimeError('Invalid number of mines')        

        self.m_rows = rows
        self.m_cols = cols
        self.m_numMines = numMines
        self.gameOver = False
        self.wonGame = False
        self.m_board = Board(self.m_rows,self.m_cols, self.m_numMines)
        self.firstMove = True
        return

    def leftClick(self, row, col):
        '''returns false is user loses game
            returns true if user made a valid move
        '''
        #if this is user's first move, still need to set mines
        if self.firstMove is True:
            firstStep(self.m_board, row, col)
            self.firstMove = False
        else:
            if selectSpace(self.m_Board, row, col) is True:
                return (False)
        return

    def rightClick(self, row, col):
        '''returns -1 if user is out of flags
            returns 0 if flag was successfully planted
            returns 1 if user wins (all mines flagged)
        '''
        try:
            toggleFlagSpace(self.m_board, row, col)
        except:
            return (-1)
        
        #check if user has won the game (flagged all mines)
        if userWin(self.m_board) is True:
            return 1
        else:
            return 0

        



    
