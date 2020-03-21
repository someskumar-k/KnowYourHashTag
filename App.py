from HashTagModules.HashTagPreProcessor import HashTagPreProcessor
from HashTagModules.ApiUtils import ApiUtils
from flask import Flask, request, jsonify
import json as json
from flask_restful import Resource, Api
#from sqlalchemy import create_engine
from json import dumps


app = Flask(__name__)
api = Api(app)

class InstaHash(Resource):
    def get(self):
        data = 'storiesbysrd'#request.args['tagName']
        apidata = ApiUtils().getJsonDataForHashTag(key=data)
        data = HashTagPreProcessor(json_data=apidata,hash_tag=data).getProcessedHashTagData()
        resp = jsonify(str(data))
        return resp

api.add_resource(InstaHash, '/') # Route_1
if __name__ == '__main__':
     app.run(port='5000', debug=True)