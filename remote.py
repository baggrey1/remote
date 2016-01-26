# API for controlling everything using an IR blaster
# Date: 1/25/2016
# Authon: Brian Aggrey
from flask import (Flask, request)
import subprocess

app = Flask(__name__)

@app.route("/send_once/")
# This route accepts a get request containing params
# for sending an IR code once
def send_once():
	remote = request.args.get('remote', '')
	code = request.args.get('code', '')
	
	subprocess.call(["irsend", "send_once", remote, code])
	return 'sent once '+ remote + ' ' + code, 200

if __name__ == "__main__":
	app.run(host='0.0.0.0', port=4444, debug=True)