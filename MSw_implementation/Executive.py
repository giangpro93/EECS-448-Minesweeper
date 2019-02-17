from BoardSpace import BoardSpace, getSpace, showSpace

class Executive:

    def __init__(rows, cols, numMines):
        if rows < 2 or cols < 2:
            raise RuntimeError("Invalid board size")
        if numMines < 1 or numMines > rows * cols - 1:
            raise RuntimeError("Invalid number of mines")

        m_rows = rows
        m_cols = cols
        m_numMines = numMines
        gameOver = False
        wonGame = False

    
