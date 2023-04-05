import tkinter as tk
import tkinter.ttk as ttk
import subprocess
import keyboard
import time
import configparser
import os.path
import tkinter.messagebox as mb
import PyBookDataBaseControl as pydb
import PyBookTexts as pytx

"""Внешний вид программы"""
image_window_light = 'theme/image_window_light.png'
image_window_dark = 'theme/image_window_dark.png'

reg_window_light = 'theme/reg_window_light.png'
reg_window_dark = 'theme/reg_window_light.png'

work_window_light = 'theme/main_window_light.png'
work_window_dark = 'theme/main_window_dark.png'

bg_light = '#F5F5F5'
bg_dark = '#252A34'

#Сохраняем ID
global global_user_id
global_user_id = 0

"""Окна программы"""

#Окно-заглушка
def create_image_window():
	"""Создание окна-заглушки"""
	global image_window
	image_window = tk.Tk()
	image_window.title("PythonBook")

	"""Начало центрирования окна"""
	app_width = 510
	app_height = 310

	screen_width = image_window.winfo_screenwidth()
	screen_height = image_window.winfo_screenheight()

	x = (screen_width / 2) - (app_width / 2)
	y = (screen_height / 2) - (app_height / 2)

	image_window.geometry(f'{app_width}x{app_height}+{int(x)}+{int(y)}')
	"""Конец центрирования окна"""

	image_window.overrideredirect(True)
	image_window.attributes('-topmost', True) #Поверх всех окон

	"""Внешний вид окна загрузки"""
	image_download_window = tk.PhotoImage(
		file = image_window_light)
	download_window_lb = tk.Label(image = image_download_window).place(
		x = 0, y = 0, width = 510, height = 310)

	"""Надпись <Python> """
	python_lb = tk.Label(image_window, text = 'Python', 
		font = ('Comic Sans MS', 34, 'underline'), fg = '#FF2E63', bd = 0, 
		bg = bg_light).place(x = 155, y = 10, width = 200, height = 70)

	"""Информация об авторе"""
	author_lb = tk.Label(image_window, text = '© Федоров', 
		font = ('Comic Sans MS', 12), fg = '#FF2E63', bd = 0, bg = bg_light
		).place(x = 63, y = 269, width = 83, height = 20)

	"""Стартовая функция, которая определяет, была ли создана 
	учетная запись пользователя или нет.
	Если была - открывает окно авторизации,
	если нет - открывает окно регистрации"""
	def _start_():
		"""Проверка наличия файла конфигурации
		если он есть, то ничего не делаем, а если его нет,
		то создаём новый"""
		if os.path.exists('Config.ini'):
			pass
		else:
			config = configparser.ConfigParser()
			config.add_section("Registration_User")
			config.set("Registration_User", "Registration", "off")
			#Сюда сохраняем нужно ли запомнить данные о входе
			config.set("Registration_User", "Password_on", "[None]")
			config.set("Registration_User", "User_ID", "[None]")
			config.set("Registration_User", "Version", "Pybook 1v11.11.2022")
		
			with open('Config.ini', "w+") as config_file:
				config.write(config_file)
			
		"""Читаем файл конфигурации, нам нужно узнать, 
		регистрировался ли пользователь или же нет"""		
		config = configparser.ConfigParser()
		config.read('Config.ini')
		
		global user
		user = config.get("Registration_User", "Registration")

		if user == 'off':
			"""Скрываем окно-заглушку и переходим 
			в окно регистрации"""
			image_window.withdraw()
			create_registration_window()
		else:
			"""Скрываем окно-заглушку и переходим 
			в окно авторизации"""
			image_window.withdraw()
			create_authorization_window()

	"""Запуск функции, которая отвечает за начальные задачи программы"""
	image_window.after(2000, _start_)
	image_window.mainloop()

#Окно регистрации
global create_registration_window
def create_registration_window():
	"""Создание окна регистрации"""
	registration_window = tk.Toplevel()
	registration_window.title("PyBook Регистрация")
	registration_window.resizable(width = False, height = False)

	"""Начало центрирования окна"""
	app_width = 310
	app_height = 510

	screen_width = registration_window.winfo_screenwidth()
	screen_height = registration_window.winfo_screenheight()

	x = (screen_width / 2) - (app_width / 2)
	y = (screen_height / 2) - (app_height / 2)
	y -= 20

	registration_window.geometry(f'{app_width}x{app_height}+{int(x)}+{int(y)}')
	"""Конец центрирования окна"""

	registration_window.iconbitmap('icons/ico.ico')
	registration_window.attributes('-topmost', True) #Поверх всех окон

	"""Внешний вид окна регистрации"""
	image_registration_window = tk.PhotoImage(
		file = reg_window_light)
	registration_window_lb = tk.Label(registration_window, 
		image = image_registration_window
		).place(x = 0, y = 0, width = 310, height = 510)
	#Для красоты
	label_lb1 = tk.Label(registration_window, bg = '#FF2E63'
		).place(x = 10, y = 5, width = 290, height = 480)
	label_lb2 = tk.Label(registration_window, bg = '#F5F5F5'
		).place(x = 12, y = 7, width = 286, height = 476)
	

	#Текст - название формы
	label_name_frame = tk.Label(registration_window, text = 'Регистрация',
		bg = '#F5F5F5', font = ('Comic Sans MS', 18, 'underline'),
		fg = '#FF2E63')
	label_name_frame.place(x = 50, y = 9, width = 210, height = 48)

	#Текст - Имя
	name_lb = tk.Label(registration_window, text = 'Имя', bg = '#F5F5F5',
		font = ('Comic Sans MS', 16, 'underline'), anchor='w')
	name_lb.place(x = 34, y = 60, width = 240, height = 30)
	#Поле ввода текста
	name_tx = ttk.Entry(registration_window, justify = 'center',
		font = ('Comic Sans MS', 12))
	name_tx.place(x = 34, y = 90, width = 240, height = 25)
	
	#Текст - Фамилия
	second_name_lb = tk.Label(registration_window, text = 'Фамилия', 
		bg = '#F5F5F5', font = ('Comic Sans MS', 16, 'underline'),
		anchor='w')
	second_name_lb.place(x = 34, y = 120, width = 240, height = 30)
	#Поле ввода текста
	second_name_tx = ttk.Entry(registration_window, justify = 'center',
		font = ('Comic Sans MS', 12))
	second_name_tx.place(x = 34, y = 150, width = 240, height = 25)

	#Текст - Пароль
	password_lb = tk.Label(registration_window, text = 'Пароль', 
		bg = '#F5F5F5', font = ('Comic Sans MS', 16, 'underline'), 
		anchor='w')
	password_lb.place(x = 34, y = 180, width = 240, height = 30)
	#Поле ввода текста
	global password_tx
	password_tx = ttk.Entry(registration_window, justify = 'center',
		font = ('Comic Sans MS', 12), show = "*")
	password_tx.place(x = 34, y = 210, width = 200, height = 25)

	#Текст - Группа или Класс, если нет - пропуск
	group_lb = tk.Label(registration_window, text = 'Группа/Класс', 
		bg = '#F5F5F5',	font = ('Comic Sans MS', 16, 'underline'), 
		anchor='w')
	group_lb.place(x = 34, y = 240, width = 240, height = 30)
	#Поле ввода текста
	group_tx = ttk.Entry(registration_window, justify = 'center',
		font = ('Comic Sans MS', 12))
	group_tx.place(x = 34, y = 270, width = 240, height = 25)

	"""Функции для кнопочек"""
	def open_password():
		"""Показывает пароль"""
		eye_off_bt_im.place_forget()
		eye_on_bt_im.place(x = 240, y = 206)
		password_tx['show'] = ""

	def close_password():
		"""Скрывает пароль"""
		eye_off_bt_im.place(x = 240, y = 206)
		eye_on_bt_im.place_forget()
		password_tx['show'] = "*"

	def registration_user_on():
		"""Регистрирует пользователя в системе"""
		#Открываем .ini для взаимодействия с ним
		config = configparser.ConfigParser()
		config.read('Config.ini')

		user = []

		#Сюда сохраняем регистрировался ли пользователь
		config.set("Registration_User", "Registration", "on")
		#Сюда сохраняем имя
		name_user = name_tx.get()
		if name_tx.index("end") == 0:
			name_lb['fg'] = '#FF2E63'
			name_lb['text'] = 'Имя*'
			return 'break'
		if ' ' in name_user:
			return 'break'
		user.append(name_user)
		#Сюда сохраняем фамилию
		second_name_user = second_name_tx.get()
		if second_name_tx.index("end") == 0:
			second_name_lb['fg'] = '#FF2E63'
			second_name_lb['text'] = 'Фамилия*'
			return 'break'
		if ' ' in second_name_user:
			return 'break'
		user.append(second_name_user)
		#Сюда сохраняем класс/группу
		group = group_tx.get()
		if group_tx.index("end") == 0:
			group_lb['fg'] = '#FF2E63'
			group_lb['text'] = 'Группа/Класс*'
			return 'break'
		if ' ' in group:
			return 'break'
		user.append(group)
		#Сюда сохраняем пароль
		password = password_tx.get()
		if password_tx.index("end") == 0:
			password_lb['fg'] = '#FF2E63'
			password_lb['text'] = 'Пароль*'
			return 'break'
		if ' ' in password:
			return 'break'
		user.append(password)
		#Сюда сохраняем прогресс
		user.append('0')
		#Сюда сохраняем нужно ли запомнить данные о входе
		password_on_or_off = str(var.get())
		config.set("Registration_User", "Password_on", 
			str(password_on_or_off))
	
		with open('Config.ini', "w") as config_file:
			config.write(config_file)

		#Записываем информацию в БД
		pydb.add_user(user)

		#Сохранение информации о пользователе
		if str(password_on_or_off) == '1':
			config = configparser.ConfigParser()
			config.read('Config.ini')
			user.pop(4)
			user_id = pydb.save_user(user)
			user_id = user_id[0]
			config.set("Registration_User", "User_ID", str(user_id))
			with open('Config.ini', "w") as config_file:
				config.write(config_file)

		#Сохраняем ID
		user_id = pydb.save_user(user)
		global global_user_id
		global_user_id = user_id[0]

		#Закрываем окно регистрации
		registration_window.destroy()
		#Открываем главное окно программы
		create_work_window()

	def on_closing():
		"""Ловим закрытие окна верхнего уровня и 
		закрываем всю программу"""
		image_window.destroy()
	#Протокол закрытия, его и ловим
	registration_window.protocol("WM_DELETE_WINDOW", on_closing)

	def close_reg_window():
		#Закрываем окно регистрации
		registration_window.destroy()


	#Кнопка показать пароль
	global image_eye_off, eye_off_bt_im
	image_eye_off = tk.PhotoImage(
		file = 'icons/eye_on.png')

	eye_off_bt_im = tk.Button(registration_window, bd = 0, bg = '#F5F5F5', 
		image = image_eye_off, 
		activebackground = '#F5F5F5', command = open_password)
	eye_off_bt_im.place(x = 240, y = 206)

	#Кнопка скрыть пароль
	global image_eye_on, eye_on_bt_im
	image_eye_on = tk.PhotoImage(
		file = 'icons/eye_off.png')

	eye_on_bt_im = tk.Button(registration_window, bd = 0, bg = '#F5F5F5', 
		image = image_eye_on, 
		activebackground = '#F5F5F5', command = close_password)
	eye_on_bt_im.place_forget()

	#Кнопка - запомнить
	var = tk.IntVar()
	remember_cbt = ttk.Checkbutton(registration_window, 
		text = 'on', variable = var).place(x = 34, y = 300)
	remember_bt = tk.Button(registration_window, bd = 0, bg = '#F5F5F5', 
		font = ('Comic Sans MS', 12, 'underline'), 
		text = 'Запомнить меня', activeforeground = '#08D9D6',
		activebackground = '#F5F5F5')
	remember_bt.place(x = 49, y = 298, height = 22)
	
	#Кнопка - Регистрация
	global image_reg
	image_reg = tk.PhotoImage(
		file = 'icons/ok.png')

	reg_bt_im = tk.Button(registration_window, bd = 0, bg = '#F5F5F5', 
		image = image_reg, 
		activebackground = '#F5F5F5', command = registration_user_on)
	reg_bt_im.place(x = 38, y = 330)

	reg_bt = tk.Button(registration_window, bd = 0, bg = '#F5F5F5', 
		font = ('Comic Sans MS', 12, 'underline'), 
		text = 'Зарегистрироваться', fg = '#FF2E63', 
		command = registration_user_on,
		activebackground = '#F5F5F5', activeforeground = '#08D9D6')
	reg_bt.place(x = 84, y = 336)

	#Кнопка - Выход
	global image_exit
	image_exit = tk.PhotoImage(
		file = 'icons/no.png')

	exit_bt_im = tk.Button(registration_window, bd = 0, bg = '#F5F5F5', 
		image = image_exit, 
		activebackground = '#F5F5F5', command = on_closing)
	exit_bt_im.place(x = 38, y = 380)

	exit_bt = tk.Button(registration_window, bd = 0, bg = '#F5F5F5', 
		font = ('Comic Sans MS', 12, 'underline'), 
		text = 'Выход', fg = '#FF2E63', command = on_closing,
		activebackground = '#F5F5F5', activeforeground = '#08D9D6')
	exit_bt.place(x = 84, y = 388)
	
	#Кнопка - Вход в аккаунт
	aut_bt = tk.Button(registration_window, bd = 0, bg = '#F5F5F5', 
		font = ('Comic Sans MS', 12, 'underline'), 
		text = 'У меня уже есть аккаунт', activeforeground = '#08D9D6',
		activebackground = '#F5F5F5', command = lambda: (
			close_reg_window(), create_authorization_window()))
	aut_bt.place(x = 60, y = 445)

	registration_window.mainloop()

