from flask import render_template
from Mist.app import service

@service.route('/manual')
def manual():
    return "hola"

