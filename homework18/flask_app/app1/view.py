from flask import Blueprint
from datetime import datetime
import requests


app1 = Blueprint('app1',__name__)


@app1.route('/times')
def times():
    times = datetime.now().isoformat()
    return f"{str(times)}"

@app1.route('/quote')
def quote():
    r = requests.get('https://api.kanye.rest')
    return f"{r.json()['quote']}"