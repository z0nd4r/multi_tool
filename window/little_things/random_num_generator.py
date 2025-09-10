import re
from tkinter import ttk, messagebox
from config import get_random_num

class RandomNumberGenerator:
    def __init__(self, parent):
        self.root = parent

        self._create_interface()

    def _create_interface(self):
        check_1 = (self.root.register(self.is_valid_1), "%P")

        self.root.columnconfigure(0, weight=1)  # ✅ Левый распор
        self.root.columnconfigure(1, weight=0)  #
        self.root.columnconfigure(2, weight=0)  # Центральные столбцы
        self.root.columnconfigure(3, weight=0)  #
        self.root.columnconfigure(4, weight=0)  #
        self.root.columnconfigure(5, weight=1)

        self.label_ran_num = ttk.Label(self.root, text='Случайное число:')
        self.label_ran_num.grid(row=0, column=1, pady=10, columnspan=4)

        self.label_num = ttk.Label(self.root,
                                   text='0',
                                   font=('Arial', 65))
        self.label_num.grid(row=1, column=1, columnspan=4)

        self.button = ttk.Button(self.root,
                                 text='Сгенерировать',
                                 command=self._show_generation_result)
        self.button.grid(row=2, column=1, columnspan=4)

        self.label_range = ttk.Label(self.root, text='Диапазон:')
        self.label_range.grid(row=3, column=1, columnspan=4, pady=10)

        self.label_range_of = ttk.Label(self.root, text='от')
        self.label_range_of.grid(row=4, column=1, padx=(0, 5))
        self.entry_range_of = ttk.Entry(self.root,
                                        width=5,
                                        validate='key',
                                        validatecommand=check_1)
        self.entry_range_of.grid(row=4, column=2, padx=(0, 5))
        self.entry_range_of.insert(0, 10)

        self.label_range_to = ttk.Label(self.root, text='до')
        self.label_range_to.grid(row=4, column=3, padx=(0, 5))
        self.entry_range_to = ttk.Entry(self.root,
                                        width=5,
                                        validate='key',
                                        validatecommand=check_1)
        self.entry_range_to.grid(row=4, column=4)
        self.entry_range_to.insert(0, 100)


    def _show_generation_result(self):
        try:
            of = int(self.entry_range_of.get())
            to = int(self.entry_range_to.get())

            result = get_random_num(of, to)
            print(result)

            self.label_num.config(text=result)
        except ValueError:
            messagebox.showerror('Ошибка', 'Введите диапазон чисел')

    def is_valid_1(self, newval):
        return re.match(r'^\d*$', newval) is not None