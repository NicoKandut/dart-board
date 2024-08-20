from flask import Flask, render_template
from shared_memory_dict import SharedMemoryDict
import atexit
import os

shm_data: SharedMemoryDict = SharedMemoryDict(name="data", size=128)
app = Flask(__name__, template_folder=os.getcwd() + "/poc/webservice/templates", static_folder=os.getcwd() + "/poc/webservice/static")

def cleanup():
    shm_data.shm.close()
    shm_data.shm.unlink()
    del shm_data

data = {
    "score": 0,
    "remainding": 0,
    "player": 0,
    "game_state": 0,
    "last_dart_x_pos": 0,
    "last_dart_y_pos": 0 
    }

for key in data:
    shm_data[key] = 0

atexit.register(cleanup)

@app.route("/")
def hello_world():
    return render_template('_base.html', data=shm_data)