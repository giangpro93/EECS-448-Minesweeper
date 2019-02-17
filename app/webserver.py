from flask import Flask, render_template, request, Response
import os.path
import requests
import json

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
    print(request.form.to_dict()['json_string'])
    # POST with JSON 
    return str(True)

@app.route('/api/selectSpace', methods=['GET', 'POST'])
def api_selectSpace():
    print(request.form.to_dict()['json_string'])
    # POST with JSON 
    payload = [[1,2,3],[1,2,3],[-1,-1,-1]]
    r = json.dumps(payload)
    return str(r)

def handle_request(request_data):
    # body = request_data['Body'].strip()
    return "test"


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=3001)
