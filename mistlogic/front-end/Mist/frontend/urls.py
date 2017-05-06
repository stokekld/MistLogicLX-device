from flask import render_template
from Mist.app import service
from MistDB import dbDevice

device = dbDevice()

@service.route('/')
def index():
    return render_template('index.html', error={})

@service.route('/equipo')
def equipo():
    manual = ""
    if device.getProp('manual'):
        manual = "checked"
    return render_template('equipo.html', manual = manual);
