#BoardSpace class goes in each spot on the game board, enabling tracking of
#mine location, flags, # of spots near, etc.
class BoardSpace:

	def __init__(self):
		self.isMine = False
		self.isFlagged = False
		self.isHidden = True
		self.numMines = 0
	
	#Someone wants to toggle flag
	def toggleFlag():
		self.isFlagged = not self.isFlagged
	
	#Unhides a space
	def unhide():
		self.isHidden = False
	
	#Sets number of mines calculated by board
	def setNumMines(mines):
		self.numMines = mines
	

	#tells you if space is a mine
	def isThisAMine():
		return self.isMine
	
	#tells is space is flagged
	def isFlagged():
		return self.isFlagged
	
	#returns if space is hidden
	def isThisHidden():
		return self.isHidden
	
	#returns number of mines surrounding the space
	def getNumMines():
		return self.numMines

	#defines how the space should be displayed
	def getSpace():
		if self.isFlagged:
			return "f"
		elif self.isHidden:
			return "_"
		elif not self.isMine:
			return self.numMines
		else:
			return "b"

	#Shows either a bomb or a number of bombs around
	def showSpace():
		if self.isMine:
			return "b"
		else:
			return self.numMines



obj = BoardSpace()

print (obj.isFlagged())
print (obj.getNumMines())
print (obj.getSpace())
print (obj.showSpace())
print (obj.isThisAMine())

obj.setNumMines(10)
obj.setMine()
obj.toggleFlag()

print obj.isFlagged()
print obj.getNumMines()
print obj.getSpace()
print obj.showSpace()
print obj.isThisAMine()
obj.toggleFlag()
print obj.isFlagged()
