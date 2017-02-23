"""
Flask Documentation:     http://flask.pocoo.org/docs/
Jinja2 Documentation:    http://jinja.pocoo.org/2/documentation/
Werkzeug Documentation:  http://werkzeug.pocoo.org/documentation/
This file creates your application.
"""

import os
from flask import Flask, request

import main

app = Flask(__name__)

@app.route('/log', methods=['POST'])
def log():
    params = request.get_json(force=True)
    main.main(params['company'], params['employee'], params['pw'], params['action'])
    return 'OK'


@app.errorhandler(404)
def page_not_found(error):
    """Custom 404 page."""
    return '<html><head><title>Go away</title></head></html>'


if __name__ == '__main__':
    app.run(debug=True)

