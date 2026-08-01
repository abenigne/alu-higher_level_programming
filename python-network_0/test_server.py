#!/usr/bin/python3
"""Local test server mimicking the ALU python-network_0 checkpoint routes."""
from flask import Flask, request

app = Flask(__name__)


@app.route('/', methods=['GET'])
def index():
    """Route for task 0 - body size test (10 bytes)."""
    return "0123456789"


@app.route('/route_1', methods=['GET'])
def route_1():
    """Route for task 1 - returns body of a 200 response."""
    return "Route 2"


@app.route('/route_3', methods=['DELETE'])
def route_3():
    """Route for task 2 - DELETE request."""
    return "I'm a DELETE request"


@app.route('/route_4', methods=['OPTIONS', 'HEAD', 'PUT'])
def route_4():
    """Route for task 3 - lists allowed methods."""
    return "", 200, {'Allow': 'OPTIONS, HEAD, PUT'}


@app.route('/route_5', methods=['GET'])
def route_5():
    """Route for task 4 - checks custom header."""
    user_id = request.headers.get('X-HolbertonSchool-User-Id')
    if user_id == '98':
        return "Hello Holberton School!"
    return "Missing or wrong header", 403


@app.route('/route_6', methods=['POST'])
def route_6():
    """Route for task 5 - POST params."""
    email = request.form.get('email', '')
    subject = request.form.get('subject', '')
    return "POST params:\n\temail: {}\n\tsubject: {}\n".format(email, subject)


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
