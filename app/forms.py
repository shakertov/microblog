from flask_wtf import FlaskForm
from wtforms import (
	StringField,
	PasswordField,
	BooleanField,
	SubmitField,
	TextAreaField
)
from wtforms.validators import (
	DataRequired,
	ValidationError,
	Email,
	EqualTo,
	Length
)
from app.models import User


class LoginForm(FlaskForm):
	username = StringField('Имя пользователя', validators=[DataRequired()])
	password = PasswordField('Пароль', validators=[DataRequired()])
	remember_me = BooleanField('Запомнить меня')
	submit = SubmitField('Войти')


class RegistrationForm(FlaskForm):
	username = StringField('Имя пользователя', validators=[DataRequired()])
	email = StringField('Email', validators=[DataRequired(), Email()])
	password = PasswordField('Пароль', validators=[DataRequired()])
	password2 = PasswordField('Повторите пароль', validators=[DataRequired(), EqualTo('password')])
	submit = SubmitField('Зарегистрироваться')

	def validate_username(self, username):
		user = User.query.filter_by(username=username.data).first()
		if user is not None:
			raise ValidationError('Данное имя уже занято.')

	def validate_email(self, email):
		user = User.query.filter_by(email=email.data).first()
		if user is not None:
			raise ValidationError('Данный email уже содержится в базе.')


class EditProfileForm(FlaskForm):
	username = StringField('Имя пользователя', validators=[DataRequired()])
	about_me = TextAreaField('Обо мне', validators=[Length(min=0, max=140)])
	submit = SubmitField('Отправить')

	def __init__(self, original_username, *args, **kwargs):
		super(EditProfileForm, self).__init__(*args, **kwargs)
		self.original_username = original_username

	def validate_username(self, username):
		if username.data != self.original_username:
			user = User.query.filter_by(username=self.username.data).first()
			if user is not None:
				raise ValidationError('Данное имя уже занято.')


class PostForm(FlaskForm):
	post = TextAreaField('Есть чем поделиться?',
		validators=[DataRequired(), Length(min=1, max=140)])
	submit = SubmitField('Отправить')


class ResetPasswordRequestForm(FlaskForm):
	email = StringField('Введите Ваш Email',
		validators=[DataRequired(), Email()])
	submit = SubmitField('Сбросить пароль')


class ResetPasswordForm(FlaskForm):
	password = PasswordField('Пароль', validators=[DataRequired()])
	password2 = PasswordField('Повторите пароль',
		validators=[DataRequired(), EqualTo('password')])
	submit = SubmitField('Сбросить пароль')

