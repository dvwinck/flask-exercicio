from flask import Flask, jsonify, request
from flask_restful import Api,  Resource
import json
from Morse import Morse


app = Flask(__name__)
api = Api(app)

class ToMorse (Resource):
    def get (self):
        palavra = request.args.get("palavra")
        morse = Morse()

        returningJsonFile = {
            "status" : 200,
            "msg" : "OK",
            "texto" : palavra,
            "morse": morse.toMorseCode(palavra)
        }
        return jsonify(returningJsonFile)

class ToText (Resource):
    def get (self):
        palavra = request.args.get("palavra")
        print('>>',palavra)
        morse = Morse()

        returningJsonFile = {
            "status" : 200,
            "msg" : "OK",
            "texto" : palavra,
            "morse": morse.toText(palavra)
        }
        return jsonify(returningJsonFile)

api.add_resource(ToMorse, '/tomorse')
api.add_resource(ToText, '/totext')

if __name__ == "__main__":
    app.run(debug=True)