#Окно авторизации
global create_authorization_window
def create_authorization_window():
	"""Создание окна авторизации"""
	authorization_window = tk.Toplevel()
	authorization_window.title("PyBook Вход")
	authorization_window.resizable(width = False, height = False)

	"""Начало центрирования окна"""
	app_width = 310
	app_height = 510

	screen_width = authorization_window.winfo_screenwidth()
	screen_height = authorization_window.winfo_screenheight()

	x = (screen_width / 2) - (app_width / 2)
	y = (screen_height / 2) - (app_height / 2)
	y -= 20

	authorization_window.geometry(f'{app_width}x{app_height}+{int(x)}+{int(y)}')
	"""Конец центрирования окна"""

	authorization_window.iconbitmap('icons/ico.ico')
	authorization_window.attributes('-topmost', True) #Поверх всех окон

	"""Внешний вид окна авторизации"""
	image_authorization_window = tk.PhotoImage(
		file = reg_window_light)
	authorization_window_lb = tk.Label(authorization_window, 
		image = image_authorization_window
		).place(x = 0, y = 0, width = 310, height = 510)
	#Для красоты
	label_lb1 = tk.Label(authorization_window, bg = '#FF2E63'
		).place(x = 10, y = 5, width = 290, height = 480)
	label_lb2 = tk.Label(authorization_window, bg = '#F5F5F5'
		).place(x = 12, y = 7, width = 286, height = 476)
	

	#Текст - название формы
	label_name_frame = tk.Label(authorization_window, text = 'Вход в аккаунт',
		bg = '#F5F5F5', font = ('Comic Sans MS', 18, 'underline'),
		fg = '#FF2E63')
	label_name_frame.place(x = 50, y = 9, width = 210, height = 48)

	#Текст - Имя
	name_lb = tk.Label(authorization_window, text = 'Имя', bg = '#F5F5F5',
		font = ('Comic Sans MS', 16, 'underline'))
	name_lb.place(x = 15, y = 60, width = 80, height = 30)
	#Поле ввода текста
	name_tx = ttk.Entry(authorization_window, justify = 'center',
		font = ('Comic Sans MS', 12))
	name_tx.place(x = 34, y = 90, width = 240, height = 25)

	
	#Текст - Фамилия
	second_name_lb = tk.Label(authorization_window, text = 'Фамилия', 
		bg = '#F5F5F5', font = ('Comic Sans MS', 16, 'underline'))
	second_name_lb.place(x = 15, y = 120, width = 129, height = 30)
	#Поле ввода текста
	second_name_tx = ttk.Entry(authorization_window, justify = 'center',
		font = ('Comic Sans MS', 12))
	second_name_tx.place(x = 34, y = 150, width = 240, height = 25)

	#Текст - Пароль
	password_lb = tk.Label(authorization_window, text = 'Пароль', 
		bg = '#F5F5F5', font = ('Comic Sans MS', 16, 'underline'))
	password_lb.place(x = 15, y = 180, width = 116, height = 30)
	#Поле ввода текста
	global password_tx
	password_tx = ttk.Entry(authorization_window, justify = 'center',
		font = ('Comic Sans MS', 12), show = "*")
	password_tx.place(x = 34, y = 210, width = 200, height = 25)

	#Текст - Группа или Класс, если нет - пропуск
	group_lb = tk.Label(authorization_window, text = 'Группа/Класс', 
		bg = '#F5F5F5',	font = ('Comic Sans MS', 16, 'underline'))
	group_lb.place(x = 15, y = 240, width = 184, height = 30)
	#Поле ввода текста
	group_tx = ttk.Entry(authorization_window, justify = 'center',
		font = ('Comic Sans MS', 12))
	group_tx.place(x = 34, y = 270, width = 240, height = 25)

	"""Функции для кнопочек"""	
	def open_password():
		"""Показывает пароль"""
		eye_off_bt_im.place_forget()
		eye_on_bt_im.place(x = 240, y = 206)
		password_tx['show'] = ""

	def close_password():
		"""Скрывает пароль"""
		eye_off_bt_im.place(x = 240, y = 206)
		eye_on_bt_im.place_forget()
		password_tx['show'] = "*"

	def authorization_user_on():
		"""Авторизирует пользователя в системе"""
		#Открываем .ini для взаимодействия с ним
		config = configparser.ConfigParser()
		config.read('Config.ini')

		user = []

		#Сюда сохраняем регистрировался ли пользователь
		config.set("Registration_User", "Registration", "on")
		#Сюда сохраняем имя
		name_user = name_tx.get()
		user.append(name_user)
		#Сюда сохраняем фамилию
		second_name_user = second_name_tx.get()
		user.append(second_name_user)
		#Сюда сохраняем класс/группу
		group = group_tx.get()
		user.append(group)
		#Сюда сохраняем пароль
		password = password_tx.get()
		user.append(password)
		#Сюда сохраняем нужно ли запомнить данные о входе
		password_on_or_off = str(var.get())
		config.set("Registration_User", "Password_on", 
			str(password_on_or_off))
	
		with open('Config.ini', "w") as config_file:
			config.write(config_file)	

		#Проверяем информацию в БД
		check = pydb.check_user(user)
		if check == 1:
			#Сохранение информации о пользователе
			if str(password_on_or_off) == '1':
				config = configparser.ConfigParser()
				config.read('Config.ini')
				user_id = pydb.save_user(user)
				user_id = user_id[0]
				config.set("Registration_User", "User_ID", str(user_id))
				with open('Config.ini', "w") as config_file:
					config.write(config_file)

			#Сохраняем ID
			user_id = pydb.save_user(user)
			global global_user_id
			global_user_id = user_id[0]
			#Закрываем окно авторизации
			authorization_window.destroy()
			#Открываем главное окно
			create_work_window()
		else:
			msg = "Проверьте правильность введенных данных"
			mb.showerror("Ошибка", msg)		

		

	def close_aut_window():
		#Закрывем окно авторизации
		authorization_window.destroy()

	def on_closing():
		"""Ловим закрытие окна верхнего уровня и 
		закрываем всю программу"""
		image_window.destroy()
	#Протокол закрытия, его и ловим
	authorization_window.protocol("WM_DELETE_WINDOW", on_closing)

	#Кнопка показать пароль
	global image_eye_off, eye_off_bt_im
	image_eye_off = tk.PhotoImage(
		file = 'icons/eye_off.png')

	eye_off_bt_im = tk.Button(authorization_window, bd = 0, bg = '#F5F5F5', 
		image = image_eye_off, command = open_password,
		activebackground = '#F5F5F5')
	eye_off_bt_im.place(x = 240, y = 206)

	#Кнопка скрыть пароль
	global image_eye_on, eye_on_bt_im
	image_eye_on = tk.PhotoImage(
		file = 'icons/eye_on.png')

	eye_on_bt_im = tk.Button(authorization_window, bd = 0, bg = '#F5F5F5', 
		image = image_eye_on, command = close_password, 
		activebackground = '#F5F5F5')
	eye_on_bt_im.place_forget()

	#Кнопка - запомнить
	var = tk.IntVar()
	var.set(1)

	remember_cbt = ttk.Checkbutton(authorization_window, 
		text = 'on', variable = var).place(x = 34, y = 300)
	remember_bt = tk.Button(authorization_window, bd = 0, bg = '#F5F5F5', 
		font = ('Comic Sans MS', 12, 'underline'), 
		text = 'Запомнить меня', activeforeground = '#08D9D6',
		activebackground = '#F5F5F5')
	remember_bt.place(x = 49, y = 298, height = 22)

	#Кнопка - Вход
	global image_reg
	image_reg = tk.PhotoImage(
		file = 'icons/ok.png')

	reg_bt_im = tk.Button(authorization_window, bd = 0, bg = '#F5F5F5', 
		image = image_reg, 
		activebackground = '#F5F5F5', command = authorization_user_on)
	reg_bt_im.place(x = 38, y = 330)

	reg_bt = tk.Button(authorization_window, bd = 0, bg = '#F5F5F5', 
		font = ('Comic Sans MS', 12, 'underline'), 
		text = 'Войти', fg = '#FF2E63', command = authorization_user_on,
		activebackground = '#F5F5F5', activeforeground = '#08D9D6')
	reg_bt.place(x = 84, y = 336)

	#Кнопка - Выход
	global image_exit
	image_exit = tk.PhotoImage(
		file = 'icons/no.png')

	exit_bt_im = tk.Button(authorization_window, bd = 0, bg = '#F5F5F5', 
		image = image_exit, 
		activebackground = '#F5F5F5', command = on_closing)
	exit_bt_im.place(x = 38, y = 380)

	exit_bt = tk.Button(authorization_window, bd = 0, bg = '#F5F5F5', 
		font = ('Comic Sans MS', 12, 'underline'), 
		text = 'Выход', fg = '#FF2E63', command = on_closing,
		activebackground = '#F5F5F5', activeforeground = '#08D9D6')
	exit_bt.place(x = 84, y = 388)
	
	#Кнопка - Регистрация
	aut_bt = tk.Button(authorization_window, bd = 0, bg = '#F5F5F5', 
		font = ('Comic Sans MS', 12, 'underline'), 
		text = 'У меня ещё нет аккаунта', activeforeground = '#08D9D6',
		activebackground = '#F5F5F5', command = lambda: (
			close_aut_window(), create_registration_window()))
	aut_bt.place(x = 60, y = 445)

	#Кнопка - Забыл пароль
	no_password_bt = tk.Button(authorization_window, bd = 0, bg = '#F5F5F5', 
		font = ('Comic Sans MS', 12, 'underline'), 
		text = 'Забыл пароль', activeforeground = '#08D9D6',
		activebackground = '#F5F5F5')
	no_password_bt.place(x = 150, y = 388)

	#Автозаполнение окна авторизации, ели пользователь решил запомнить пароль
	#Открываем .ini для взаимодействия с ним
	config = configparser.ConfigParser()
	config.read('Config.ini')
	password_on_or_off = config.get("Registration_User", "Password_on")
	if password_on_or_off == '1':
		user_id = config.get("Registration_User", "User_ID")
		user = pydb.info_user(user_id)
		name_tx.insert(0, user[1])
		second_name_tx.insert(0, user[2])
		group_tx.insert(0, user[3])
		password_tx.insert(0, user[4])
		#Сохраняем ID
		global global_user_id
		global_user_id = user_id
	else:
		pass

	authorization_window.mainloop()

