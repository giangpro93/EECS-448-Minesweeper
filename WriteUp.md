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


#Meeting #2 - 4:00 - 5:30

Attendees: Andre, Nathan, Colin, Michael

Location: Spahr Library Floor 2

### Accomplishments
Decided on genres of music to include - TBA
Began Front End development and assigned tasks
Resolved lab time issue



##Meeting #3 - 1:00 - 2:45

Attendees: Michael, Nathan

Location: Jayhawker Towers

###Accomplishments 
Generated rails server Successfully got aspects of MVC to work

##Meeting #4 - 2:21 - 4:00

Attendees: Tiernon, Michael, Nathan, Colin

Location: Legends Apartments

###Accomplishments 
Decided to abandon ruby on rails and use python backend
Convert ruby files to python

##Meeting #5 - 10:00 - 1:00

Attendees: Tiernon, Michael, Nathan, Andre

Locations: Legends Apartments

###Accomplishments
Rewrite executive class in python to function w/ JS
Transfer data via JSON




# Splitting Work

## Nathan
Nathan was responsible for original class design built with Ruby. This was completed by initalizing a 2D array with objects at each index, and manipulating from an executive class. Once the team decided to switch to a flask/python backend with a js/html/css frontend, Nathan converted the ruby code to python. He also did worked to debug the game by playing a lot of minesweeper. 

## Michael
Michael was responsible for original class design built with ruby. He worked especially in the Executive class, designing how the minesweeper game would run. Once the design was changed, Michael was heavily involved with designing the flask webserver.py file. Michael also recorded a lot of the documentation associated with the python code. 

## Andre
Originally Andre was responsible for launching and configureing the Rails server on Google Cloud. This was completed, but due to the teams inexperiece with the technology, we pivoted to flask/python. Andre was responsible for setting up the flask server and the connections between the back and front end. He worked on using json to allow the frontend to select a space, sending a command to the backend to modify the board.

## Colin
Colin was involved with the algorithms for placing bombs and taking the first step on the board. He defined a lot of board.py and was also heavily involved converting our ruby files to python. Colin performed a lot of debugging on the backend once the server was up and running with our js/html/css frontend. 

## Tiernon
Tiernon built and designed a majority of the frontend. Originally embedded ruby files for use with rails, he had to pivot to building them entirely out of js/html/css once we switched technologies. He also worked extensively on updating the board once the backend changed the state of the game. 
