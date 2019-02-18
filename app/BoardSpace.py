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
    """
    Returns information about specific board space
    Pre: 
        none
    Post: 
        none
    Args: 
        space
    Returns: 
        returns "f" if space is flagged, "_" if space is hidden, num nearby mines if space is not a mine, "b" if space is a mine
    """

    if space.isFlagged:
        return "f"
    elif space.isHidden:
        return "_"
    elif not space.isMine:
        return space.numMines
    else:
        return "b"


def showSpace(space):
    """
    Shows limited space details
    Pre: 
        none
    Post: 
        none
    Args: 
        space
    Returns: 
        returns "b" if space is a mine, else int number of nearby mines
    """

    if space.isMine:
        return "b"
    else:
        return space.numMines
