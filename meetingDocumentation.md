Meeting #1 - 2/6/2019<br/>
Attendees: Andre, Nathan, Tiernon, Michael<br/>
Location: Spahr Library<br/>
Accomplishments:<br/>
  Figure out interaction between front and back end.<br/>
  Proclaimed decision to use ruby on rails <br/><br/>
Front-Back Interaction Plan:<br/>
* Initialization <br/>
   * From front-end <br/>
      * Board Size (x,y) <br/>
      * number of mines <br/>
   * From back-end<br/>
      * check values, throw exception if invalid <br/>
      * initialize 2D array (Board Class)<br/>
   * Start Game:<br/>
      * Front-End sends first (x,y) <br/>
      * Back generate mines <br/>
   * Step: <br/>
      * send (x,y) user choice (front)<br/>
      * refresh board (back)<br/>
   * End:<br/>
      * bools gameOver, wonGame<br/>
