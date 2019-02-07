require_relative 'BoardSpace'

class Board
	@m_rows = 0
	@m_cols = 0
	@m_numMines = 0
	@m_numFlags = 0
	@m_board = []

	#initializes the board
	def initialize(rows, cols, mines)
		@m_rows = rows
		@m_cols = cols
		@m_numMines = mines
		@m_numFlags = mines 

		@m_board = Array.new(rows) {Array.new(cols)}
	
		for x in (0...@m_rows)
			for y in (0...@m_cols)
				@m_board[x][y] = BoardSpace.new()
			end
		end	
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
		for x in (0..(@m_rows-1))
			for y in (0..(@m_cols-1))
				print @m_board[x][y].getSpace()
			end
			print "\n"
		end	
	end
	
	#shows either bomb or number of spaces around bomb
	def showBoard()
		for x in (0..(@m_rows-1))
			for y in (0..(@m_cols-1))
				print @m_board[x][y].showSpace()
			end
			print "\n"
		end	
	end

	#shows flags on the board
	def showFlags()
		for x in (0..(@m_rows-1))
			for y in (0..(@m_cols-1))
				if @m_board[x][y].isFlagged()
					print "f"
				else
					print "0"
				end
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
		#hold indices of random numbers for mines
		mineIndex = []

		while mineIndex.length < @m_numMines
			
			found = false
			temp = rand(maxIndex-1)

			#check we already have the randomly generated number and then add to array
			if mineIndex.length == 0 && @m_rows * xpos + ypos != temp
				mineIndex.push(temp)
			else
				for i in (0...mineIndex.length)
					if temp == mineIndex[i] || @m_rows * xpos + ypos == temp
						found = true
					end
				end

				if found == false
					mineIndex.push(temp)
				end

			end

		end

		

		#implement bombs
		for i in (0...mineIndex.length)
			
			xVal = mineIndex[i] / @m_cols
			yVal = mineIndex[i] % @m_rows
			#@m_board[xVal][yVal].setMine()
		end

		@m_board[2][3].toggleFlagged()
		#@m_board[2][3].setNumMines(3)
	end

end

obj = Board.new(4,4,3)
obj.placeBombs(3,0)
obj.showBoard()
obj.showFlags()

