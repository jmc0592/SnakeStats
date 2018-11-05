import os
import json
import pdb

import config
from utility.converter import RequestConverter

from flask import Flask, request, jsonify
import pymongo

app = Flask(__name__)
dirname = os.path.dirname(__file__)

db_client = pymongo.MongoClient(config.mongodb['server'], config.mongodb['port'])
db = db_client[config.mongodb['name']]

@app.route('/')
def index():
    # TODO: Ew. Do something better.
    with open(os.path.join(dirname, 'ui/html/index.html'), 'r') as f:
        return f.read()

@app.route('/feeding_stats', methods=['POST', 'GET'])
def feeding_stats():
    if request.method == 'POST':
        if config.stubApi:
            return jsonify({'result': 1, 'message': 'Stub'})
        requestData = request.data.decode()
        if config.debug:
            print(requestData)

        try:
            feeding = json.loads(requestData)
            feeding = RequestConverter.convertFromFormDataToDictFormat(feeding)
            db.feedings.insert_one(feeding)
        except:
            return _createFailureResponse()
        return jsonify({'result': 0, 'message': 'Data added successfully'})

    elif request.method == 'GET':
        if config.stubApi:
                return jsonify({"message": "Stub" "feedName" : "MyDude", "feedDate" : "2018-11-02", "feedTime" : "2240", "feedFood" : "fuzzy", "feedSubstrate" : "aspen", "feedEnclosure" : "10G glass", "feedTemp" : "90" })
        if config.debug:
            print(request.args)

        try:
            feedings = [fr for fr in db.feedings.find(projection={'_id': False})]
        except:
            return _createFailureResponse()
        return jsonify(feedings)

def _createFailureResponse(message='Failure', statusCode=500):
    failureDict = {'result': -1}
    failureDict['message'] = message
    response = jsonify(failureDict)
    response.status = statusCode

    return response

if __name__ == '__main__':
    app.run(debug=config.debug)