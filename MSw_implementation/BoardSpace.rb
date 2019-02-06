#BoardSpace class goes in each spot on the game board, enabling tracking of
#mine location, flags, # of spots near, etc.

class BoardSpace
	@@isMine = false
	@@isFlagged = false
	@@isHidden = true
	@@Mines = 0

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
		@@Hidden = false
	end
	#Sets number of mines calculated by board
	def setMines(numMines)
		@@Mines = numMines
	end

	#tells you if space is a mine
	def thisIsAMine()
		return @@isMine
	end
	#tells is space is flagged
	def isFlagged()
		return @@isFlagged
	end

	
end

