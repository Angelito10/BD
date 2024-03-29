import os 
from sqlalchemy import create_engine
import urllib

class Config(object):
    SECRET_KEY = 'MY_SECRET_KEY'
    SESSION_COOKIE_SECURE = False


class DevelopmetConfig(Config):
    DEBUG = True
    SQLALCHEMY_DATABASE_URI = 'mysql+pymysql://1234:root@127.0.0.1/idgs801'
    SQLALCHEMY_TRACK_MODIFICATION = False