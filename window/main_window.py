import tkinter as tk
from tkinter import ttk
from . import NumberSystems, ImageConverter


class MainWindow:
    def __init__(self):
        # Конфигурация приложения
        self.main_window = tk.Tk()

        self.main_window.tk.call('tk', 'scaling', 1.5)

        self.title = "Multi Tool"
        self.width = 324
        self.height = 400

        # Инициализация окна
        self._build_main_window()

        tk.mainloop()

    def _build_main_window(self):
        self.main_window.title(self.title)
        self.main_window.geometry(f"{self.width}x{self.height}")
        self.main_window.resizable(False, False) # запрет изменения размеров окна

        self._build_notebook()
        self._build_converter_frame()
        self._build_calculator_frame()

        self._build_combo_converter()
        self._build_combo_calculator()

        self._build_style()

    # создание вкладок
    def _build_notebook(self):
        self.notebook = ttk.Notebook(self.main_window)
        self.notebook.pack(fill='both', expand=True)

        self.frame_1 = ttk.Frame(self.notebook)
        self.frame_2 = ttk.Frame(self.notebook)

        self.frame_1.pack(fill='both', expand=True)
        self.frame_2.pack(fill='both', expand=True)

        self.notebook.add(self.frame_1, text="Конвертер")
        self.notebook.add(self.frame_2, text="Калькулятор")

    # выпадающий список
    def _build_combo(self, frame_top, values, value, frame_down):
        self.combo = ttk.Combobox(frame_top, values=values)  # Выпадающий список
        if value == 0:
            self.combo.insert(45, 'Выберите калькулятор')  # Плейсхолдер
        elif value == 1:
            self.combo.insert(45, 'Выберите конвертер')  # Плейсхолдер

        self.combo.config(foreground="black")

        self.combo.bind("<FocusIn>", lambda event: self.on_focus_in(event, value))
        self.combo.bind("<FocusOut>", lambda event: self.on_focus_out(event, value))
        self.combo.bind("<<ComboboxSelected>>", lambda event: self._on_change(event, frame_down))
        self.combo.pack(fill="x", padx=10, pady=(5, 10))

        return self.combo

    def _build_combo_converter(self):
        values = ["Изображения", "Текстовые файлы"]
        value = 1
        self.combo_converter = self._build_combo(self.frame_1, values, value, self.converter_frame)

    def _build_combo_calculator(self):
        values = ["Обычный", "Системы счисления"]
        value = 0
        self.combo_calculator = self._build_combo(self.frame_2, values, value, self.calculator_frame)

    def on_focus_in(self, event, value):
        if self.combo.get() == value:
            self.combo.delete(0, "end")
            self.combo.config(foreground="black")

    def on_focus_out(self, event, value):
        if not self.combo.get():
            self.combo.insert(0, value)
            self.combo.config(foreground="grey")

    def _build_converter_frame(self):
        self.converter_frame = ttk.Frame(self.frame_1)
        self.converter_frame.pack(side='bottom', fill="both", expand=True)

    def _build_calculator_frame(self):
        self.calculator_frame = ttk.Frame(self.frame_2)
        self.calculator_frame.pack(side='bottom', fill="both", expand=True)

    def _on_change(self, event, frame):
        for widget in frame.winfo_children():
            widget.destroy()

        selected_tab_index = self.notebook.index("current")

        if selected_tab_index == 0:
            combo = self.combo_converter
        elif selected_tab_index == 1:
            combo = self.combo_calculator

        choice = combo.get()
        # print(choice)
        if choice == "Обычный":
            pass
            # RegularCalculator(self.calculator_frame)
        elif choice == "Системы счисления":
            NumberSystems(self.calculator_frame)
        elif choice == 'Изображения':
            ImageConverter(self.converter_frame)

    def _build_style(self):
        style = ttk.Style()
        style.configure("TLabel", font=("Arial", 10))
        style.configure("TCombobox", padding=5)

