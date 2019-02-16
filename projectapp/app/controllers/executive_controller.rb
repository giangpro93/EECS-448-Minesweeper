require_relative 'Board'

class ExecutiveController < ApplicationController
  
  @board
  @m_rows = 0
  @m_cols = 0
  @m_numMines = 0

  #initializes board and accepts first guess, then populates board with mines
  #when game starts enter board size and number of mines
  def initialize(rows, cols, mines)
    #check if values work - !!!!THIS LIKELY NEEDS TO BE CHANGED
    if rows < 2 || cols < 2
        raise RuntimeError.new("Invalid board size")
    end
    if mines > rows * cols -1 || mines < 1
        raise RuntimeError.new("Invalid quantity of mines")
    end
    
    @m_rows = rows
    @m_cols = cols
    @m_numMines = mines
  end


  def run
    @Board = Board.new(@m_rows, @m_cols, @m_numMines)
  end


  def leftClick
    #somehow detect which square is pressed (front-end issue)
    col = 4
    row = 2
    #turn into coordinates and send here
    loser = @board.userLeftClick(col, row)

    if (loser == false)
      #check if we won
      if (@board.userWin())
        {
          #exit game with a win
        }

    else
      #end the game

    end
  end

  #flag a spot
  def rightClick
    #get coordinates from user
    col = 3
    row = 2

    #flag the spot
    begin
      @board.toggleFlagSpace(row, col)
    rescue
      #switch to error screen

    end

    #check if game is over
    if (@board.userWin())
      #Exit because user won the game
    end

  end

end


