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
        self.main_frame.pack(padx=10, pady=10)

        check_1 = (self.root.register(self.is_valid_1), "%P")
        check_2 = (self.root.register(self.is_valid_2), "%P")

        # КАЛЬКУЛЯТОР №1
        self.calc_1_visible = True

        # фрейм для первого числа и выпадающего списка
        self.frame_1 = ttk.Frame(self.main_frame)
        self.frame_1.pack(fill='x')

        ttk.Label(self.frame_1, text="Перевести число").pack()
        self.number_entry_1 = ttk.Entry(self.frame_1,
                                       validate="key",
                                       validatecommand=check_1)
        self.number_entry_1.pack()

        ttk.Label(self.frame_1, text="из десятичной").pack()

        ttk.Label(self.frame_1, text="в").pack()
        self.combo_1 = ttk.Combobox(self.frame_1,
                                    values=self.lst,
                                    validate="key",
                                    validatecommand=check_2
                                    )
        self.combo_1.pack()

        # КАЛЬКУЛЯТОР №2
        self.frame_1_1 = ttk.Frame(self.main_frame)

        ttk.Label(self.frame_1_1, text="Перевести число").pack()
        self.number_entry_1_1 = ttk.Entry(self.frame_1_1,
                                       validate="key",
                                       validatecommand=check_1)
        self.number_entry_1_1.pack()

        ttk.Label(self.frame_1_1, text="из").pack()
        self.combo_1_1 = ttk.Combobox(self.frame_1_1, values=self.lst)
        self.combo_1_1.pack()

        ttk.Label(self.frame_1_1, text="в десятичную").pack()

        # фрейм для результата
        self.frame_2 = ttk.Frame(self.main_frame)
        self.frame_2.pack(fill='x')

        ttk.Label(self.frame_2, text="Результат:").pack(pady=5)
        self.number_entry_2 = ttk.Entry(self.frame_2)
        self.number_entry_2.pack()

        btn_frame = ttk.Frame(self.main_frame)
        btn_frame.pack(fill='x', pady=15)

        # linux
        # large_button_font = font.Font(family="Arial", size=14, weight="bold")
        # s = ttk.Style()
        # s.configure('BigArrow.TButton',
        #             font=large_button_font,
        #             width=2,
        #             height=2,
        #             padding=[2, 2, 2, 1.9]) # стиль для кнопки со стрелками
        #
        # ttk.Button(btn_frame, text="Конвертировать",
        #            command=self.show_conversion_result).pack(side='left', padx=(37, 7), expand=True)
        # ttk.Button(btn_frame, text="⮀", style='BigArrow.TButton', command=self._change_calculator).pack(side='right')

        # windows
        large_button_font = font.Font(family="Arial", size=13, weight="bold")
        s = ttk.Style()
        s.configure('BigArrow.TButton',
                    font=large_button_font,
                    width=2,
                    height=2,
                    padding=[0.2, 0.2, 0.2, 0.2]) # стиль для кнопки со стрелками

        ttk.Button(btn_frame, text="Конвертировать",
                   command=self.show_conversion_result).pack(side='left', padx=(33, 7), expand=True)
        ttk.Button(btn_frame, text="⮀", style='BigArrow.TButton', command=self._change_calculator).pack(side='right')


    def is_valid_1(self, newval):
        return re.match(r'^\d*$', newval) is not None

    def is_valid_2(self, newval):
        return re.match(r'^\d{0,2}$', newval) is not None

    def show_conversion_result(self):
        if self.calc_1_visible:
            if self.combo_1.get() == "" or self.number_entry_1.get() == "":
                messagebox.showerror("Ошибка", f"Не все числа введены")
                return
            elif int(self.combo_1.get()) > 16 or int(self.combo_1.get()) < 2:
                messagebox.showerror("Ошибка", f"Введите систему счисления не меньше 2 и не больше 16")
                return

            try:
                converter = Convert(
                    int(self.number_entry_1.get()),
                    int(self.combo_1.get())
                )
                result = converter.convert_1()

                # Обновляем результат во frame_3
                self.number_entry_2.config(state='normal')
                self.number_entry_2.delete(0, 'end')
                self.number_entry_2.insert(0, result)
                self.number_entry_2.config(state='readonly')

            except ValueError as e:
                messagebox.showerror("Ошибка", f"Не все числа введены или вы ввели число меньше 1")

        else:
            if self.combo_1_1.get() == "" or self.number_entry_1_1.get() == "":
                messagebox.showerror("Ошибка", f"Не все числа введены")
                return
            elif int(self.combo_1_1.get()) > 16 or int(self.combo_1_1.get()) < 2:
                messagebox.showerror("Ошибка", f"Введите систему счисления не меньше 2 и не больше 16")
                return
            elif number_check(self.number_entry_1_1.get(), int(self.combo_1_1.get())):
                return

            try:
                converter = Convert(
                    int(self.number_entry_1_1.get()),
                    int(self.combo_1_1.get())
                )
                result = converter.convert_2()
                print(result)

                # Обновляем результат во frame_3
                self.number_entry_2.config(state='normal')
                self.number_entry_2.delete(0, 'end')
                self.number_entry_2.insert(0, result)
                self.number_entry_2.config(state='readonly')

            except ValueError as e:
                messagebox.showerror("Ошибка", f"Не все числа введены или вы ввели число меньше 1")

    def _change_calculator(self):
        if self.calc_1_visible:
            self.frame_1_1.place(relx=0, rely=0, relwidth=1, relheight=1)
            self.number_entry_2.config(state='normal')
            self.number_entry_2.delete(0, 'end')
            self.number_entry_2.config(state='readonly')
        else:
            self.frame_1_1.place_forget()
            self.number_entry_2.config(state='normal')
            self.number_entry_2.delete(0, 'end')
            self.number_entry_2.config(state='readonly')

        self.calc_1_visible = not self.calc_1_visible











