from flask import Flask, render_template, request, Response
from Executive import Executive
import os.path
import requests
import json

app = Flask(__name__)

#hold lists of user games
games = []
#hold current userID (increments by 1)
userID = 80046264357


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
    print(request.form.to_dict()['json_string'])

    #add new game to list of games
    newGame = Executive('''rows, cols, numMines''', userID)
    games.append(newGame)
    #increment userID by 1
    userID += 1

    # POST with JSON
    return str(True)


@app.route('/api/selectSpace', methods=['GET', 'POST'])
def api_selectSpace(self):
    print(request.form.to_dict()['json_string'])
    # POST with JSON
    payload = [[1, 2, 3], [1, 2, 3], [-1, -1, -1]]
    r = json.dumps(payload)

    for i in self.games:
        if (games[i].getUserID() == '''passed in userID'''):
            #call either right or left click method
            print(i)

    return str(r)


def handle_request(request_data):
    # body = request_data['Body'].strip()
    return "test"


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=3001)
