class BoardSpace:
    """
BoardSpace class goes in each spot on the game board, enabling tracking of
mine location, flags, # of spots near, etc.
    """
    isMine = False
    isFlagged = False
    isHidden = True
    numMines = 0


def getSpace(space):
    if space.isFlagged:
        return "f"
    elif space.isHidden:
        return "_"
    elif not space.isMine:
        return space.numMines
    else:
        return "b"


def showSpace(space):
    if space.isMine:
        return "b"
    else:
        return space.numMines
