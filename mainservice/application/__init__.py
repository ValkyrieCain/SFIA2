from flask import Flask
import os
app = Flask(__name__)
app.config['SECRET_KEY'] = str(os.getenv('SECRET_KEY'))
from application import routes