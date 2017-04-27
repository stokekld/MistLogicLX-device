from flask import render_template
from Mist.app import service

@service.route('/')
def hello():
    return render_template('equipo.html', error={})
