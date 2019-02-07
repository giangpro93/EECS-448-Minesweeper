require_relative 'BoardSpace'

class Board


	#initializes the board
	def initialize(rows, cols, mines)
		@m_rows = rows
		@m_cols = cols
		@m_numMines = mines
		@m_numFlags = mines

		@m_board = Array.new(rows){Array.new(cols){BoardSpace.new()}}

	end

	#returns number of rows
	def getRows()
		return @m_rows
	end
	#returns number of columns
	def getCols()
		return @m_cols
	end
	#returns number of flags
	def getFlags()
		return @m_numFlags
	end	

	#prints board to terminal(currently)
	def printBoard()
		for x in (0...@m_rows)
			for y in (0...@m_cols)
				print @m_board[x][y].getSpace()
				print " "
			end
			print "\n"
		end	
	end
	
	#shows either bomb or number of spaces around bomb
	def showBoard()
		for x in (0...@m_rows)
			for y in (0...@m_cols)
				print @m_board[x][y].showSpace()
				print " "
			end
			print "\n"
		end	
	end
	
	#takes first step, then places all bombs
	def firstStep(xpos, ypos)
		placeBombs(xpos, ypos)
		calculateNearby()
	end
	
	#places all mines around the first space stepped on
	def placeBombs(xpos,ypos)
		
		#initializes a 1D array to randomly place bombs in indicies
		maxIndex = @m_cols * @m_rows
		minesPlaced = 0
		mineIndex = Array.new(maxIndex)

		#initialize 
		for x in (0...maxIndex)
			mineIndex[x] = false
		end
		
		#randomly decides where in the array the bombs go, not on xpos,ypos.
		while (minesPlaced < @m_numMines)
			arrVal = rand(maxIndex)
			if(!mineIndex[arrVal] && arrVal != (ypos*@m_rows)+xpos)
				mineIndex[arrVal] = true
				minesPlaced +=1
			end
		end
		
		#copy 1D array into 2D array
		for i in (0...@m_rows)
			for j in (0...@m_cols)
				if (mineIndex[i+(j*@m_rows)])
					@m_board[i][j].setMine()
				end
			end
		end
	end

	def calculateNearby()
	
	end

end

