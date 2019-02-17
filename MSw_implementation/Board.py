from BoardSpace import BoardSpace
from BoardSpace import getSpace
from BoardSpace import showSpace

class Board:


	#initializes the board
	def __init__(rows, cols, mines):
		m_rows = rows
		m_cols = cols
		m_numMines = mines
		m_numFlags = mines
		#track number of mines correctly flagged
		m_numMinesFlagged = 0
		m_board = []
		for r in range(0,rows):
			m_board.append([])
			for c in range(0,cols):
				m_board[r].append(BoardSpace())


	#prints board to terminal(currently)
	def printBoard():
		for x in m_rows:
			for y in m_cols:
				print m_board[x][y].getSpace()
				print " "
			print "\n"

	#shows either bomb or number of spaces around bomb
	def showBoard():
		for x in m_rows:
			for y in m_cols:
				print m_board[x][y].showSpace()
				print " "
			print "\n"

	#shows flags on the board
	def showFlags():
		for x in (m_rows-1):
			for y in (m_cols-1):
				if m_board[x][y].isFlagged():
					print "f"
				else:
					print "0"
			print "\n"

	#takes first step, then places all bombs
	def firstStep(xpos, ypos):
		placeBombs(xpos, ypos)
		calculateNearby()
		selectSpace(xpos,ypos)


	#places all mines around the first space stepped on
	def placeBombs(xpos,ypos):

		#initializes a 1D array to randomly place bombs in indicies
		maxIndex = m_cols * m_rows
		mineIndex = Array.new(maxIndex-1, false)

		#initializes a certian number of mines
		for x in (0...m_numMines):
			mineIndex[x] = True
		end

		#shuffle the array to achieve randomness
		mineIndex = mineIndex.shuffle()

		#copy 1D array into 2D array, adjusting for xpos,ypos
		collision = 0
		for i in m_rows:
			for j in m_cols:
				if i == xpos && j == ypos:
					collision = 1
				elif (mineIndex[i+(j*m_rows)-collision]):
					m_board[i][j].setMine()


	def calculateNearby():
		for i in m_rows:
			for j in m_cols:
				if(not m_board[i][j].isThisAMine()):
					m_board[i][j].setNumMines(calcAround(i,j))


	def calculateNearby():
		for i in range(0, m_rows):
			for j in range(0, m_cols):
				if not m_board[i][j].isThisAMine():
					m_board[i][j].setNumMines(calcAround(i,j))

	def calcAround(xpos,ypos):
		count = 0
		for x in range(xpos - 1, xpos + 1):
			for y in range(ypos - 1, xpos + 1):
				if (x != xpos || y != ypos && board[x][y].isThisAMine():
					count++

		return count



	def recUnhide(xpos,ypos):
		if m_board[xpos][ypos].getNumMines() == 0 && @m_board[xpos][ypos].isThisHidden():
			m_board[xpos][ypos].unhide()
			for x in range(xpos-1, xpos+1):
				for y in range(ypos-1, ypos+1):
					if x != xpos && y != ypos:
						recUnhide(x, y)
		else
			m_board[xpos][ypos].unhide()

	#-------------------------
	#methods for Executive to call (excluding initialize)

	#toggleFlag Space if valid
	def toggleFlagSpace(row, col):
		#check if we can flag the space
		if not m_board[row][col].isFlagged() && m_numFlags > 0:
			m_board[row][col].toggleFlag()
			m_numFlags -= 1
			#if the space is a mine, update correctedly flagged count
			if m_board[row][col].isThisAMine():
				m_numMinesFlagged += 1
		#check if space is already flagged, then remove
		elif m_board[row][col].isFlagged():
			m_board[row][col].toggleFlag()
			m_numFlags += 1
			#if the space is a mine, update correctedly flagged count
			if m_board[row][col].isThisAMine()
				m_numMinesFlagged -= 1

		#throw an exception if you're out of flags
		else:
			raise RuntimeError("Out of flags")



	#user clicks a spot
	#returns true if a mine is hit, else false
	def selectSpace(row, col):
		#if the selected space is a mine
		if m_board[row][col].isThisAMine():
			return True
		else:
			#check if this spot is adjacent to other mines
			#if not, reveal 8 surrounding spaces in recursive function
			recUnhide(row,col)

			#return false
			return False

	#check if the user has flagged all mines - true if user has won, else false
	def userWin():
		if m_numMines == m_numMinesFlagged:
			return True
		else:
			return False



	#end of Executive call functions
	#------------------------------





obj = Board(10,10,3)
