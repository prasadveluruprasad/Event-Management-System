# coding:utf-8
from flask import Flask
from flask_sqlalchemy import SQLAlchemy

import pymysql
pymysql.install_as_MySQLdb()

class Config(object):

    SECRET_KEY = "harryiscool"
    # database
    SQLALCHEMY_DATABASE_URI = "mysql+pymysql://root:123456789@127.0.0.1:3306/eventManager"
    SQLALCHEMY_TRACK_MODIFICATIONS = True
    UPLOAD_FOLDER = 'eventManager/static/img/'
    UPLOAD_FOLDER = UPLOAD_FOLDER

class DevelopmentConfig(Config):
    DEBUG = True

class ProductionConfig(Config):
    pass


config_map = {
    "develop": DevelopmentConfig,
    "product": ProductionConfig
}

# database
db = SQLAlchemy()


def create_app(config_name):

    app = Flask(__name__)

    # get module
    config_class = config_map.get(config_name)
    app.config.from_object(config_class)

    # init app with db
    db.init_app(app)


    return app

def create_database():

    connect = pymysql.connect(
        user = 'root',
        password = '123456789',
        db = 'eventmanager',
        host =
          '127.0.0.1',
        port = 3306,
        charset = 'utf8'
        )
    
    con = connect.cursor()
    con.execute('use eventmanager')
    con.execute('show tables;')
    tables = con.fetchall()
    
    if tables == ():
        db.drop_all()
        db.create_all()

        con.close()
        connect.close()
        return True
    
    con.close()
    connect.close()
    return False


