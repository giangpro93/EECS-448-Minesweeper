from flask import Flask, render_template, request, Response
import os.path
import requests
import json
from Executive import Executive

app = Flask(__name__)

#hold lists of user games
games = []
#hold current userID (increments by 1)
m_userID = 80046264357

@app.route('/', methods=['GET', 'POST'])
def main():
    """main post

    Args:
        None
    Returns:
        The HTML filess

    Raises:
        Nones
    """
    if request.method == 'POST':
        return handle_request(request.form)
    if request.method == 'GET':
        return render_template('index.html')

@app.route('/api/createBoard', methods=['POST'])
def api_newboard(self):
    s = request.form.to_dict()['json_string']
    json_acceptable_string = s.replace("'", "\"")
    d = json.loads(json_acceptable_string)
    rows = (int)(d['rows'])
    cols = (int)(d['cols'])
    mines = (int)(d['mines'])

    #add new game to list of games
    newGame = Executive(rows, cols, mines, self.m_userID)
    games.append(newGame)
    #increment userID by 1
    self.m_userID += 1
    # POST with JSON 
    return str(True)

@app.route('/api/selectSpace', methods=['POST'])
def api_selectSpace(self):
    s = request.form.to_dict()['json_string']
    # POST with JSON
    json_acceptable_string = s.replace("'", "\"")
    d = json.loads(json_acceptable_string)
    rows = (d['rows'])
    cols = (d['cols'])
    rightClick = (d['rightClick'])

    for i in self.games:
        if (games[i].getUserID() == '''passed in userID'''):
            #call either right or left click method
            if rightClick is True:
                result = games[i].rightClick(rows, cols)

                #handle different cases on right click
                if result == -1:
                    #user out of flags
                    #return unchanged board
                elif result == 0:
                    #Flag successfully planted
                    #return board
                elif result == 1:
                    #user has won - END GAME                
            else:
                result = games[i].leftClick(rows, cols)
                if result is False:
                    #user has lost - END GAME
                else
                    #return board

    

    return str(d)

def handle_request(request_data):
    # body = request_data['Body'].strip()
    return "test"


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=3001)
