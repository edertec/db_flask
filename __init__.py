from flask import Flask
from config import DevelopmentConfig
from database import db

app = Flask(__name__)
app.config.from_object(DevelopmentConfig)
db.init_app(app)
