import os
from flask import Flask, request
from timewatch import TimeWatchClient

app = Flask(__name__)


@app.route('/punch-in', methods=['POST'])
def punch_in():
    body = request.get_json(force=True)

    company = body['company']
    employee_id = body['employeeId']
    password = body['password']

    client = TimeWatchClient(company, employee_id, password)
    client.login()
    client.punch_in()

    return ':+1:'


@app.route('/punch-out', methods=['POST'])
def punch_out():
    body = request.get_json(force=True)

    company = body['company']
    employee_id = body['employeeId']
    password = body['password']

    client = TimeWatchClient(company, employee_id, password)
    client.login()
    client.punch_out()

    return ':+1:'


@app.errorhandler(404)
def page_not_found(error):
    return '<html><head><title>...</title></head></html>'


if __name__ == '__main__':
    app.run(debug=True)
