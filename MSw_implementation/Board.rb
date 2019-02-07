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
	
	#places all bombs around the first space stepped on
	def placeBombs(xpos,ypos)
		#Mark Bombs with @m_board[x][y].setMine()
	end

end

obj = Board.new(10,2,3)
obj.showBoard()

