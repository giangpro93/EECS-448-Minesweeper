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
	end
	
	#places all mines around the first space stepped on
	def placeBombs(xpos,ypos)
		#Mark Bombs with @m_board[x][y].setMine()
		maxIndex = @m_cols * @m_rows
		minesPlaced = 0
		mineIndex = Array.new(maxIndex)

		for x in (0...maxIndex)
			mineIndex[x] = false
		end
		
		while (minesPlaced < @m_numMines)
			arrVal = rand(maxIndex)
			if(!mineIndex[arrVal] && arrVal != (ypos*@m_rows)+xpos)
				mineIndex[arrVal] = true
				minesPlaced +=1
			end
		end
		
		for i in (0...@m_rows)
			for j in (0...@m_cols)
				if (mineIndex[i+(j*@m_rows)])
					@m_board[i][j].setMine()
				end
			end
		end
	end

end

obj = Board.new(20,20,20*20-1)
obj.placeBombs(12,12)
obj.showBoard()

