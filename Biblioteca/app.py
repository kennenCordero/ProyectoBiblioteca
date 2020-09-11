from flask import Flask
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)

app.config['SECRET_KEY']='0123password'
app.config['SQLALCHEMY_DATABASE_URI']='sqlite:///database/library.db'
db=SQLAlchemy(app)

from controllers.controller import *

if __name__ == '__main__':
    app.run(debug=True)