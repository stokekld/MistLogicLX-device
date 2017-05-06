from flask import render_template
from Mist.app import service

@service.route('/')
def index():
    return render_template('index.html', error={})

@service.route('/equipo')
def equipo():
    return render_template('equipo.html');
