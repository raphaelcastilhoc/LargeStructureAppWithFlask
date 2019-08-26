import os

basedir = os.path.abspath(os.path.dirname(__file__))

class Config:
    DATABASE_URI = os.environ.get('LARGE_PYTHON_APP_DATABASE_URI')