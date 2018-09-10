import os
from dotenv import load_dotenv

basedir = os.path.abspath(os.path.dirname(__file__))
load_dotenv(os.path.join(basedir, '.env'))


class config(object):
    SECRET_KEY = os.environ.get('SECRET_KEY') or 'you-will-never-guess'
    SQLALCHEMY_DATABASE_URI = 'mysql+pymysql://root:123456@localhost:3306/catinfo?charset=utf8'
    SQLALCHEMY_TRACK_MODIFICATIONS = False

    UPLOADED_PHOTO_DEST = os.path.dirname(os.path.abspath(__file__))+'/app/main/upload'
    # UPLOADED_PHOTO_URL = 'http://127.0.0.1:5000/'
    ALLOWED_EXTENSIONS=['txt', 'pdf', 'png', 'jpg', 'jpeg', 'gif']

    #远程链接
    hostname = '192.168.1.90'
    username = 'root'
    password = '111111'
    port = 22