from flask import Blueprint, request, render_template, abort
import requests
from .validate import Validator, ValidationError


app1 = Blueprint('app1', __name__)


@app1.route('/quote')
def quote():

    list = []
    quotnumber = request.args.get('number')
    quotnumber = int(quotnumber)
    kanye_quotes = [requests.get('https://api.kanye.rest').json()['quote'] for x in
                    range(quotnumber)]
    return render_template("kanye_west.html", list = kanye_quotes )


@app1.route('/registration', methods = ["POST", "GET"])
def register():
    if request.method == 'POST': 
        username = request.form['username']
        password = request.form['password']
        email = request.form['email']
        val = Validator(username, password, email) 
        try:
            if val.validate():  
                abort(405)
        except ValidationError: 
            abort(406)
    return render_template('recording.html')


@app1.errorhandler(405)
def valid_accept(error):

    return f"Valid Accept"


@app1.errorhandler(406)
def valid_error(error):

    return f"Valid Error"