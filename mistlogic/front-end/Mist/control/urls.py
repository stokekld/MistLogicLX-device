from flask import render_template, jsonify
from Mist.app import service
from MistDB import dbDevice

device = dbDevice()

@service.route('/manual')
def manual():
    manual = not device.getProp('manual')
    device.setProp('manual', manual)
    return jsonify(state=True)

