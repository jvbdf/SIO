import os

basedir = os.path.abspath(os.path.dirname(__file__))

class Config:
    SECRET_KEY = '@D3ti_SHop2024%('
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    SQLALCHEMY_DATABASE_URI = f'sqlite:///{os.path.join(basedir, "database.db")}'
    # UPLOAD_FOLDER = 'static/img/profile_pics'
    UPLOAD_FOLDER = 'static/img/profile_pics' 
