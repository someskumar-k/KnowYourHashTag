from HashTagModules.HashTagPreProcessor import HashTagPreProcessor
from HashTagModules.ApiUtils import ApiUtils

from flask import Flask, jsonify
from flask import request
from flask_restful import Resource, Api

app = Flask(__name__)

@app.route('/api/kyht')
def getExample():
            return "Under Development!"

if __name__ == '__main__':
     app.run()