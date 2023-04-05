import sqlite3
import configparser

def start():
	"""Функция создания БД и таблицы с информацией о
	пользователях"""
	#Соединение с БД
	conn = sqlite3.connect('PyBookDb.db')
	cur = conn.cursor()

	#Создание таблицы
	cur.execute("""CREATE TABLE IF NOT EXISTS users(
		ID INTEGER PRIMARY KEY,
		FirstName TEXT,
		LastName TEXT,
		Class TEXT,
		Password TEXT,
		Progress TEXT);
	""")
	conn.commit()

def add_user(user):
	"""Функция добавления нового пользовтеля"""
	#Соединение с БД
	conn = sqlite3.connect('PyBookDb.db')
	cur = conn.cursor()
	#Добавление пользователя
	cur.execute("INSERT INTO users(FirstName, LastName, Class, Password, Progress) VALUES(?, ?, ?, ?, ?);", user)
	conn.commit()

def check_user(user):
	"""Функция проверки на наличие пользовтеля в БД"""
	#Соединение с БД
	conn = sqlite3.connect('PyBookDb.db')
	cur = conn.cursor()
	#Проверка на наличие пользователя
	cur.execute("SELECT ID FROM users WHERE FirstName=? AND LastName=? AND Class=? AND Password=?", user)
	if cur.fetchone() is None:
		return 0
	else:
		return 1

def save_user(user):
	"""Функция получения ID пользователя"""
	#Соединение с БД
	conn = sqlite3.connect('PyBookDb.db')
	cur = conn.cursor()
	#Получение ID
	cur.execute("SELECT ID FROM users WHERE FirstName=? AND LastName=? AND Class=? AND Password=?", user)
	one_result = cur.fetchone()
	return one_result

def password_user(user):
	"""Функция изменения пароля"""
	#Соединение с БД
	conn = sqlite3.connect('PyBookDb.db')
	cur = conn.cursor()
	#Получение ID
	cur.execute("UPDATE users SET Password=? WHERE FirstName=? AND LastName=? AND Class=?", user)
	conn.commit()
	
def info_user(user_id):
	"""Функция получения всей информации о пользователе, по его id"""
	#Соединение с БД
	conn = sqlite3.connect('PyBookDb.db')
	cur = conn.cursor()
	#Получение информации по ID
	cur.execute("SELECT * FROM users WHERE ID=?", user_id)
	one_result = cur.fetchone()
	return one_result

def plus_progress(Progress):
	"""Функция изменения прогресса пользователя, по его id"""
	#Соединение с БД
	conn = sqlite3.connect('PyBookDb.db')
	cur = conn.cursor()
	#Замена прогресса, на новый
	cur.execute("UPDATE users SET Progress=? WHERE ID=?", Progress)
	conn.commit()

def delete_user(user_id):
	"""Функция удаления пользователя, по его id"""
	#Соединение с БД
	conn = sqlite3.connect('PyBookDb.db')
	cur = conn.cursor()
	#Замена прогресса, на новый
	cur.execute("DELETE FROM users WHERE ID=?", (user_id,))
	conn.commit()
	
def edit_user(user):
	"""Функция изменения данных пользователя, по его id"""
	#Соединение с БД
	conn = sqlite3.connect('PyBookDb.db')
	cur = conn.cursor()
	#Замена имени, на новое
	cur.execute("UPDATE users SET FirstName=? WHERE ID=?", (user[1], user[0]))
	conn.commit()
	#Замена фамилии, на новую
	cur.execute("UPDATE users SET LastName=? WHERE ID=?", (user[2], user[0]))
	conn.commit()
	#Замена класса, на новый
	cur.execute("UPDATE users SET Class=? WHERE ID=?", (user[3], user[0]))
	conn.commit()




def user_progress(Progress):
	conn = sqlite3.connect('PyBookDb.db')
	cur = conn.cursor()

	Progress = ['Ура!', 'Прогресс', 'Имя', 'Фамилия']

	#Замена прогресса, на новый
	cur.execute("UPDATE users SET Progress=? WHERE Progress=? AND FirstName=? AND LastName=?", Progress)
	conn.commit()

def output_user():
	conn = sqlite3.connect('PyBookDb.db')
	cur = conn.cursor()

	cur.execute("SELECT FirstName, LastName, Class, Progress FROM users;")
	one_result = cur.fetchall()
	return one_result
	



#user = ('Имя', 'Фамилия', 'Класс', 'Пароль', 'Прогресс')
#add_user(user)

#delete_user('1')

output_user()
#user_progress()
#info_user('2')