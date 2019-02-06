class Board
	@@m_rows = 0
	@@m_cols = 0
	@@m_numMines = 0
	@@m_numFlags = 0
	@@m_board = []

	def initialize(rows, cols, mines)
		m_rows = rows
		m_cols = cols
		m_numMines = mines
		m_numFlags = mines
		m_board = Array.new(rows){Array.new(cols)}
	end


	
end

