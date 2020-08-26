from datetime import datetime

from flask import render_template
from program import app


@app.route('/')
@app.route('/index')
def index():
    return render_template('index.html', title='Template Demo', time=datetime.now())


@app.route('/100Jours')
def p100jours():
    return render_template('100Jours.html')