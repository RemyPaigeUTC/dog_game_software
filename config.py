import os
basedir = os.path.abspath(os.path.dirname(__file__))

class Config:
    #config settings defined as class variables
    #secret key used as crypto key to generae singniture and tokens
    SECRET_KEY = os.environ.get('SECRET_KEY') or 'you-will-never-guess'
    SQLALCHEMY_DATABASE_URI = os.environ.get('DATABASE_URL') or \
                              'sqlite:///' + os.path.join(basedir, 'app.db')
    DOGS_PER_PAGE = 25