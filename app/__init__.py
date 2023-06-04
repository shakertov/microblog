from flask import Flask
from config import Config
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from flask_login import LoginManager
from flask_mail import Mail
from flask_bootstrap import Bootstrap
import logging
from logging.handlers import RotatingFileHandler
import os

# Настройки приложения
app = Flask(__name__)
app.config.from_object(Config)

# Инициальизация БД
db = SQLAlchemy(app)
migrate = Migrate(app, db)

# Инициализация почты
mail = Mail(app)

# Инициализация управления пользователями
login = LoginManager(app)
login.login_view = 'login'
login.login_message = 'Пожалуйста, войдите, чтобы открыть эту страницу!'

# Инициализация bootstrap
bootstrap = Bootstrap(app)

if not app.debug:
	if not os.path.exists('logs'):
		os.mkdir('logs')
	file_handler = RotatingFileHandler('logs/microblog.log', maxBytes=10240, backupCount=10)
	file_handler.setFormatter(logging.Formatter(
		'%(asctime)s %(levelname)s: %(message)s in [%(pathname)s:%(lineno)d]'
	))
	app.logger.addHandler(file_handler)

	app.logger.setLevel(logging.INFO)
	app.logger.info('Microblog startup')

from app import routes, models, errors