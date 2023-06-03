import os

basedir = os.path.abspath(os.path.dirname(__file__))

class Config(object):
	# Секретный ключ
	SECRET_KEY = os.environ.get('SECRET_KEY') or 'you-will-never-guess'
	DEBUG = True

	# Настройки БД
	SQLALCHEMY_DATABASE_URI = os.environ.get('DATABASE_URL') or \
        'sqlite:///' + os.path.join(basedir, 'app.db')
	SQLALCHEMY_TRACK_MODIFICATIONS = False

	# Настройки почты
	MAIL_SERVER = 'smtp.yandex.ru'
	MAIL_PORT = 465
	MAIL_USE_TLS = False
	MAIL_USE_SSL = True
	MAIL_USERNAME = 'freedable@yandex.ru'
	MAIL_PASSWORD = 'xcjmjhvwldftfclw'

	ADMINS = ['freedable@yandex.ru']

	# Пагинация
	POSTS_PER_PAGE = 25
