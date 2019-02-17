from flask import Flask, render_template, request, Response
from databaseHandler import initializeDatabase
import os.path
import requests

app = Flask(__name__)


@app.route('/', methods=['GET', 'POST'])
def main():
    if request.method == 'POST':
        return handle_request(request.form)
    if request.method == 'GET':
        return render_template('index.html')


def handle_request(request_data):
    body = request_data['Body'].strip()
    return "test"


if __name__ == '__main__':
    if not os.path.isfile('database.db'):
        initializeDatabase()
    app.run(host='0.0.0.0', port=3000)
