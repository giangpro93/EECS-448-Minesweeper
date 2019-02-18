from flask import Flask, render_template, request, Response
import os.path
import requests
import json
from Executive import Executive


#hold lists of user games
games = []


app = Flask(__name__)


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
def api_newboard():
    s = request.form.to_dict()['json_string']
    json_acceptable_string = s.replace("'", "\"")
    d = json.loads(json_acceptable_string)
    rows = (int)(d['rows'])
    cols = (int)(d['cols'])
    mines = (int)(d['mines'])
    userID = (int)(d['userID'])
    #add new game to list of games
    newGame = Executive(rows, cols, mines, userID)
    games.append(newGame)
    print(games[0].getUserID())
    # POST with JSON 
    return str(True)

@app.route('/api/selectSpace', methods=['POST'])
def api_selectSpace():
    s = request.form.to_dict()['json_string']
    # POST with JSON
    json_acceptable_string = s.replace("'", "\"")
    d = json.loads(json_acceptable_string)
    rows = (int)(d['rows'])
    cols = (int)(d['cols'])
    userID = (int)(d['userID'])
    rightClick = (d['rightClick'] == "true")
    print(rightClick)
    for i in games:
        if (i.getUserID() == userID):
            #call either right or left click method
            if rightClick is True:
                result = i.rightClick(rows, cols)

                #handle different cases on right click
                if result == -1:
                    #user out of flags
                    return str(i.getJson)
                elif result == 0:
                    #Flag successfully planted
                    return str(i.getJson)
                elif result == 1:
                    return "WINNER"                
            else:
                result = i.leftClick(rows, cols)
                if result is False:
                    print("LOSER")
                else:
                    return str(i.getJson)

    



def handle_request(request_data):
    # body = request_data['Body'].strip()
    return "test"


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=3001, debug=True)
