import tkinter as tk
from tkinter import ttk
from . import NumberSystems, RegularCalculator

class MainWindow:
    def __init__(self):
        # Конфигурация приложения
        self.main_window = tk.Tk()

        self.title = "Multi Tool"
        self.width = 300
        self.height = 400

        # Инициализация окна
        self._build_main_window()

        tk.mainloop()

    def _build_main_window(self):
        self.main_window.title(self.title)
        self.main_window.geometry(f"{self.width}x{self.height}")
        self.main_window.resizable(False, False) # запрет изменения размеров окна

        self._build_notebook()
        self._build_combo()
        self._build_calculator_frame()
        self._build_style()

    # создание вкладок
    def _build_notebook(self):
        self.notebook = ttk.Notebook(self.main_window)
        self.notebook.pack(fill='both', expand=True)

        self.frame_1 = ttk.Frame(self.notebook)
        self.frame_2 = ttk.Frame(self.notebook)

        self.frame_1.pack(fill='both', expand=True)
        self.frame_2.pack(fill='both', expand=True)

        self.notebook.add(self.frame_1, text="Калькулятор")
        self.notebook.add(self.frame_2, text="Конвертер форматов")

    def _build_combo(self):
        self.combo = ttk.Combobox(self.frame_1, values=["Обычный", "Системы счисления"])  # Выпадающий список
        self.combo.insert(0, "Выберите калькулятор")  # Плейсхолдер
        self.combo.config(foreground="black")

        self.combo.bind("<FocusIn>", self.on_focus_in)
        self.combo.bind("<FocusOut>", self.on_focus_out)
        self.combo.bind("<<ComboboxSelected>>", self._on_calculator_change)
        self.combo.pack(fill="x", padx=10, pady=(0, 10))

    def on_focus_in(self, event):
        if self.combo.get() == "Выберите калькулятор":
            self.combo.delete(0, "end")
            self.combo.config(foreground="black")

    def on_focus_out(self, event):
        if not self.combo.get():
            self.combo.insert(0, "Выберите калькулятор")
            self.combo.config(foreground="grey")

    def _build_calculator_frame(self):
        self.calculator_frame = tk.Frame(self.frame_1)
        self.calculator_frame.pack(fill="both", expand=True)

    def _on_calculator_change(self, event):
        for widget in self.calculator_frame.winfo_children():
            widget.destroy()

        choice = self.combo.get()
        if choice == "Обычный":
            pass
            # RegularCalculator(self.calculator_frame)
        elif choice == "Системы счисления":
            NumberSystems(self.calculator_frame)

    def _build_style(self):
        style = ttk.Style()
        style.configure("TLabel", font=("Arial", 10))
        style.configure("TCombobox", padding=5)

