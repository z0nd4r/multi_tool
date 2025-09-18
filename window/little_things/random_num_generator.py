import re
import tkinter as tk
from tkinter import ttk, messagebox
from config import get_random_num

class RandomNumberGenerator:
    def __init__(self, parent):
        self.root = parent

        self._create_interface()

    def _create_interface(self):
        check_1 = (self.root.register(self.is_valid_1), "%P")

        self.root.columnconfigure(0, weight=1)  # левый отступ
        self.root.columnconfigure(1, weight=0)  #
        self.root.columnconfigure(2, weight=0)  # центральные столбцы
        self.root.columnconfigure(3, weight=0)  #
        self.root.columnconfigure(4, weight=0)  #
        self.root.columnconfigure(5, weight=1)  # правый отступ

        self.label_ran_num = ttk.Label(self.root, text='Случайное число:')
        self.label_ran_num.grid(row=0, column=2, pady=10, columnspan=2)

        self.label_num = ttk.Label(self.root,
                                   text='0',
                                   font=('Arial', 65))
        self.label_num.grid(row=1, column=2, columnspan=2)

        self.button = ttk.Button(self.root,
                                 text='Сгенерировать',
                                 command=self._show_generation_result)
        self.button.grid(row=2, column=1, columnspan=4)

        self.type_of_range = tk.StringVar(value='range')

        self.radio_button_range = ttk.Radiobutton(self.root,
                                                 text='из диапазона',
                                                 value='range',
                                                 variable=self.type_of_range,
                                                 command=self._select_type_of_range)
        self.radio_button_range.grid(row=3, column=2, pady=10, padx=(0, 5), sticky='e')

        self.radio_button_range = ttk.Radiobutton(self.root,
                                                 text='из списка',
                                                 value='list',
                                                 variable=self.type_of_range,
                                                 command=self._select_type_of_range)
        self.radio_button_range.grid(row=3, column=3, pady=10, sticky='w')

        # self.label_range = ttk.Label(self.root, text='Диапазон:')
        # self.label_range.grid(row=3, column=1, columnspan=4, pady=10)

        # фрейм для диапазона
        self.range_frame = ttk.Frame(self.root)
        self.range_frame.grid(row=4, column=1, columnspan=4, pady=10)
        self.range_frame_visible = True

        self.label_range_of = ttk.Label(self.range_frame, text='от')
        self.label_range_of.grid(row=0, column=1, padx=(0, 5))
        self.entry_range_of = ttk.Entry(self.range_frame,
                                        width=5,
                                        validate='key',
                                        validatecommand=check_1)
        self.entry_range_of.grid(row=0, column=2, padx=(0, 5))
        self.entry_range_of.insert(0, 10)

        self.label_range_to = ttk.Label(self.range_frame, text='до')
        self.label_range_to.grid(row=0, column=3, padx=(0, 5))
        self.entry_range_to = ttk.Entry(self.range_frame,
                                        width=5,
                                        validate='key',
                                        validatecommand=check_1)
        self.entry_range_to.grid(row=0, column=4)
        self.entry_range_to.insert(0, 100)

        # фрейм для диапазона из списка
        self.range_list_frame = ttk.Frame(self.root)
        self.range_list_frame.grid(row=4, column=1, columnspan=4, pady=10)
        self.range_list_frame_visible = False

        self.entry_list = ttk.Entry(self.range_list_frame)
        self.entry_list.grid(row=0, column=1)
        self.label_list = ttk.Label(self.range_list_frame, text='напишите числа через пробел')
        self.label_list.grid(row=1, column=1)

        self.range_list_frame.grid_remove() # убираем видимость фрейма, чтобы потом показать

    # выводим результат
    def _show_generation_result(self):
        try:
            if self.range_frame_visible:
                of = int(self.entry_range_of.get())
                to = int(self.entry_range_to.get())

                result = get_random_num(None, of, to)

            elif self.range_list_frame_visible:
                lst = self.entry_list.get()
                if len(lst) < 1:
                    messagebox.showerror('Ошибка', 'Введите диапазон чисел')
                    return

                result = get_random_num(lst)

            self.label_num.config(text=result)
        except ValueError:
            messagebox.showerror('Ошибка', 'Введите диапазон чисел')

    def is_valid_1(self, newval):
        return re.match(r'^\d*$', newval) is not None

    # показываем фрейм либо с диапазоном из двух чисел, либо со списком
    def _select_type_of_range(self):
        print(self.type_of_range.get())
        if self.type_of_range.get() == 'range':
            self.range_frame.grid()
            self.range_list_frame.grid_remove()
            self.range_frame_visible = not self.range_frame_visible
            self.range_list_frame_visible = not self.range_list_frame_visible
        elif self.type_of_range.get() == 'list':
            self.range_list_frame.grid()
            self.range_frame.grid_remove()
            self.range_list_frame_visible = not self.range_list_frame_visible
            self.range_frame_visible = not self.range_frame_visible
