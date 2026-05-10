import os

class Config:
    SECRET_KEY = 'secret123'
    SQLALCHEMY_DATABASE_URI = 'sqlite:///univoice.db'
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    UPLOAD_FOLDER = os.path.join('static', 'uploads')