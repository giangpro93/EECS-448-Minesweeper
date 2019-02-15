require_relative 'Board'

#Executive class to run the program
#Will hold a board and handle interactions with front-end
class Executive

@m_rows = 0
@m_cols = 0
@m_numMines = 0
@gameOver = false
@wonGame = false

#when game starts enter board size and number of mines
def initialize(rows, cols, mines)
    #check if values work
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

#run the game - CURRENTLY SET UP FOR CONSOLE CONTROL
def run()
    #create board
    b1 = Board.new(@m_rows, @m_cols, @m_numMines)

    #accept starting position from FRONT to initialize mines
    puts "type initial row choice, then col choice"
    rowChoice = gets.chomp.to_i
    colChoice = gets.chomp.to_i
    b1.firstStep(rowChoice,colChoice)

    #while the game is not over, allow user input
    while !@gameOver && !@wonGame
        #likely won't need to check validity of input since it's coming from the front end
        puts "enter 1 to toggle a flag or 2 to check for a mine"
        userChoice = gets.chomp.to_i

        if userChoice == 1#user wants to toggle flag
            puts "enter row, then col"
            rowChoice = gets.chomp.to_i
            colChoice = gets.chomp.to_i
            #toggle the flag for specified space - will throw exception if out of flags
            begin
                b1.toggleFlagSpace(rowChoice, colChoice)
            rescue RuntimeError => e
                puts "Insufficient number of flags"
            end

        elsif userChoice == 2#user checks for mine
            puts "enter row, then col"
            rowChoice = gets.chomp.to_i
            colChoice = gets.chomp.to_i

            #returns true to break out of while loop if a mine is hit
            @gameOver = b1.selectSpace(rowChoice,colChoice)
        end

        #check to see if user has won
        @wonGame = b1.userWin()

        #update board control file if game does not end
        b1.printBoard()
    end

    #determine win/loss
    if @gameOver
        return "You lose"
        b1.showBoard()
    end

    if @wonGame
        return "You win"
    end

end

end
