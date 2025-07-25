import re
import tkinter as tk
from tkinter import ttk, messagebox

from config import Convert

class NumberSystems:
    def __init__(self, parent):
        self.root = parent

        self.lst = [i for i in range(1, 17)]
        self._create_interface()

    def _create_interface(self):
        # главный фрейм
        self.main_frame = tk.Frame(self.root)
        self.main_frame.pack(padx=10, pady=10)

        check_1 = (self.root.register(self.is_valid_1), "%P")
        check_2 = (self.root.register(self.is_valid_2), "%P")

        # фрейм для первого числа и выпадающего списка
        self.frame_1 = tk.Frame(self.main_frame)
        self.frame_1.pack(fill='x')

        tk.Label(self.frame_1, text=" Перевести число").pack()
        self.number_entry_1 = tk.Entry(self.frame_1,
                                       validate="key",
                                       validatecommand=check_1)
        self.number_entry_1.pack()

        tk.Label(self.frame_1, text="из десятичной").pack()
        # self.combo_1 = ttk.Combobox(self.frame_1, values=self.lst)
        # self.combo_1.pack()

        # фрейм для второго выпадаюзего списка
        self.frame_2 = tk.Frame(self.main_frame)
        self.frame_2.pack(fill='x')

        tk.Label(self.frame_2, text="в").pack()
        self.combo_2 = ttk.Combobox(self.frame_2,
                                    values=self.lst,
                                    validate="key",
                                    validatecommand=check_2
                                    )
        self.combo_2.pack()

        # фрейм для результата
        self.frame_3 = tk.Frame(self.main_frame)
        self.frame_3.pack(fill='x')

        tk.Label(self.frame_3, text="Результат:").pack()
        self.number_entry_2 = tk.Entry(self.frame_3)
        self.number_entry_2.pack()

        btn_frame = tk.Frame(self.main_frame)
        btn_frame.pack(pady=10)
        tk.Button(btn_frame, text="Конвертировать",
                  command=lambda: self.show_conversion_result()).pack()

    def is_valid_1(self, newval):
        return re.match(r'^\d*$', newval) is not None

    def is_valid_2(self, newval):
        return re.match(r'^\d{0,2}$', newval) is not None

    def show_conversion_result(self):
        if int(self.combo_2.get()) > 16:
            messagebox.showerror("Ошибка", f"Введите систему счисления не больше 16")
            return

        try:
            converter = Convert(
                int(self.number_entry_1.get()),
                int(self.combo_2.get())
            )
            result = converter.convert_1()

            # Обновляем результат во frame_3
            self.number_entry_2.config(state='normal')
            self.number_entry_2.delete(0, 'end')
            self.number_entry_2.insert(0, result)
            self.number_entry_2.config(state='readonly')

        except ValueError as e:
            messagebox.showerror("Ошибка", f"Не все числа введены")











