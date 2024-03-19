import time, datetime
from flask import Flask

app = Flask(__name__)

@app.route("/")
def confirm_run():
    return "api running"

@app.route("/time")
def get_current_time():
    return {"time": time.time()}

