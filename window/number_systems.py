import re
import tkinter as tk
from tkinter import ttk, messagebox, W, E, N, S, font, END

from config import Convert, number_check


class NumberSystems:
    def __init__(self, parent):
        self.root = parent

        self.lst = [i for i in range(2, 17)]
        self._create_interface()

    def _create_interface(self):
        # главный фрейм
        self.main_frame = ttk.Frame(self.root)
        self.main_frame.pack(padx=10, pady=1)

        check_1 = (self.root.register(self.is_valid_1), "%P")

        # фрейм для первого числа и выпадающего списка
        self.frame_1 = ttk.Frame(self.main_frame)
        self.frame_1.pack(fill='x')

        ttk.Label(self.frame_1, text="Перевести число").pack()
        self.number_entry_1 = ttk.Entry(self.frame_1,
                                        validate="key",
                                        validatecommand=check_1)
        self.number_entry_1.pack()

        ttk.Label(self.frame_1, text="из").pack()
        self.combo_1 = ttk.Combobox(self.frame_1,
                                    values=self.lst,
                                    state='readonly'
                                    )
        self.combo_1.pack()

        ttk.Label(self.frame_1, text="в").pack()
        self.combo_2 = ttk.Combobox(self.frame_1,
                                    values=self.lst,
                                    state='readonly'
                                    )
        self.combo_2.pack()

        # фрейм для результата
        self.frame_2 = ttk.Frame(self.main_frame)
        self.frame_2.pack(fill='x')

        ttk.Label(self.frame_2, text="Результат:").pack(pady=5)
        self.number_entry_2 = ttk.Entry(self.frame_2, state='readonly')
        self.number_entry_2.pack()

        ttk.Button(self.frame_2, text='Конвертировать',
                   command=self.show_conversion_result).pack(pady=15)

    def is_valid_1(self, newval):
        return re.match(r'^\d*$', newval) is not None

    def show_conversion_result(self):
        # if self.calc_1_visible:
        if self.combo_1.get() == "" or self.combo_2.get() == "" or self.number_entry_1.get() == "":
            messagebox.showerror("Ошибка", f"Не все числа введены")
            return
        elif int(self.combo_1.get()) > 16 or int(self.combo_1.get()) < 2:
            messagebox.showerror("Ошибка", f"Введите систему счисления не меньше 2 и не больше 16")
            return
        elif int(self.combo_2.get()) > 16 or int(self.combo_2.get()) < 2:
            messagebox.showerror("Ошибка", f"Введите систему счисления не меньше 2 и не больше 16")
            return
        elif number_check(self.number_entry_1.get(), int(self.combo_1.get())):
            return

        try:
            converter = Convert(
                int(self.number_entry_1.get()),
                int(self.combo_1.get()),
                int(self.combo_2.get())
            )
            result = converter.convert()

            # Обновляем результат во frame_3
            self.number_entry_2.config(state='normal')
            self.number_entry_2.delete(0, 'end')
            self.number_entry_2.insert(0, result)
            self.number_entry_2.config(state='readonly')

        except ValueError as e:
            messagebox.showerror("Ошибка", f"Не все числа введены или вы ввели число меньше 1")











