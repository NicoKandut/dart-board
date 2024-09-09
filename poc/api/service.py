from flask import Flask
from flask_restful import Resource, Api
from multiprocessing import Array

import logging
log = logging.getLogger('werkzeug')
log.setLevel(logging.ERROR)

app = Flask("api-service")
api = Api(app)

class Data(Resource):
  def get(self):
    last_score = shm[0]
    last_x = shm[1]
    last_y = shm[2]
    valid = shm[3]
    return {'last_score': last_score,
            'last_x': last_x,
            'last_y': last_y,
            'valid': valid
            }

api.add_resource(Data, '/last_arrow')

def main(shm_a: Array):
  global shm
  shm = shm_a
  app.run() # DONT start it with debug=True. wired behavior ^^