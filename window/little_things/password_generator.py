import re
from tkinter import ttk, messagebox
import tkinter as tk

from config import get_random_password

class PasswordGenerator:
    def __init__(self, parent):
        self.root = parent

        self.check_var = tk.IntVar()

        self._create_interface()

    def _create_interface(self):
        check_1 = (self.root.register(self.is_valid_1), "%P")

        self.root.columnconfigure(0, weight=1)  # левый отступ
        self.root.columnconfigure(1, weight=0)  #
        self.root.columnconfigure(2, weight=0)  # центральные столбцы
        self.root.columnconfigure(3, weight=0)  #
        self.root.columnconfigure(4, weight=0)  #
        self.root.columnconfigure(5, weight=1)  # правый отступ

        self.password_label = tk.Label(self.root,
                                       text='Тут будет пароль',
                                       cursor='hand2',)
        self.password_label.grid(row=0, column=1, columnspan=4, pady=15)

        self.button = ttk.Button(self.root, text='Сгенерировать', command=self._show_generation_result)
        self.button.grid(row=1, column=1, columnspan=4, pady=5)

        self.len_password_entry = ttk.Entry(self.root,
                                            width=3,
                                            validate='key',
                                            validatecommand=check_1
                                            )
        self.len_password_entry.grid(row=2, column=2, pady=(15,5), padx=3, sticky='e')
        self.len_password_entry.insert(0, 10)

        self.len_password_label = ttk.Label(self.root, text='- длина пароля')
        self.len_password_label.grid(row=2, column=3, pady=(15,5), padx=3, sticky='w')


        # self.symbols_label = ttk.Label(self.root, text='Спецсимволы:')
        # self.symbols_label.grid(row=3, column=2, pady=5, padx=0, sticky='e')

        self.symbols_checkbutton = ttk.Checkbutton(self.root, text='спецсимволы', variable=self.check_var)
        self.symbols_checkbutton.grid(row=3, column=1, columnspan=4, pady=5, padx=5)

        self.password_label.bind("<Button-1>", self._copy_password)

    def _show_generation_result(self):
        try:
            len_pass = int(self.len_password_entry.get())
            if len_pass > 40:
                messagebox.showerror('Ошибка', 'Введите длину пароля\nне более 40')
                return

            # проверка чебокс
            if self.check_var.get() == 1:
                type_pass = True
            else:
                type_pass = False

            result = get_random_password(len_pass, type_pass)

            self.password_label.config(text=result)
        except ValueError:
            messagebox.showerror('Ошибка', 'Введите длину пароля')

    def _copy_password(self, event):
        self.password_label.clipboard_clear()
        self.password_label.clipboard_append(self.password_label.cget("text"))
        self.password_label.update()

        original_text = self.password_label.cget("text")

        # визуальное подтверждение
        original_bg = self.password_label.cget("bg")
        self.password_label.config(bg="#d4edda", text="✓ Скопировано!")

        self.root.after(1500, lambda: self.password_label.config(bg=original_bg,
                                                                 text=original_text))

    def is_valid_1(self, newval):
        return re.match(r'^\d*$', newval) is not None
