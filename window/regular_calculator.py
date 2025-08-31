import os
import re
import tkinter as tk
from tkinter import ttk, END, messagebox
from config import calculation


class RegularCalculator:
    def __init__(self, parent, main_window):
        self.main = main_window

        self.root = parent

        self.buttons = [[7, 8, 9, '/'],
                        [4, 5, 6, '*'],
                        [1, 2, 3, '-'],
                        ['.', 0, '=', '+'],
                        ['C', '<--', 'e', 'ист']]

        self.history = []
        self.history_listbox = None  # пока нет окна

        self.check_1 = (self.root.register(self.is_valid_1), "%P")

        self._create_interface()

    def _create_interface(self):
        self.main_frame = ttk.Frame(self.root)
        self.main_frame.pack(pady=5)

        s = ttk.Style()

        self.number_entry_1 = tk.Entry(self.main_frame,
                                       font=('Arial', 15),
                                       validate='key',
                                       width=25,
                                       validatecommand=self.check_1,
                                       relief="solid")

        # self.number_entry_1.bind("<Key>", pulse_entry)
        # self.number_entry_1.bind("<KeyRelease>", expand_entry)

        self.number_entry_1.pack()

        self.buttons_frame = ttk.Frame(self.main_frame)
        self.buttons_frame.pack(pady=10)

        s = ttk.Style()
        s.configure('b.TButton',
                    width=5,
                    height=5,
                    padding=[12, 12, 12, 12])

        for i, g in enumerate(self.buttons):
            for f in range(len(g)):
                command = lambda text=g[f]: self._button_clicked(text)
                ttk.Button(self.buttons_frame,
                           text=g[f],
                           style='b.TButton',
                           command=command).grid(column=f, row=i)

        self.history_window_visible = False

    # окно для истории вычислений
    def _show_history_window(self):
        self.history_window_visible = True

        self.history_window = tk.Toplevel(self.root)
        self.history_window.title("История вычислений")

        self.ws = self.history_window.winfo_screenwidth()
        self.hs = self.history_window.winfo_screenheight()

        self.width = 300
        self.height = 300

        x = (self.ws / 1.4) - (self.width / 2)
        y = (self.hs / 2) - (self.height / 2)

        self.history_window.geometry('%dx%d+%d+%d' % (self.width, self.height, x, y)) # история справа от основного окна
        self.history_window.minsize(self.width, self.height)

        self.history_frame = ttk.Frame(self.history_window)
        self.history_frame.pack()

        self.history_label = tk.Label(self.history_frame, text="История", font=('Arial', 12))
        self.history_label.pack()

        # Listbox с прокруткой
        self.history_scrollbar = tk.Scrollbar(self.history_frame)
        self.history_scrollbar.pack(side="right", fill="y")

        self.history_listbox = tk.Listbox(self.history_frame,
                                          width=100,
                                          height=10,
                                          font=('Arial', 12),
                                          yscrollcommand=self.history_scrollbar.set)
        self.history_listbox.pack()

        self.history_scrollbar.config(command=self.history_listbox.yview)

        for item in self.history:
            self.history_listbox.insert(tk.END, item)

        def on_close():
            print("Окно истории закрыто")
            self.history_window.destroy()
            self.history_listbox = None
            self.history_window_visible = False

        def on_close_2():
            print("Основное окно закрыто")
            self.main.destroy() # закрыть основное окно
            # self.history_window.destroy() # закрыть меню истории
            self.history_listbox = None
            self.history_window_visible = False
            if os.path.exists("history.txt"):
                os.remove("history.txt")

        self.history_window.protocol("WM_DELETE_WINDOW", on_close)

        self.main.protocol("WM_DELETE_WINDOW", on_close_2)

    def _button_clicked(self, value_of_button):
        text = self.number_entry_1.get()

        # if len(text) > 20:
        #     self.expand_entry()

        if value_of_button == 'ист' and self.history_window_visible is False:
            self._show_history_window()

        # проверка, нажата ли сейчас кнопка знака и написаны ли уже два числа, если написаны
        # то нужно выполнить над ними действие, а после уже написать новый знак, чтобы не получался длинный пример
        if type(value_of_button) != int and value_of_button in '+-/*':
            if text:
                text = self.number_entry_1.get()
                if ('+' in text[0:len(text)]
                        or '-' in text[0:len(text)]
                        or '*' in text[0:len(text)]
                        or '/' in text[0:len(text)]) and text[-1] not in '+-/*' and text[-1] != 'e':
                    self._result(text, value_of_button)
                elif text[-1] in '+-/*': # если в конце есть знак, а мы нажимаем на новый, то первый меняется на новый
                    self.number_entry_1.delete(len(text) - 1, END)
                    self.number_entry_1.insert(tk.END, value_of_button)

        if text:
            if value_of_button == '=':
                if text[-1] in '+-/*.':
                    self.number_entry_1.delete(len(text)-1, END)
                    text = self.number_entry_1.get()
                self._result(text, '')
        if text:
            if value_of_button == '<--':
                self.number_entry_1.delete(len(text)-1, END)
            if value_of_button == 'C':
                self.number_entry_1.delete(0, END)
        self.number_entry_1.insert(END, value_of_button)

        text = self.number_entry_1.get()
        l = len(text)

        for i in range(l):
            if i + 1 != l:
                if text[i] == text[0] == '0' and value_of_button != '.' and text[i + 1] != '.':
                    print(text[i], 'one', i)
                    self.number_entry_1.delete(i)
                elif text[i] == '0' and text[i - 1] in '+-/*' and value_of_button != '.' and text[i + 1] != '.':
                    print(text[i], text[i - 1], 'two', i)
                    self.number_entry_1.delete(i)

    def _result(self, text, dop):
        try:
            result = calculation(text)
        except Exception as e:
            result = 'Ошибка'
            messagebox.showerror("Ошибка", f'{e}')

        self.number_entry_1.delete(0, tk.END) # очищаем
        self.number_entry_1.insert(0, str(result)+dop) # вставляем результат и знак, если он есть

        # if len(str(result)) > 20:
        #     self.expand_entry()

        # текст для истории
        record = f"{text} = {result}"
        self.history.append(record)

        # запись в файл
        with open("history.txt", "a", encoding="utf-8") as f:
            f.write(record + "\n")

        # делаем файл скрытым
        os.system("attrib +h history.txt")

        # обновление Listbox, если окно открыто
        if self.history_listbox:
            try:
                self.history_listbox.insert(tk.END, record)
            except tk.TclError:
                self.history_listbox = None  # окно было закрыто

    def is_valid_1(self, newval):
        if newval and newval[0] in "+-*/":  # проверка, что строка не начинается с оператора
            return False
        elif re.search(r"[+\-*/.]{2,}", newval):  # ищет два или более операторов подряд
            return False
        elif re.search(r"\d{" + str(13) + ",}", newval):  # ищет последовательность цифр длиннее 13
            return False
        return re.match(r'^[\d+\-*/.e]*$', newval) is not None # разрешенные символы

    # расширение виджета для чисел по мере их написания
    # def expand_entry(self):
    #     widget = self.number_entry_1
    #     content = widget.get()
    #     new_width = min(40, max(20, len(content)+1))
    #     widget.configure(width=new_width)

# анимация встряски при введении символов
# def pulse_entry(event):
#     widget = event.widget
#     def animate(step=0):
#         colors = ["#00aaff", "#66ccff", "#00aaff"]
#         widget.configure(highlightthickness=2,
#                          highlightbackground=colors[step % len(colors)],
#                          highlightcolor=colors[step % len(colors)])
#         if step < 6:
#             widget.after(100, animate, step + 1)
#         else:
#             widget.configure(highlightthickness=0)
#     animate()



