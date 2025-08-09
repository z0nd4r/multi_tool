import re
import tkinter as tk
from tkinter import ttk, END
from config import calculation


class RegularCalculator:
    def __init__(self, parent):
        self.root = parent

        self.buttons = [[7, 8, 9, '/'],
                        [4, 5, 6, '*'],
                        [1, 2, 3, '-'],
                        ['.', 0, '=', '+'],
                        ['C', '<--']]

        self.check_1 = (self.root.register(self.is_valid_1), "%P")

        self._create_interface()

    def _create_interface(self):
        self.main_frame = ttk.Frame(self.root)
        self.main_frame.pack(pady=5)

        self.number_entry_1 = ttk.Entry(self.main_frame,
                                        width=30,
                                        font=1,
                                        validate='key',
                                        validatecommand=self.check_1)
        self.number_entry_1.pack()

        self.number_entry_2 = ttk.Entry(self.main_frame,
                                        width=30,
                                        font=1,
                                        state='readonly')
        self.number_entry_2.pack()

        self.buttons_frame = ttk.Frame(self.main_frame)
        self.buttons_frame.pack()

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

    def _button_clicked(self, value_of_button):
        text = self.number_entry_1.get()
        if text:
            if value_of_button == '=':
                self._result(text)
        if text:
            if value_of_button == '<--':
                self.number_entry_1.delete(len(text)-1, END)
            if value_of_button == 'C':
                self.number_entry_1.delete(0, END)
                self.number_entry_2.config(state='normal')
                self.number_entry_2.delete(0, END)
                self.number_entry_2.config(state='readonly')
        self.number_entry_1.insert(END, value_of_button)

    def _result(self, text):
        result = calculation(text)

        self.number_entry_2.config(state='normal')
        self.number_entry_2.delete(0, END)
        self.number_entry_2.insert(0, result)
        self.number_entry_2.config(state='readonly')

    def is_valid_1(self, newval):
        if newval and newval[0] in "+-*/":  # проверка, что строка не начинается с оператора
            return False
        elif re.search(r"[+\-*/.]{2,}", newval):  # ищет два или более операторов подряд
            return False
        return re.match(r'^[\d+\-*/.]*$', newval) is not None