#Главное окно программы
global create_work_window
def create_work_window():
	"""Создание главного окна"""
	work_window = tk.Toplevel()
	work_window.title("PyBook")
	work_window.resizable(width = False, height = False)

	"""Начало центрирования окна"""
	app_width = 1060
	app_height = 670

	screen_width = work_window.winfo_screenwidth()
	screen_height = work_window.winfo_screenheight()

	x = (screen_width / 2) - (app_width / 2)
	y = (screen_height / 2) - (app_height / 2)
	y -= 20

	work_window.geometry(f'{app_width}x{app_height}+{int(x)}+{int(y)}')
	"""Конец центрирования окна"""

	work_window.iconbitmap('icons/ico.ico')
	#work_window.attributes('-topmost', True) #Поверх всех окон

	"""Внешний вид главного окна"""
	image_work_window = tk.PhotoImage(
		file = work_window_light)
	work_window_lb = tk.Label(work_window, 
		image = image_work_window
		).place(x = 0, y = 0, width = 1060, height = 670)

	"""Функции"""
	#Открыть окно с информацией о пользователе
	def open_user_info():
		"""Прячем кнопку, и закрываем все другие окна"""
		user_bt_im.place_forget()
		global user_info_frame
		try:
			if settings_frame.winfo_exists():
				settings_frame.place_forget()
				settings_bt_im.place(x = 0, y = 48)
		except:
			pass
		try:
			if question_frame.winfo_exists():
				question_frame.place_forget()
				question_bt_im.place(x = 0, y = 96)
		except:
			pass
		try:
			if book_frame.winfo_exists():
				book_frame.place_forget()
				book_bt_im.place(x = 0, y = 144)
		except:
			pass

		#Контейнер для хранения виджетов окна-информации о пользователе
		user_info_frame = tk.Frame(work_window)
		user_info_frame.place(x = 0, y = 55, width = 400, height = 585)
		"""Внешний вид окна"""
		global image_user_info
		image_user_info = tk.PhotoImage(
			file = 'theme/user_info_light.png')
		user_window_lb = tk.Label(user_info_frame, 
			image = image_user_info)
		user_window_lb.place(x = 0, y = 0, width = 400, height = 585)

		#Текст - Имя
		name_lb = tk.Label(user_info_frame, text = 'Имя', bg = '#F5F5F5',
			font = ('Comic Sans MS', 14, 'underline'), anchor = 'w')
		name_lb.place(x = 50, y = 90, width = 184, height = 30)
		#Поле ввода текста
		name_tx = ttk.Entry(user_info_frame, justify = 'center',
			font = ('Comic Sans MS', 12))
		name_tx.place(x = 50, y = 120, width = 240, height = 25)

		
		#Текст - Фамилия
		second_name_lb = tk.Label(user_info_frame, text = 'Фамилия', 
			bg = '#F5F5F5', font = ('Comic Sans MS', 14, 'underline'), 
			anchor = 'w')
		second_name_lb.place(x = 50, y = 150, width = 184, height = 30)
		#Поле ввода текста
		second_name_tx = ttk.Entry(user_info_frame, justify = 'center',
			font = ('Comic Sans MS', 12))
		second_name_tx.place(x = 50, y = 180, width = 240, height = 25)

		#Текст - Группа или Класс, если нет - пропуск
		group_lb = tk.Label(user_info_frame, text = 'Группа/Класс', 
			bg = '#F5F5F5',	font = ('Comic Sans MS', 14, 'underline'), 
			anchor = 'w')
		group_lb.place(x = 50, y = 210, width = 184, height = 30)
		#Поле ввода текста
		group_tx = ttk.Entry(user_info_frame, justify = 'center',
			font = ('Comic Sans MS', 12))
		group_tx.place(x = 50, y = 240, width = 240, height = 25)

		#Текст - Страница учебника
		book_page_lb = tk.Label(user_info_frame, text = 'Страница в учебнике', 
			bg = '#F5F5F5',	font = ('Comic Sans MS', 14, 'underline'), 
			anchor = 'w')
		book_page_lb.place(x = 50, y = 270, width = 194, height = 30)
		#Поле ввода текста
		book_page_tx = ttk.Entry(user_info_frame, justify = 'center',
			font = ('Comic Sans MS', 12))
		book_page_tx.place(x = 50, y = 300, width = 240, height = 25)

		#Текст - Удаление аккаунта
		del_user_lb = tk.Label(user_info_frame, 
			text = 'Введите пароль, чтобы\nудалить аккаунт',
			bg = '#F5F5F5',	font = ('Comic Sans MS', 14), 
			anchor = 'w', fg = '#FF2E63')
		del_user_lb.place_forget()
		#Поле ввода текста
		del_user_tx = ttk.Entry(user_info_frame, justify = 'center',
			font = ('Comic Sans MS', 12), show = '*')
		del_user_tx.place_forget()

		"""Начало удаления аккаунта"""

		#Кнопка - Удалить аккаунт
		def del_user():
			user = []

			#Сюда сохраняем имя
			name_user = name_tx.get()
			user.append(name_user)
			#Сюда сохраняем фамилию
			second_name_user = second_name_tx.get()
			user.append(second_name_user)
			#Сюда сохраняем класс/группу
			group = group_tx.get()
			user.append(group)
			#Сюда сохраняем пароль
			password = del_user_tx.get()
			user.append(password)	

			#Проверяем информацию в БД
			check = pydb.check_user(user)
			if check == 1:
				#Удаляем пользователя
				user_id = global_user_id
				pydb.delete_user(str(user_id))
				config = configparser.ConfigParser()
				config.read('Config.ini')
				config.set("Registration_User", "Registration", "off")
				config.set("Registration_User", "Password_on", "off")
				with open('Config.ini', "w") as config_file:
					config.write(config_file)
				#Закрываем главное окноокно авторизации
				work_window.destroy()
				#Открываем окно регистрации
				create_registration_window()
			else:
				msg = "Проверьте правильность введенных данных"
				mb.showerror("Ошибка", msg)
			
		global image_del
		image_del = tk.PhotoImage(
			file = 'icons/delete.png')

		del_bt_im = tk.Button(user_info_frame, bd = 0, bg = '#F5F5F5', 
			image = image_del, command = del_user,
			activebackground = '#F5F5F5')
		del_bt_im.place_forget()

		del_bt = tk.Button(user_info_frame, bd = 0, bg = '#F5F5F5', 
			font = ('Comic Sans MS', 14, 'underline'), 
			text = 'Удалить аккаунт', fg = '#FF2E63', 
			activebackground = '#F5F5F5', command = del_user)
		del_bt.place_forget()

		#Кнопочка - Удалить аккаунт
		def close_book_window():
			#Открываем поле для ввода пароля и кнопку подтвердить
			exit_user_bt.place_forget()
			delete_user_bt.place_forget()
			del_user_lb.place(x = 50, y = 330, width = 240, height = 60)
			del_user_tx.place(x = 50, y = 388, width = 240, height = 25)
			del_bt_im.place(x = 50, y = 450)
			del_bt.place(x = 96, y = 456)
			global no_del
			def no_del():
				exit_user_bt.place(x = 80, y = 530)
				delete_user_bt.place(x = 80, y = 330)
				del_user_lb.place_forget()
				del_user_tx.place_forget()
				del_bt_im.place_forget()
				del_bt.place_forget()
				no_del_user_bt.place_forget()
			no_del_user_bt = tk.Button(user_info_frame, bd = 0, bg = '#F5F5F5', 
				font = ('Comic Sans MS', 14, 'underline'), 
				text = 'Отмена', activeforeground = '#08D9D6',
				activebackground = '#F5F5F5', command = no_del)
			no_del_user_bt.place(x = 275, y = 456)
			
		delete_user_bt = tk.Button(user_info_frame, bd = 0, bg = '#F5F5F5', 
			font = ('Comic Sans MS', 14, 'underline'), 
			text = 'Удалить аккаунт', activeforeground = '#FF2E63',
			activebackground = '#F5F5F5', command = close_book_window)
		delete_user_bt.place(x = 80, y = 330)

		"""Конец удаления аккаунта"""

		#Кнопочка - Сменить из аккаунт
		def close_book_window():
			#Закрываем окно учебник
			work_window.destroy()
		exit_user_bt = tk.Button(user_info_frame, bd = 0, bg = '#F5F5F5', 
			font = ('Comic Sans MS', 14, 'underline'), 
			text = 'Сменить аккаунт', activeforeground = '#08D9D6',
			activebackground = '#F5F5F5', command = lambda: (
				close_book_window(), create_authorization_window()))
		exit_user_bt.place(x = 80, y = 530)

		"""
		#Текст - Количество решенных тестов
		tests_lb = tk.Label(user_info_frame, text = 'Решено тестов', 
			bg = '#F5F5F5',	font = ('Comic Sans MS', 14, 'underline'), 
			anchor = 'w')
		tests_lb.place(x = 50, y = 330, width = 184, height = 30)
		#Поле ввода текста
		tsets_tx = ttk.Entry(user_info_frame, justify = 'center',
			font = ('Comic Sans MS', 12))
		tsets_tx.place(x = 50, y = 360, width = 240, height = 25)
		"""
		def user_info():
			"""Функция подстановки информации о пользователе"""
			user_id = str(global_user_id)
			user = pydb.info_user(user_id)
			name_tx.insert(0, user[1])
			name_tx['state'] = 'disabled'
			second_name_tx.insert(0, user[2])
			second_name_tx['state'] = 'disabled'
			group_tx.insert(0, user[3])
			group_tx['state'] = 'disabled'
			book_page_tx.insert(0, user[5])
			book_page_tx['state'] = 'disabled'
		user_info()
			
		def close_user_info():
			"""Функция, которая закрывает окошко с
			информацией о пользователе"""
			user_info_frame.place_forget()
			user_bt_im.place(x = 0, y = 0)

		name_label = tk.Label(user_info_frame, 
			text = 'Информация о пользователе',
			font = ('Comic Sans MS', 14, 'underline'), fg = '#252A34', bd = 0, 
			bg = bg_light).place(x = 48, y = 18, width = 300, height = 30)

		global click
		click = 0
		global save_edit_user
		def save_edit_user():
			def save_():	
				user = []
				user.append(str(global_user_id))
				#Сюда сохраняем имя
				name_user = name_tx.get()
				if name_tx.index("end") == 0:
					name_lb['fg'] = '#FF2E63'
					name_lb['text'] = 'Имя*'
					return 'break'
				if ' ' in name_user:
					return 'break'
				user.append(name_user)
				#Сюда сохраняем фамилию
				second_name_user = second_name_tx.get()
				if second_name_tx.index("end") == 0:
					second_name_lb['fg'] = '#FF2E63'
					second_name_lb['text'] = 'Фамилия*'
					return 'break'
				if ' ' in second_name_user:
					return 'break'
				user.append(second_name_user)
				#Сюда сохраняем класс/группу
				group = group_tx.get()
				if group_tx.index("end") == 0:
					group_lb['fg'] = '#FF2E63'
					group_lb['text'] = 'Группа/Класс*'
					return 'break'
				if ' ' in group:
					return 'break'
				user.append(group)
				
				name_tx['state'] = 'disabled'
				second_name_tx['state'] = 'disabled'
				group_tx['state'] = 'disabled'
				book_page_tx['state'] = 'disabled'

				pydb.edit_user(user)

				delete_user_bt.place(x = 80, y = 330)
				save_user_bt.place_forget()

				global click
				click = 0

			try:	
				no_del()
			except:
				pass

			if click == 1:
				"""Сохранение информации о пользователе"""
				save_user_bt = tk.Button(user_info_frame, bd = 0, bg = '#F5F5F5', 
					font = ('Comic Sans MS', 14, 'underline'), 
					text = 'Сохранить зменения', activeforeground = '#FF2E63',
					activebackground = '#F5F5F5', fg = '#08D9D6', command = save_)
				save_user_bt.place(x = 70, y = 330)

		def edit_name_user():
			"""Функция редактирования имени"""
			delete_user_bt.place_forget()
			name_tx['state'] = 'normal'
			global click
			click += 1
			save_edit_user()
			
		def edit_second_name_user():
			"""Функция редактирования фамилии"""
			delete_user_bt.place_forget()
			second_name_tx['state'] = 'normal'
			global click
			click += 1
			save_edit_user()
			
		def edit_group_user():
			"""Функция редактирования группы"""
			delete_user_bt.place_forget()
			group_tx['state'] = 'normal'
			global click
			click += 1
			save_edit_user()
			
		#Всплывающая подсказка
		def help_close_user_info_on(event):
			global help_image_close_user_info
			help_image_close_user_info = tk.PhotoImage(
			file = 'theme/help_light_1.png')
			global help_label_close_user_info
			help_label_close_user_info = tk.Label(work_window,
				image = help_image_close_user_info, text = 'Закрыть',
				compound='center',
				font = ('Comic Sans MS', 14, 'underline'))
			help_label_close_user_info.place(x = 400, y = 65, 
				width = 132, height = 48)
		def help_close_user_info_off(event):
			help_label_close_user_info.place_forget()
		#Кнопочка - закрыть окно с информацией
		global close_info_user
		close_info_user = tk.PhotoImage(
		file = 'icons/no.png')
		close_info_user_bt_im = tk.Button(user_info_frame, bd = 0, 
			bg = '#F5F5F5', image = close_info_user, 
			command = close_user_info, activebackground = '#F5F5F5')
		close_info_user_bt_im.place(x = 340, y = 10)
		close_info_user_bt_im.bind("<Enter>", help_close_user_info_on)
		close_info_user_bt_im.bind("<Leave>", help_close_user_info_off)

		#Всплывающая подсказка
		def help_edit_name_on(event):
			global help_image_edit_name
			help_image_edit_name = tk.PhotoImage(
			file = 'theme/help_light_48.png')
			global help_label_edit_name
			help_label_edit_name = tk.Label(work_window,
				image = help_image_edit_name, text = 'Изменить имя',
				compound='center',
				font = ('Comic Sans MS', 14, 'underline'))
			help_label_edit_name.place(x = 340, y = 160, 
				width = 256, height = 48)
		def help_edit_name_off(event):
			help_label_edit_name.place_forget()
		#Кнопочка - редактировать : имя
		global edit_user_name
		edit_user_name = tk.PhotoImage(
		file = 'icons/mini_edit.png')
		edit_user_name_bt_im = tk.Button(user_info_frame, bd = 0, 
			bg = '#F5F5F5', image = edit_user_name, 
			command = edit_name_user, activebackground = '#F5F5F5')
		edit_user_name_bt_im.place(x = 300, y = 116)
		edit_user_name_bt_im.bind("<Enter>", help_edit_name_on)
		edit_user_name_bt_im.bind("<Leave>", help_edit_name_off)

		def help_edit_second_name_on(event):
			global help_image_second_name
			help_image_second_name = tk.PhotoImage(
			file = 'theme/help_light_48.png')
			global help_label_second_name
			help_label_second_name = tk.Label(work_window,
				image = help_image_second_name, text = 'Изменить фамилию',
				compound='center',
				font = ('Comic Sans MS', 14, 'underline'))
			help_label_second_name.place(x = 340, y = 220, 
				width = 256, height = 48)
		def help_edit_second_name_off(event):
			help_label_second_name.place_forget()
		#Кнопочка - редактировать : фамилия
		global edit_user_second_name
		edit_user_second_name = tk.PhotoImage(
		file = 'icons/mini_edit.png')
		edit_user_second_name_bt_im = tk.Button(user_info_frame, bd = 0, 
			bg = '#F5F5F5', image = edit_user_second_name, 
			command = edit_second_name_user, activebackground = '#F5F5F5')
		edit_user_second_name_bt_im.place(x = 300, y = 176)
		edit_user_second_name_bt_im.bind("<Enter>", help_edit_second_name_on)
		edit_user_second_name_bt_im.bind("<Leave>", help_edit_second_name_off)

		def help_edit_group_on(event):
			global help_image_edit_group
			help_image_edit_group = tk.PhotoImage(
			file = 'theme/help_light_48.png')
			global help_label_edit_group
			help_label_edit_group = tk.Label(work_window,
				image = help_image_edit_group, text = 'Изменить класс/группу',
				compound='center',
				font = ('Comic Sans MS', 14, 'underline'))
			help_label_edit_group.place(x = 340, y = 280, 
				width = 256, height = 48)
		def help_edit_group_off(event):
			help_label_edit_group.place_forget()
		#Кнопочка - редактировать : класс
		global edit_user_group
		edit_user_group = tk.PhotoImage(
		file = 'icons/mini_edit.png')
		edit_user_group_bt_im = tk.Button(user_info_frame, bd = 0, 
			bg = '#F5F5F5', image = edit_user_group, 
			command = edit_group_user, activebackground = '#F5F5F5')
		edit_user_group_bt_im.place(x = 300, y = 236)
		edit_user_group_bt_im.bind("<Enter>", help_edit_group_on)
		edit_user_group_bt_im.bind("<Leave>", help_edit_group_off)

	#Открыть окно с настройками
	def open_settings():
		"""Прячем кнопку, и закрываем все другие окна"""
		settings_bt_im.place_forget()
		global settings_frame
		try:
			if user_info_frame.winfo_exists():
				user_info_frame.place_forget()
				user_bt_im.place(x = 0, y = 0)
		except:
			pass
		try:
			if question_frame.winfo_exists():
				question_frame.place_forget()
				question_bt_im.place(x = 0, y = 96)
		except:
			pass
		try:
			if book_frame.winfo_exists():
				book_frame.place_forget()
				book_bt_im.place(x = 0, y = 144)
		except:
			pass

		#Контейнер для хранения виджетов окна-настройки
		settings_frame = tk.Frame(work_window)
		settings_frame.place(x = 0, y = 55, width = 400, height = 585)
		"""Внешний вид окна"""
		global image_settings_window
		image_settings_window = tk.PhotoImage(
			file = 'theme/user_info_light.png')
		settings_window_lb = tk.Label(settings_frame, 
			image = image_settings_window)
		settings_window_lb.place(x = 0, y = 0, width = 400, height = 585)

		def close_settings():
			"""Функция, которая закрывает окошко с настройками"""
			settings_frame.place_forget()
			settings_bt_im.place(x = 0, y = 48)

		name_label = tk.Label(settings_frame, 
			text = 'Настройки',
			font = ('Comic Sans MS', 14, 'underline'), fg = '#252A34', bd = 0, 
			bg = bg_light).place(x = 48, y = 18, width = 300, height = 30)

		#Всплывающая подсказка
		def help_close_settings_on(event):
			global help_image_close_settings
			help_image_close_settings = tk.PhotoImage(
			file = 'theme/help_light_1.png')
			global help_label_close_settings
			help_label_close_settings = tk.Label(work_window,
				image = help_image_close_settings, text = 'Закрыть',
				compound='center',
				font = ('Comic Sans MS', 14, 'underline'))
			help_label_close_settings.place(x = 400, y = 65, 
				width = 132, height = 48)
		def help_close_settings_off(event):
			help_label_close_settings.place_forget()
		#Кнопочка - закрыть окно с настройками
		global close_settings_
		close_settings_ = tk.PhotoImage(
		file = 'icons/no.png')
		close_settings_bt_im = tk.Button(settings_frame, bd = 0, 
			bg = '#F5F5F5', image = close_settings_, 
			command = close_settings, activebackground = '#F5F5F5')
		close_settings_bt_im.place(x = 340, y = 10)
		close_settings_bt_im.bind("<Enter>", help_close_settings_on)
		close_settings_bt_im.bind("<Leave>", help_close_settings_off)

	#Открыть окно с информацией, вопросами
	def open_question():
		"""Прячем кнопку, и закрываем все другие окна"""
		question_bt_im.place_forget()
		global question_frame
		try:
			if user_info_frame.winfo_exists():
				user_info_frame.place_forget()
				user_bt_im.place(x = 0, y = 0)
		except:
			pass
		try:
			if settings_frame.winfo_exists():
				settings_frame.place_forget()
				settings_bt_im.place(x = 0, y = 48)
		except:
			pass
		try:
			if book_frame.winfo_exists():
				book_frame.place_forget()
				book_bt_im.place(x = 0, y = 144)
		except:
			pass

		#Контейнер для хранения виджетов окна-помощи
		question_frame = tk.Frame(work_window)
		question_frame.place(x = 0, y = 55, width = 400, height = 585)
		"""Внешний вид окна"""
		global image_question_window
		image_question_window = tk.PhotoImage(
			file = 'theme/user_info_light.png')
		question_window_lb = tk.Label(question_frame, 
			image = image_question_window)
		question_window_lb.place(x = 0, y = 0, width = 400, height = 585)

		"""Текст об авторе"""
		config = configparser.ConfigParser()
		config.read('Config.ini')
		version = config.get("Registration_User", "Version")
		
		author_text = (
			'Приложение PyBook придумано и\n',
			'разработано Федоровым Максимом\n\n',
			'PyBook - это интерактивный\n',
			'учебник, который с помощью\n',
			'простых формулировок и примеров\n',
			'научит вас основам языка Python\n\n',
			'В случае обнаружения ошибки или\n',
			'предложениях об улучшении\n',
			'функционала PyBook, просьба\n',
			'сообщить сюда:\n',
			'fedorowma@ya.ru\n\n\n\n\n\n',version)
		author = tk.Label(question_frame, bg = bg_light,
			font = ('Comic Sans MS', 14), fg = '#252A34', anchor='nw', 
			text = " ".join(author_text))
		author.place(x = 35, y = 75, width = 350, height = 500)

		def close_question():
			"""Функция, которая закрывает окошко помощь"""
			question_frame.place_forget()
			question_bt_im.place(x = 0, y = 96)

		name_label = tk.Label(question_frame, 
			text = 'Информация',
			font = ('Comic Sans MS', 14, 'underline'), fg = '#252A34', bd = 0, 
			bg = bg_light).place(x = 48, y = 18, width = 300, height = 30)

		#Всплывающая подсказка
		def help_close_question_on(event):
			global help_image_close_question
			help_image_close_question = tk.PhotoImage(
			file = 'theme/help_light_1.png')
			global help_label_close_question
			help_label_close_question = tk.Label(work_window,
				image = help_image_close_question, text = 'Закрыть',
				compound='center',
				font = ('Comic Sans MS', 14, 'underline'))
			help_label_close_question.place(x = 400, y = 65, 
				width = 132, height = 48)
		def help_close_question_off(event):
			help_label_close_question.place_forget()
		#Кнопочка - закрыть окно помощи
		global close_question_
		close_question_ = tk.PhotoImage(
		file = 'icons/no.png')
		close_question_bt_im = tk.Button(question_frame, bd = 0, 
			bg = '#F5F5F5', image = close_question_, 
			command = close_question, activebackground = '#F5F5F5')
		close_question_bt_im.place(x = 340, y = 10)
		close_question_bt_im.bind("<Enter>", help_close_question_on)
		close_question_bt_im.bind("<Leave>", help_close_question_off)

	#Открыть учебник
	def open_book():
		"""Прячем кнопку, и закрываем все другие окна"""
		book_bt_im.place_forget()
		global book_frame
		try:
			if user_info_frame.winfo_exists():
				user_info_frame.place_forget()
				user_bt_im.place(x = 0, y = 0)
		except:
			pass
		try:
			if settings_frame.winfo_exists():
				settings_frame.place_forget()
				settings_bt_im.place(x = 0, y = 48)
		except:
			pass
		try:
			if question_frame.winfo_exists():
				question_frame.place_forget()
				question_bt_im.place(x = 0, y = 96)
		except:
			pass
		#Контейнер для хранения виджетов учебника
		book_frame = tk.Frame(work_window, bg = '#F5F5F5')
		book_frame.place(x = 130, y = 85, width = 800, height = 500)
		"""Внешний вид окна"""
		global image_book_window
		image_book_window = tk.PhotoImage(
			file = 'theme/book_light.png')
		book_window_lb = tk.Label(book_frame, 
			image = image_book_window)
		book_window_lb.place(x = 0, y = 0, width = 800, height = 500)

		def open_code_edit():
			edit_bt_im.place_forget()
			"""Функция открытия редактора кода"""
			"""Создание окна регистрации"""
			code_edit_window = tk.Toplevel()
			code_edit_window.title("PyBook Редактор")
			code_edit_window.resizable(width = False, height = False)

			"""Начало центрирования окна"""
			app_width = 376
			app_height = 670

			screen_width = code_edit_window.winfo_screenwidth()
			screen_height = code_edit_window.winfo_screenheight()

			x = (screen_width / 2) - (app_width / 2)
			y = (screen_height / 2) - (app_height / 2)
			y -= 20

			code_edit_window.geometry(f'{app_width}x{app_height}+{int(x)}+{int(y)}')
			"""Конец центрирования окна"""

			code_edit_window.iconbitmap('icons/ico.ico')
			code_edit_window.attributes('-topmost', True) #Поверх всех окон

			"""Внешний вид окна редактора"""
			global code_edit_win
			code_edit_win = tk.PhotoImage(
				file = 'theme/code_edit_light.png')
			code_edit_window_lb = tk.Label(code_edit_window, 
				image = code_edit_win
				).place(x = 0, y = 0, width = 376, height = 670)

			#Поле для ввода кода
			code_edit_text = tk.Text(code_edit_window, font = ('Consolas', 14), 
				bg = '#F5F5F5', bd = 0, fg = '#252A34')
			code_edit_text.place(x = 12, y = 100, width = 351, height = 300)
			code_edit_text.focus_set()
			input_label = tk.Label(code_edit_window, 
				font = ('Comic Sans MS', 14, 'underline'), 
				text = 'Здесь вводим код', fg = '#FF2E63', bd = 0,
			bg = bg_light).place(x = 12, y = 65, width = 351, height = 30)
			#Поле вывода результата
			code_edit_result = tk.Text(code_edit_window, font = ('Consolas', 14), 
				bg = '#F5F5F5', bd = 0, fg = '#FF2E63')
			code_edit_result.place(x = 12, y = 460, width = 351, height = 170)
			output_label = tk.Label(code_edit_window, 
				font = ('Comic Sans MS', 14, 'underline'), 
				text = 'Здесь видим результат', fg = '#08D9D6', bd = 0,
			bg = bg_light).place(x = 12, y = 430, width = 351, height = 30)

			#Функции кнопок редактора 
			#Пуск
			def stat_code():
				code_edit_result.delete('1.0', 'end')
				Cpath = 'PyBookFile.py'
				path = Cpath
				with open(path, 'w+') as file:
					code = code_edit_text.get('1.0', 'end')
					file.write(code)
				Command = f'python {Cpath}'
				process = subprocess.Popen(Command, stdout = subprocess.PIPE, 
					stderr = subprocess.PIPE, shell = True)
				result, Error = process.communicate()
				code_edit_result.insert('1.0', result)
				code_edit_result.insert('1.0', Error)
			#Очистить
			def delete_code():
				code_edit_text.delete('1.0', 'end')
				code_edit_result.delete('1.0', 'end')
			#Табуляция
			def tab_pressed(arg):
				code_edit_text.insert(tk.INSERT, " "*4)
				return 'break'
			#Одинарные кавычки
			def quotation_marks_1_pressed(arg):
				code_edit_text.insert(tk.INSERT, "'"*2)
				time.sleep(0.2)
				keyboard.press("left")
				return 'break'
			#Двойные кавычки
			def quotation_marks_2_pressed(arg):
				code_edit_text.insert(tk.INSERT, '"'*2)
				time.sleep(0.2)
				keyboard.press("left")
				return 'break'
			#Скобки
			def parenthesis_pressed(arg):
				code_edit_text.insert(tk.INSERT, '()')
				time.sleep(0.2)
				keyboard.press("left")
				return 'break'

			#Кнопочки для редактора кода
			#Кнопки будут в этом контейнере для удобства
			bt_edit_frame = tk.Frame(code_edit_window, bg = bg_light)
			bt_edit_frame.place(x = 275, y = 10, width = 102, height = 50)

			#Кнопка - Запуск
			global image_play
			image_play = tk.PhotoImage(
				file = 'icons/play.png')

			play_bt_im = tk.Button(bt_edit_frame, bd = 0, bg = '#F5F5F5', 
				image = image_play, 
				activebackground = '#F5F5F5', command = stat_code)
			play_bt_im.place(x = 2, y = 0, width = 48, height = 48)
			#Кнопка - Очистить
			global image_delete
			image_delete = tk.PhotoImage(
				file = 'icons/delete.png')

			delete_bt_im = tk.Button(bt_edit_frame, bd = 0, bg = '#F5F5F5', 
				image = image_delete, 
				activebackground = '#F5F5F5', command = delete_code)
			delete_bt_im.place(x = 52, y = 0, width = 48, height = 48)

			code_edit_text.bind("<Tab>", tab_pressed)
			code_edit_text.bind("<'>", quotation_marks_1_pressed)
			code_edit_text.bind('<">', quotation_marks_2_pressed)
			code_edit_text.bind('<(>', parenthesis_pressed)

			def on_button():
				edit_bt_im.place(x = 162, y = 0)
				code_edit_window.destroy()
			#Протокол закрытия, его и ловим
			code_edit_window.protocol("WM_DELETE_WINDOW", on_button)
			code_edit_window.mainloop()

		def close_book():
			"""Функция, которая закрывает окошко помощь"""
			book_frame.place_forget()
			book_bt_im.place(x = 0, y = 144)

		name_label = tk.Label(book_frame, 
			text = 'PyBook',
			font = ('Comic Sans MS', 14, 'underline'), fg = '#252A34', bd = 0, 
			bg = bg_light).place(x = 10, y = 8, width = 65, height = 30)

		line_label = tk.Label(book_frame, 
			font = ('Comic Sans MS', 14),
			text = '_____________________________________________________',
			fg = '#252A34', bd = 0,
			bg = bg_light).place(x = 235, y = 398, width = 324, height = 40)

		def next_page():
			"""Следующая страница"""
			Progress = []
			m_page = pytx.max_page()
			global book_page
			if book_page == m_page: #Указывать максимальное значение
				pass
			else:
				book_page += 1
				Progress.append(book_page)
				user_id = str(global_user_id)
				Progress.append(user_id)
				pydb.plus_progress(Progress)
				text_number_page = pytx.number_page(book_page)
				book_label['text'] = " ".join(text_number_page)
			
		def back_page():
			"""Предыдущая страница"""
			Progress = []

			global book_page 
			if book_page == 0: #Указывать минимальное значение
				pass
			else:
				book_page -= 1
				Progress.append(book_page)
				user_id = str(global_user_id)
				Progress.append(user_id)
				pydb.plus_progress(Progress)
				text_number_page = pytx.number_page(book_page)
				book_label['text'] = " ".join(text_number_page)
			
		"""Здесь будем записывать тексты в учебник"""
		
		"""По ID пользователя запрашиваем в БД информацию, а точнее
		номер страницы, на которой остановился пользователь, чтобы 
		автоматически открыть эту страницу в программе"""
		user_id = str(global_user_id)
		user = pydb.info_user(user_id)
		page = user[5]
		global book_page
		book_page = int(page)
		text_number_page = pytx.number_page(book_page)
		#Сюда записываем текст
		global book_label
		book_label = tk.Label(book_frame, bg = bg_light,
			font = ('Comic Sans MS', 14), fg = '#252A34', anchor='center', 
			text = " ".join(text_number_page))
		book_label.place(x = 10, y = 80, width = 780, height = 300)

		#Кнопочки!
		button_book_fr = tk.Frame(book_frame, bg = '#F5F5F5')
		button_book_fr.place(x = 238, y = 430, width = 324, height = 55)
		
		#Всплывающая подсказка
		def help_back_on(event):
			global help_image_back
			help_image_back = tk.PhotoImage(
			file = 'theme/help_light_1.png')
			global help_label_back
			help_label_back = tk.Label(work_window,
				image = help_image_back, text = 'Назад',
				compound='center',
				font = ('Comic Sans MS', 14, 'underline'))
			help_label_back.place(x = 300, y = 460, 
				width = 132, height = 48)
		def help_back_off(event):
			help_label_back.place_forget()
		#Назад
		global back_
		back_ = tk.PhotoImage(
		file = 'icons/left.png')
		back_bt_im = tk.Button(button_book_fr, bd = 0, 
			bg = '#F5F5F5', image = back_, 
			activebackground = '#F5F5F5', command = back_page)
		back_bt_im.place(x = 0, y = 0)
		back_bt_im.bind("<Enter>", help_back_on)
		back_bt_im.bind("<Leave>", help_back_off)

		#Всплывающая подсказка
		def help_info_on(event):
			global help_image_info
			help_image_info = tk.PhotoImage(
			file = 'theme/help_light_1.png')
			global help_label_info
			help_label_info = tk.Label(work_window,
				image = help_image_info, text = 'Дополнение',
				compound='center',
				font = ('Comic Sans MS', 14, 'underline'))
			help_label_info.place(x = 354, y = 460, 
				width = 132, height = 48)
		def help_info_off(event):
			help_label_info.place_forget()
		#Дополнение
		global info_
		info_ = tk.PhotoImage(
		file = 'icons/info.png')
		info_bt_im = tk.Button(button_book_fr, bd = 0, 
			bg = '#F5F5F5', image = info_, 
			activebackground = '#F5F5F5')
		info_bt_im.place(x = 54, y = 0)
		info_bt_im.bind("<Enter>", help_info_on)
		info_bt_im.bind("<Leave>", help_info_off)

		#Всплывающая подсказка
		def help_content_on(event):
			global help_image_content
			help_image_content = tk.PhotoImage(
			file = 'theme/help_light_1.png')
			global help_label_content
			help_label_content = tk.Label(work_window,
				image = help_image_content, text = 'Содержание',
				compound='center',
				font = ('Comic Sans MS', 14, 'underline'))
			help_label_content.place(x = 408, y = 460, 
				width = 132, height = 48)
		def help_content_off(event):
			help_label_content.place_forget()
		#Содержание
		global content_
		content_ = tk.PhotoImage(
		file = 'icons/content.png')
		content_bt_im = tk.Button(button_book_fr, bd = 0, 
			bg = '#F5F5F5', image = content_, 
			activebackground = '#F5F5F5')
		content_bt_im.place(x = 108, y = 0)
		content_bt_im.bind("<Enter>", help_content_on)
		content_bt_im.bind("<Leave>", help_content_off)

		#Всплывающая подсказка
		def help_edit_on(event):
			global help_image_edit
			help_image_edit = tk.PhotoImage(
			file = 'theme/help_light_1.png')
			global help_label_edit
			help_label_edit = tk.Label(work_window,
				image = help_image_edit, text = 'Редактор',
				compound='center',
				font = ('Comic Sans MS', 14, 'underline'))
			help_label_edit.place(x = 455, y = 460, 
				width = 132, height = 48)
		def help_edit_off(event):
			help_label_edit.place_forget()
		#Редактор
		global edit_
		edit_ = tk.PhotoImage(
		file = 'icons/edit.png')
		edit_bt_im = tk.Button(button_book_fr, bd = 0, 
			bg = '#F5F5F5', image = edit_, 
			activebackground = '#F5F5F5', command = open_code_edit)
		edit_bt_im.place(x = 162, y = 0)
		edit_bt_im.bind("<Enter>", help_edit_on)
		edit_bt_im.bind("<Leave>", help_edit_off)

		#Всплывающая подсказка
		def help_help_on(event):
			global help_image_help
			help_image_help = tk.PhotoImage(
			file = 'theme/help_light_1.png')
			global help_label_help
			help_label_help = tk.Label(work_window,
				image = help_image_help, text = 'Помощь',
				compound='center',
				font = ('Comic Sans MS', 14, 'underline'))
			help_label_help.place(x = 510, y = 460, 
				width = 132, height = 48)
		def help_help_off(event):
			help_label_help.place_forget()
		#Помощь
		global help_
		help_ = tk.PhotoImage(
		file = 'icons/question.png')
		help_bt_im = tk.Button(button_book_fr, bd = 0, 
			bg = '#F5F5F5', image = help_, 
			activebackground = '#F5F5F5')
		help_bt_im.place(x = 216, y = 0)
		help_bt_im.bind("<Enter>", help_help_on)
		help_bt_im.bind("<Leave>", help_help_off)

		#Всплывающая подсказка
		def help_next_on(event):
			global help_image_next
			help_image_next = tk.PhotoImage(
			file = 'theme/help_light_1.png')
			global help_label_next
			help_label_next = tk.Label(work_window,
				image = help_image_next, text = 'Далее',
				compound='center',
				font = ('Comic Sans MS', 14, 'underline'))
			help_label_next.place(x = 565, y = 460, 
				width = 132, height = 48)
		def help_next_off(event):
			help_label_next.place_forget()
		#Далее
		global next_
		next_ = tk.PhotoImage(
		file = 'icons/right.png')
		next_bt_im = tk.Button(button_book_fr, bd = 0, 
			bg = '#F5F5F5', image = next_, 
			activebackground = '#F5F5F5', command = next_page)
		next_bt_im.place(x = 270, y = 0)
		next_bt_im.bind("<Enter>", help_next_on)
		next_bt_im.bind("<Leave>", help_next_off)
		
		#Всплывающая подсказка
		def help_close_book_on(event):
			global help_image_close_book
			help_image_close_book = tk.PhotoImage(
			file = 'theme/help_light_1.png')
			global help_label_close_book
			help_label_close_book = tk.Label(work_window,
				image = help_image_close_book, text = 'Закрыть',
				compound='center',
				font = ('Comic Sans MS', 14, 'underline'))
			help_label_close_book.place(x = 798, y = 30, 
				width = 132, height = 48)
		def help_close_book_off(event):
			help_label_close_book.place_forget()
		#Кнопочка - закрыть окно помощи
		global close_book_
		close_book_ = tk.PhotoImage(
		file = 'icons/no.png')
		close_book_bt_im = tk.Button(book_frame, bd = 0, 
			bg = '#F5F5F5', image = close_book_, 
			command = close_book, activebackground = '#F5F5F5')
		close_book_bt_im.place(x = 745, y = 8)
		close_book_bt_im.bind("<Enter>", help_close_book_on)
		close_book_bt_im.bind("<Leave>", help_close_book_off)

	"""Кнопочки"""
	#Контейнер для хранения кнопочек
	button_fr = tk.Frame(work_window, bg = '#F5F5F5')
	button_fr.place(x = 1012, y = 0, width = 48, height = 240)

	#Всплывающая подсказка
	def help_user_on(event):
		global help_image_user
		help_image_user = tk.PhotoImage(
		file = 'theme/help_light_1.png')
		global help_label_user
		help_label_user = tk.Label(work_window,
			image = help_image_user, text = 'Обо мне',
			compound='center',
			font = ('Comic Sans MS', 14, 'underline'))
		help_label_user.place(x = 870, y = 0, width = 132, height = 48)
	def help_user_off(event):
		help_label_user.place_forget()
	#Кнопка - пользователь
	image_user = tk.PhotoImage(
		file = 'icons/user.png')
	user_bt_im = tk.Button(button_fr, bd = 0, bg = '#F5F5F5', 
		image = image_user, command = open_user_info,
		activebackground = '#F5F5F5')
	user_bt_im.place(x = 0, y = 0)
	user_bt_im.bind("<Enter>", help_user_on)
	user_bt_im.bind("<Leave>", help_user_off)

	#Всплывающая подсказка
	def help_settings_on(event):
		global help_image_settings
		help_image_settings = tk.PhotoImage(
		file = 'theme/help_light_1.png')
		global help_label_settings
		help_label_settings = tk.Label(work_window,
			image = help_image_settings, text = 'Настройки',
			compound='center',
			font = ('Comic Sans MS', 14, 'underline'))
		help_label_settings.place(x = 870, y = 48, width = 132, height = 48)
	def help_settings_off(event):
		help_label_settings.place_forget()
	#Кнопка - настройки
	image_settings = tk.PhotoImage(
		file = 'icons/settings.png')
	settings_bt_im = tk.Button(button_fr, bd = 0, bg = '#F5F5F5', 
		image = image_settings, command = open_settings,
		activebackground = '#F5F5F5')
	settings_bt_im.place(x = 0, y = 48)
	settings_bt_im.bind("<Enter>", help_settings_on)
	settings_bt_im.bind("<Leave>", help_settings_off)

	#Всплывающая подсказка
	def help_question_on(event):
		global help_image_question
		help_image_question = tk.PhotoImage(
		file = 'theme/help_light_1.png')
		global help_label_question
		help_label_question = tk.Label(work_window,
			image = help_image_question, text = 'Помощь',
			compound='center',
			font = ('Comic Sans MS', 14, 'underline'))
		help_label_question.place(x = 870, y = 96, width = 132, height = 48)
	def help_question_off(event):
		help_label_question.place_forget()
	#Кнопка - помощь
	image_question = tk.PhotoImage(
		file = 'icons/question.png')
	question_bt_im = tk.Button(button_fr, bd = 0, bg = '#F5F5F5', 
		image = image_question, command = open_question,
		activebackground = '#F5F5F5')
	question_bt_im.place(x = 0, y = 96)
	question_bt_im.bind("<Enter>", help_question_on)
	question_bt_im.bind("<Leave>", help_question_off)

	#Всплывающая подсказка
	def help_book_on(event):
		global help_image_book
		help_image_book = tk.PhotoImage(
		file = 'theme/book_button.png')
		global help_label_book
		help_label_book = tk.Label(work_window,
			image = help_image_book, text = 'Учебник',
			compound='center',
			font = ('Comic Sans MS', 14, 'underline'))
		help_label_book.place(x = 870, y = 144, width = 132, height = 48)
	def help_book_off(event):
		help_label_book.place_forget()
	#Кнопка - учебник
	image_book = tk.PhotoImage(
		file = 'icons/book.png')
	book_bt_im = tk.Button(button_fr, bd = 0, bg = '#F5F5F5', 
		image = image_book, command = open_book,
		activebackground = '#F5F5F5')
	book_bt_im.place(x = 0, y = 144)
	book_bt_im.bind("<Enter>", help_book_on)
	book_bt_im.bind("<Leave>", help_book_off)

	def on_closing():
		"""Ловим закрытие окна верхнего уровня и 
		закрываем всю программу"""
		image_window.destroy()
	#Протокол закрытия, его и ловим
	work_window.protocol("WM_DELETE_WINDOW", on_closing)
	work_window.mainloop()



	"""
	#Фрейм для хранения всех виджетов учебника[центр]
	text_frame = tk.Frame(work_window, bg = '#FF2E63')
	text_frame.place(x = 230, y = 0, width = 600, height = 670)
	#Для красоты
	color_lb = tk.Label(text_frame, bg = '#F5F5F5').place(
		x = 2, y = 2, width = 596, height = 666)


	#Номер страницы
	global number_page
	number_page = 1

	if number_page == 1:
		text_number_page = ('Приветствую, ' + user_name +'\n'
			'ffffffffffffffffffff')

	text_label = tk.Label(text_frame, text = " ".join(text_number_page),
		bg = '#F5F5F5', font = (14), 
		fg = '#252A34', justify = 'left')
	text_label.place(x = 4, y = 8)
	"""


	"""Редактор кода
	#Функции кнопок редактора 
	#Пуск
	def stat_code():
		code_edit_result.delete('1.0', 'end')
		Cpath = 'PyBookFile.py'
		path = Cpath
		with open(path, 'w+') as file:
			code = code_edit_text.get('1.0', 'end')
			file.write(code)
		Command = f'python {Cpath}'
		process = subprocess.Popen(Command, stdout = subprocess.PIPE, 
			stderr = subprocess.PIPE, shell = True)
		result, Error = process.communicate()
		code_edit_result.insert('1.0', result)
		code_edit_result.insert('1.0', Error)
	#Очистить
	def delete_code():
		code_edit_text.delete('1.0', 'end')
	#Табуляция
	def tab_pressed(arg):
		code_edit_text.insert(tk.INSERT, " "*4)
		return 'break'
	#Одинарные кавычки
	def quotation_marks_1_pressed(arg):
		code_edit_text.insert(tk.INSERT, "'"*2)
		time.sleep(0.2)
		keyboard.press("left")
		return 'break'
	#Двойные кавычки
	def quotation_marks_2_pressed(arg):
		code_edit_text.insert(tk.INSERT, '"'*2)
		time.sleep(0.2)
		keyboard.press("left")
		return 'break'
	#Скобки
	def parenthesis_pressed(arg):
		code_edit_text.insert(tk.INSERT, '()')
		time.sleep(0.2)
		keyboard.press("left")
		return 'break'

	#Поле для ввода кода
	edit_text_lb = tk.Label(work_window, bg = '#FF2E63'
		).place(x = 498, y = 48, width = 564, height = 464)
	code_edit_text = tk.Text(work_window, font = ('Consolas', 12))
	code_edit_text.place(x = 500, y = 50, width = 560, height = 460)
	#Поле вывода результата
	edit_result_lb = tk.Label(work_window, bg = '#FF2E63'
		).place(x = 498, y = 518, width = 564, height = 124)
	code_edit_result = tk.Text(work_window, font = ('Consolas', 12))
	code_edit_result.place(x = 500, y = 520, width = 560, height = 120)

	#Кнопочки для редактора кода
	#Кнопки будут в этом контейнере для удобства
	bt_edit_frame = tk.Frame(work_window, bg = '#FF2E63')
	bt_edit_frame.place(x = 498, y = 0, width = 102, height = 50)

	#Кнопка - Запуск
	global image_play
	image_play = tk.PhotoImage(
		file = 'icons/play.png')

	play_bt_im = tk.Button(bt_edit_frame, bd = 0, bg = '#F5F5F5', 
		image = image_play, 
		activebackground = '#F5F5F5', command = stat_code)
	play_bt_im.place(x = 2, y = 0, width = 48, height = 48)
	#Кнопка - Очистить
	global image_delete
	image_delete = tk.PhotoImage(
		file = 'icons/delete.png')

	delete_bt_im = tk.Button(bt_edit_frame, bd = 0, bg = '#F5F5F5', 
		image = image_delete, 
		activebackground = '#F5F5F5', command = delete_code)
	delete_bt_im.place(x = 52, y = 0, width = 48, height = 48)

	

	code_edit_text.bind("<Tab>", tab_pressed)
	code_edit_text.bind("<'>", quotation_marks_1_pressed)
	code_edit_text.bind('<">', quotation_marks_2_pressed)
	code_edit_text.bind('<(>', parenthesis_pressed)

	file_code = open("PyBookFile.py", "w+")
	file_code.write("This is a test!")
	file_code.close()
	with open("PyBookFile.py", "w+", encoding='utf-8') as txt:
		print(txt.read(20))"""	
	
	

""" Не обязательно
#Окно-книга
def create_book_window():
	book_window = tk.Toplevel()
	book_window.mainloop()
#Окно-редактор кода
def create_book_window():
	book_window = tk.Toplevel()
	book_window.mainloop()
"""



"""Запуск программы"""
pydb.start()
create_image_window()
