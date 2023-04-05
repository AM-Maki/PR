import tkinter as tk
import tkinter.ttk as ttk
import PyBookDataBaseControl as pydb

win_info = tk.Tk()
win_info.title("PyBook Информация")
win_info.iconbitmap('icons/ico.ico')
win_info.geometry("440x200") 
win_info.rowconfigure(index=0, weight=1)
win_info.columnconfigure(index=0, weight=1)

# определяем данные для отображения
people = pydb.output_user()
 
# определяем столбцы
columns = ("name", "second_name", "class", "progress")
 
tree = ttk.Treeview(columns=columns, show="headings")
tree.grid(row=0, column=0, sticky="nsew")
 
# определяем заголовки
tree.heading("name", text="Имя", anchor='w')
tree.heading("second_name", text="Фамилия", anchor='w')
tree.heading("class", text="Группа/Класс", anchor='w')
tree.heading("progress", text="Страница в учебнике", anchor='w')
 
tree.column("#1", stretch='NO', width=100)
tree.column("#2", stretch='NO', width=100)
tree.column("#3", stretch='NO', width=100)
tree.column("#4", stretch='NO', width=125)
 
# добавляем данные
for person in people:
	tree.insert("", 'end', values=person)
 
# добавляем вертикальную прокрутку
scrollbar = ttk.Scrollbar(orient='vertical', command=tree.yview)
tree.configure(yscroll=scrollbar.set)
scrollbar.grid(row=0, column=1, sticky="ns")
 
win_info.mainloop()