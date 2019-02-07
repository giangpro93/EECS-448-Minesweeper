#BoardSpace class goes in each spot on the game board, enabling tracking of
#mine location, flags, # of spots near, etc.
class BoardSpace
	@@isMine = false
	@@isFlagged = false
	@@isHidden = true
	@@numMines = 0

	#There is a mine here, set by Board
	def setMine()
		@@isMine = true
	end
	#Someone wants to toggle flag
	def toggleFlagged()
		@@isFlagged = !@@isFlagged
	end
	#Unhides a space
	def unhide()
		@@isHidden = false
	end
	#Sets number of mines calculated by board
	def setNumMines(mines)
		@@numMines = mines
	end

	#tells you if space is a mine
	def isThisAMine()
		return @@isMine
	end
	#tells is space is flagged
	def isFlagged()
		return @@isFlagged
	end
	#returns if space is hidden
	def isThisHidden()
		return @@isHidden
	end
	#returns number of mines surrounding the space
	def getNumMines()
		return @@numMines
	end

	#defines how the space should be displayed
	def getSpace()
		if @@isHidden
			return "_"
		elsif @@isFlagged
			return "f"
		elsif !@@isMine
			return @@numMines
		else 
			return "m"
		end
	end

	#Shows either a bomb or a number of bombs around
	def showSpace()
		if @@isMine
			return "b"
		else 
			return @@numMines
		end
	end
end



