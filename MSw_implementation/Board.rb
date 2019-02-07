class Board
	@m_rows = 0
	@m_cols = 0
	@m_numMines = 0
	@m_numFlags = 0
	@m_board = []

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

	#prints board to terminal(currently)
	def printBoard()
		for x in (0..(@m_rows-1))
			for y in (0..(@m_cols-1))
				print @m_board[x][y].getSpace()
			end
			print "\n"
		end	
	end
end


