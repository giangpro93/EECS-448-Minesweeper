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

		@m_board = Array.new(rows) {Array.new(rows,cols)}
	
		for x in (0..(@m_rows-1))
			for y in (0..(@m_cols-1))
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
	
	#takes first step, then places all bombs
	def firstStep(xpos, ypos)
		placeBombs(xpos, ypos)
	end
	
	#places all mines around the first space stepped on
	def placeBombs(xpos,ypos)
<<<<<<< HEAD
		#Mark Bombs with @m_board[x][y].setMine()
=======
		maxIndex = @m_cols * @m_rows
		mineIndex = []

		while mineIndex.length < maxIndex
			found = false
			temp = rand(maxIndex-1)
			#check we already have the randomly generated number
			#this line is likely redundant, I'll need to test in a real environment
			if mineIndex.length == 0 then 
				mineIndex.push(temp)
			else	
				for i in (0...mineIndex.length -1)
					if mineIndex[i] == temp then
						found = true
					end
				end

				if found==false then
					mineIndex.push(temp)
				end
			end
		end

		#implement bombs
		for i in (0...mineIndex.length-1)
			xVal = mineIndex[i] % @m_rows
			yVal = mineIndex[i] / @m_cols
			@m_board[xVal][yVal].setMine()
		end

>>>>>>> df18bff81ce538142cfc7173bb48854974ea89a9
	end

end

obj = Board.new(10,2,3)
obj.showBoard()

