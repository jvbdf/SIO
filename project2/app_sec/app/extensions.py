#Inicializar as extensões no contexto da Application Factory
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from flask_wtf.csrf import CSRFProtect


db = SQLAlchemy()

migrate = Migrate()

csrf = CSRFProtect()
