import streamlit as st
from flask import Flask
from flask_restful import Resource, Api

app = Flask(__name__)
api = Api(app)

class DissolvedOxygen(Resource):
    def get(self):
        return {
            "teste": "teste"
        }

api.add_resource(DissolvedOxygen, "/do")

if __name__ == '__main__':
    app.run(debug=True)