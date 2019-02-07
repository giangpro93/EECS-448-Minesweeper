class Board
	@m_rows = 0
	@m_cols = 0
	@m_numMines = 0
	@m_numFlags = 0
	@m_board = []

	def initialize(rows, cols, mines)
		m_rows = rows
		m_cols = cols
		m_numMines = mines
		m_numFlags = mines
		m_board = Array.new(rows){Array.new(cols)}
		#initialize all spots in board to have a boardspace, may not be necessary
		#set mines
		for i in (0...m_rows)
			for j in (0...m_cols)
				m_board[i][j] = boardspace.new
			end
		end
	end

	#initalize all board spaces by setting mines around the users' starting spot
	def run(startingX, startingY)
		#set mines
		for i in (0...m_rows)
			for j in (0...m_cols)
				if _____ then
					m_board
				

			end
		end

	end

	
end

