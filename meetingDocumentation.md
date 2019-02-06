# Meeting Notes

## Meeting #1 - 2/6/2019 09:00 - 09:50

Attendees: Andre, Nathan, Tiernon, Michael

Location: Spahr Library

### Accomplishments

* Figure out interaction between front and back end.
* Proclaimed decision to use ruby on rails
* Initialization of Google Cloud project

### Front-Back Interaction Plan

* Initialization
  * From front-end
    * Board Size (x,y)
    * number of mines
  * From back-end
    * check values, throw exception if invalid
    * initialize 2D array (Board Class)
  * Start Game:
    * Front-End sends first (x,y)
    * Back generate mines
  * Step:
    * send (x,y) user choice (front)
    * refresh board (back)
  * End:
    * bools gameOver, wonGame
