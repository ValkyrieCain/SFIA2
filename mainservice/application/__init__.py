from flask import Flask
from flask_sqlalchemy import SQLAlchemy
import os
app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = "mysql+pymysql://root:123456@35.246.33.184/linux"#str(os.getenv('DATABASE_URI'))
app.config['SECRET_KEY'] = "7218a9143c27c16610765205a1b21cb7"#str(os.getenv('SECRET_KEY'))
db = SQLAlchemy(app)
from application import routes