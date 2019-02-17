from BoardSpace import BoardSpace, getSpace, showSpace
import random

class Board:


	#initializes the board
	def __init__(self,rows, cols, mines):
		self.m_rows = rows
		self.m_cols = cols
		self.m_numMines = mines
		self.m_numFlags = mines
		self.m_numMinesFlagged = 0
		self.m_board = []
		for r in range(0,rows):
			self.m_board.append([])
			for c in range(0,cols):
				self.m_board[r].append(BoardSpace())


	#prints board to terminal(currently)
	def printBoard(self):
		for x in range(0,self.m_rows):
			for y in range(0,self.m_cols):
				print(getSpace(self.m_board[x][y]), end=' ')
			print()

	#shows either bomb or number of spaces around bomb
	def showBoard(self):
		for x in range(0,self.m_rows):
			for y in range (0,self.m_cols):
				print(showSpace(self.m_board[x][y]), end='')
			print()

	#shows flags on the board
	def showFlags(self):
		for x in (m_rows-1):
			for y in (m_cols-1):
				if m_board[x][y].isFlagged():
					print("f")
				else:
					print("0")
			print('\0')

	#takes first step, then places all bombs
	def firstStep(self, xpos, ypos):
		self.placeBombs(xpos, ypos)
		self.calculateNearby()
		self.selectSpace(xpos,ypos)


	#places all mines around the first space stepped on
	def placeBombs(self, xpos,ypos):

		#initializes a 1D array to randomly place bombs in indicies
		maxIndex = self.m_cols * self.m_rows
		if (ypos == 0 or ypos == self.m_rows - 1):
			maxIndex -= 3
			if (xpos == 0 or xpos == self.m_cols - 1):
				maxIndex -= 2
		else:
			if (xpos == 0 or xpos == self.m_cols - 1):
				maxIndex -= 3
		mineIndex = [False] * (maxIndex-1)

		#initializes a certian number of mines
		for x in range(0, self.m_numMines):
			mineIndex[x] = True

		#shuffle the array to achieve randomness
		random.shuffle(mineIndex)

		#copy 1D array into 2D array, adjusting for xpos,ypos
		collision = 0
		for i in range(0, self.m_rows):
			for j in range(0,self.m_cols):
				if abs(i-ypos) <= 1 and abs(j-xpos) <= 1:
					collision += 1
				elif (mineIndex[j+(i*self.m_cols)-collision]):
					self.m_board[i][j].isMine = True

	def calculateNearby(self):
		for i in range(0, self.m_rows):
			for j in range(0, self.m_cols):
				if not self.m_board[i][j].isMine:
					self.m_board[i][j].numMines = self.calcAround(i,j)

	def calcAround(self,xpos,ypos):
		count = 0
		for x in range(max(xpos - 1, 0), min(xpos + 2,self.m_cols)):
			for y in range(max(ypos - 1, 0), min(ypos + 2,self.m_rows)):
				if ((x != xpos or y != ypos) and self.m_board[x][y].isMine):
					count+=1

		return count



	def recUnhide(self, xpos,ypos):
		if self.m_board[xpos][ypos].numMines == 0 and self.m_board[xpos][ypos].isHidden:
			self.m_board[xpos][ypos].isHidden = False
			for x in range(max(xpos - 1, 0), min(xpos + 2,self.m_cols)):
				for y in range(max(ypos - 1, 0), min(ypos + 2,self.m_rows)):
					if x != xpos or y != ypos:
						self.recUnhide(x, y)
		self.m_board[xpos][ypos].isHidden = False

	#-------------------------
	#methods for Executive to call (excluding initialize)

	#toggleFlag Space if valid
	def toggleFlagSpace(row, col):
		#check if we can flag the space
		if not m_board[row][col].isFlagged() and m_numFlags > 0:
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
			if m_board[row][col].isThisAMine():
				m_numMinesFlagged -= 1

		#throw an exception if you're out of flags
		else:
			raise RuntimeError("Out of flags")



	#user clicks a spot
	#returns true if a mine is hit, else false
	def selectSpace(self, row, col):
		#if the selected space is a mine
		if self.m_board[row][col].isMine:
			return True
		else:
			#check if this spot is adjacent to other mines
			#if not, reveal 8 surrounding spaces in recursive function
			self.recUnhide(row,col)

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





obj = Board(10,10,10)
obj.firstStep(5,5)
obj.printBoard()
obj.showBoard()
