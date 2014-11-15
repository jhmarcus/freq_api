from flask import Flask
from flask.ext.sqlalchemy import SQLAlchemy
import flask.ext.restless

app = Flask(__name__)
app.config.from_object('config')
db = SQLAlchemy(app)

from freq_api import models

manager = flask.ext.restless.APIManager(app, flask_sqlalchemy_db=db)
manager.create_api(models.Freq, methods=['GET'], max_results_per_page=100)
