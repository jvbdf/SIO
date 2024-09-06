import os

basedir = os.path.abspath(os.path.dirname(__file__))

class Config:
    SECRET_KEY = '@D3ti_SHop2024%('
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    SQLALCHEMY_DATABASE_URI = f'sqlite:///{os.path.join(basedir, "database.db")}'
    UPLOAD_FOLDER = 'static/img/profile_pics' 
    
    MAX_CONTENT_LENGTH = 1 * 1024 * 1024  # 1 MB
    
    RECAPTCHA_SITE_KEY = '6LcT7DcqAAAAAF7nPx7GtBgrt1Yv7yhAr550CgEp'
    RECAPTCHA_SECRET_KEY = '6LcT7DcqAAAAAA1OAO3HFCwz5PhJWnrgQFC0susN'

