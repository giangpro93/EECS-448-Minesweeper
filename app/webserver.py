from flask import Flask, render_template, request, Response
import os.path
import requests
import json
from Board import Board

app = Flask(__name__)
myBoard = ""

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
    myBoard = Board(rows,cols,mines)
    # POST with JSON 
    return str(True)

@app.route('/api/selectSpace', methods=['POST'])
def api_selectSpace():
    s = request.form.to_dict()['json_string']
    # POST with JSON
    json_acceptable_string = s.replace("'", "\"")
    d = json.loads(json_acceptable_string)
    rows = (d['rows'])
    cols = (d['cols'])
    rightClick = (d['rightClick'])

    

    return str(d)

def handle_request(request_data):
    # body = request_data['Body'].strip()
    return "test"


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=3001)
