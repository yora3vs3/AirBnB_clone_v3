#!/usr/bin/python3
""" Script that runs Flask, imports Blueprint """
from models import storage
from api.v1.views import app_views
from os import getenv
from flask import Flask, render_template, make_response, jsonify
from flask_cors import CORS
from flasgger import Swagger
from flasgger.utils import swag_from


app = Flask(__name__)
app.register_blueprint(app_views)
CORS(app, resources={r"/api/v1/*": {"origins": "0.0.0.0"}})


@app.teardown_appcontext
def teardown_session(exception):
    """ calls storage.close """
    storage.close()


@app.errorhandler(404)
def not_found(error):
    """Handler for 404 errors"""
    return make_response(jsonify({"error": "Not found"}), 404)


if __name__ == '__main__':
    host = getenv("HBNB_API_HOST") if getenv("HBNB_API_HOST") else "0.0.0.0"
    port = getenv("HBNB_API_PORT") if getenv("HBNB_API_PORT") else 5000
    app.run(host=host, port=port, threaded=True)
