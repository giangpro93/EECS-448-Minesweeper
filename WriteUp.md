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


# Meeting #2 - 4:00 - 5:30

Attendees: Andre, Nathan, Colin, Michael

Location: Spahr Library Floor 2

### Accomplishments
Decided on genres of music to include - TBA
Began Front End development and assigned tasks
Resolved lab time issue



## Meeting #3 - 1:00 - 2:45

Attendees: Michael, Nathan

Location: Jayhawker Towers

### Accomplishments 
Generated rails server Successfully got aspects of MVC to work

## Meeting #4 - 2:21 - 4:00

Attendees: Tiernon, Michael, Nathan, Colin

Location: Legends Apartments

### Accomplishments 
Decided to abandon ruby on rails and use python backend
Convert ruby files to python

## Meeting #5 - 10:00 - 1:00

Attendees: Tiernon, Michael, Nathan, Andre

Locations: Legends Apartments

### Accomplishments
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




# Challenges

## Ruby on Rail
Well, it turns out two weeks is not long enough for us to learn a new programming language and web framework, and produce a MVP capable of playing minesweeper. Tragic. None of us had experience with any sort of system that revolved around Model/View/Controller (most of us had never heard of MVC before). After a week and 5 days of toiling in Rails, we gave up on Ruby on Rails for technologies we were more familiar with. 

## Time Crunch
Saturday night we decided to use python. So it was all hands on deck for the last day or so of our project. And we're not one for pygame , so we decided to change our embedded ruby html files to normal html files and build a backend using flask. The biggest challenge on this aspect was the time crunch because most of us were familiar with flask, python, and html/css/js.

## HackKU
We spent our entire last weekend participating in/winning HackKU. This took up around 48 hours of prime coding time that could have been spent building a Ruby on Rails minesweeper. But hey, three of our five teammembers won shiny new VR goggles. 

## Nathan and GitHub
GitHub is tricky for our friend Nathan. He couldn't figure out how to get listed as a contributer. And even then, he somehow managed to commit under three different names. (Nichols Basement, Nathan Nichols, and natenichols).

## Colin and GitHub
Colin developed on Nathan's linux machine, meaning some commits under Nathan Nichols were Colin's work.

## Development
Getting the front and back end to communicate using JSON has proven to be difficult.




# Features Left Out

## Ruby on Rails
It's on here twice. Ruby on Rails was scrapped for reasons previously mentioned.

## FirstStep
Originally we were going to remove all mines within a one space radius of the starting spot, similar to windows minesweeper. However this did not meet the criterea presented to us. So instead, mines are generated randomly except on the first space clicked, so you can have (rows*cols)-1 mines on a board. 

## Appearance
We were planning on using images/designs on each space to make the game more presentable, but that went out the window when we were short on time. The current version just uses text over spaces generated using html/css/js.


# Changes We Would Make

## Making up our Mind
The late swap to Python and Flask threw everyone into a panic. It would have been preferable for our team to have decided on this earlier in the week. We were making enough progress on Ruby on Rails that we were hesitant to scrap all the work we had done. 

## Upon Failure
We do not show the full state of the board upon losing the game. This would be the next functionality that we would add. There is currently a function in BoardSpace that returns either a number or a b (for mine).

# Summary
All in all we are happy with the finished product we will be presenting. At t-minus 2 hours til the due date, we are playing games full games of minesweeper.



## Works Cited
### Technologies
* Python
	* Flask
	* JSON library
	* Random library

* HTML/CSS/JS
	* JQuery

* (Hopefully) Google Cloud Platform


### Sources
* YouTube
	*Cody Seibert Minesweeper video

* Stack Overflow (obviously)





