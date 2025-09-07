import tkinter as tk
import tkinter.font as font
from tkinter import ttk, messagebox

from check_version import CURRENT_VERSION, update_app
from . import NumberSystems, ImageConverter, RegularCalculator, TextFileConverter

import ctypes
import platform

class MainWindow:
    def __init__(self):
        # Конфигурация приложения
        self.main_window = tk.Tk()

        self.main_window.tk.call('tk', 'scaling', 2)

        self.default_font = font.nametofont("TkDefaultFont")

        self.selected_tab_index = 0 # номер страницы инструмента

        if platform.system() == 'Windows':
            ctypes.windll.shcore.SetProcessDpiAwareness(2)
            self.default_font.configure(size=10)
            self.width = 450
            self.height = 550
        else:
            self.default_font.configure(size=11)
            self.width = 350
            self.height = 450

        self.title = "Multi Tool"

        # получаем ширину и высоту экрана
        self.ws = self.main_window.winfo_screenwidth()
        self.hs = self.main_window.winfo_screenheight()

        # Инициализация окна
        self._build_main_window()

        # Menu(self.main_window)

        tk.mainloop()

    def _build_main_window(self):
        x = (self.ws / 2) - (self.width / 2)
        y = (self.hs / 2) - (self.height / 2)

        self.main_window.title(self.title)
        self.main_window.geometry('%dx%d+%d+%d' % (self.width, self.height, x, y)) # окно появляется посередине
        self.main_window.minsize(self.width, self.height)
        # self.main_window.resizable(False, False) # запрет изменения размеров окна

        self._build_main_menu()

        self._build_tools_frames()

        self._build_menu()

        self._build_converter_frame()
        self._build_calculator_frame()

        self._build_combo_converter()
        self._build_combo_calculator()

        self._build_style()

    # создание основного меню
    def _build_main_menu(self):
        self.main_window.option_add("*tearOff", False)

        self.main_menu = tk.Menu()
        # self.file_menu = tk.Menu()
        self.tools_menu = tk.Menu()
        self.ref_menu = tk.Menu()

        self.tools_menu.add_command(label='Обновление', command=update_app)

        self.ref_menu.add_command(label='О программе', command=self._check_info)

        # self.main_menu.add_cascade(label='Файл')
        self.main_menu.add_cascade(label='Инструменты', menu=self.tools_menu)
        self.main_menu.add_cascade(label='Справка', menu=self.ref_menu)

        self.main_window.config(menu=self.main_menu)

    # создание вкладок
    def _build_tools_frames(self):
        # self.notebook = ttk.Notebook(self.main_window)
        # self.notebook.pack(fill='both', expand=True)

        self.frame_1 = ttk.Frame(self.main_window)
        self.frame_2 = ttk.Frame(self.main_window)

        self.frame_1_visible = False
        self.frame_2_visible = False

        # self.notebook.add(self.frame_1, text="Конвертер")
        # self.notebook.add(self.frame_2, text="Калькулятор")

    # выпадающий список
    def _build_combo(self, frame_top, values, value, frame_down):
        self.combo = ttk.Combobox(frame_top, values=values, font=self.default_font, state="readonly")  # Выпадающий список
        if value == 0:
            self.combo.set('Выберите калькулятор')  # Плейсхолдер
        elif value == 1:
            self.combo.set('Выберите конвертер')  # Плейсхолдер

        self.combo.config(foreground="black")

        self.combo.bind("<FocusIn>", lambda event: self.on_focus_in(event, value))
        self.combo.bind("<FocusOut>", lambda event: self.on_focus_out(event, value))
        self.combo.bind("<<ComboboxSelected>>", lambda event: self._on_change(event, frame_down))
        self.combo.pack(fill="x", padx=10, pady=(5, 5))

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

        if self.selected_tab_index == 1:
            combo = self.combo_converter
        elif self.selected_tab_index == 2:
            combo = self.combo_calculator

        choice = combo.get()
        # print(choice)
        if choice == "Обычный":
            RegularCalculator(self.calculator_frame, self.main_window)
        elif choice == "Системы счисления":
            NumberSystems(self.calculator_frame)
        elif choice == "Текстовые файлы":
            TextFileConverter(self.converter_frame)
        elif choice == "Изображения":
            ImageConverter(self.converter_frame)

    def _build_style(self):
        style = ttk.Style()
        style.configure("TLabel", font=self.default_font)
        style.configure("TCombobox", padding=5)

    def _check_info(self):
        # self.label_email = ttk.Label(text='zondar.multi.tool@yandex.ru')
        #
        # messagebox.showinfo('О программе', f'App version: {CURRENT_VERSION}\ncreated by zondar__'
        #                                    f'\nОбратная связь: {self.label_email}')

        self.info = tk.Toplevel()
        self.info.title("О программе")
        self.info.geometry("345x100")
        self.info.resizable(False, False)

        # центрируем
        self.info.transient(self.info.master)
        self.info.grab_set()

        ttk.Label(self.info,
                  text=f'App version: {CURRENT_VERSION}').grid(row=0, column=0, columnspan=2, pady=5)
        ttk.Label(self.info,
                  text=f'created by zondar__').grid(row=1, column=0, columnspan=2, pady=5)
        ttk.Label(self.info,
                  text=f'Обратная связь:').grid(row=2, column=0, pady=5, padx=(10, 1))

        self.email_label = tk.Label(self.info,
                                    text="zondar.multi.tool@yandex.ru",
                                    width=25,
                                    justify='center',
                                    cursor='hand2',
                                    relief='flat',
                                    font=self.default_font)
        self.email_label.grid(row=2, column=1, pady=5, padx=(1, 10))

        def copy_email(event):
            self.email_label.clipboard_clear()
            self.email_label.clipboard_append('zondar.multi.tool@yandex.ru')
            self.email_label.update()

            # визуальное подтверждение
            original_bg = self.email_label.cget("bg")
            self.email_label.config(bg="#d4edda", text="✓ Скопировано!")

            # Возвращаем обратно через 1.5 секунды
            self.info.after(1500, lambda: self.email_label.config(bg=original_bg,
                                                                  text="zondar.multi.tool@yandex.ru"))

        self.email_label.bind("<Button-1>", copy_email)

    def toggle_frames(self, frame):
        if frame == 1 and not self.frame_1_visible:
            if self.frame_2_visible:
                self.frame_2.pack_forget()
                self.frame_2_visible = not self.frame_2_visible
            self.frame_1.pack(fill='both', expand=True)
            self.selected_tab_index = 1
            self.frame_1_visible = not self.frame_1_visible

        elif frame == 2 and not self.frame_2_visible:
            if self.frame_1_visible:
                self.frame_1.pack_forget()
                self.frame_1_visible = not self.frame_1_visible
            self.frame_2.pack(fill='both', expand=True)
            self.selected_tab_index = 2
            self.frame_2_visible = not self.frame_2_visible

    def _build_menu(self):
        self.header = tk.Frame(self.main_window, height=50)
        self.header.pack(fill="x", side='bottom')

        toggle_frames = MainWindow.toggle_frames

        '''
        Кнопка меню
        '''
        self.menu_button = ttk.Button(self.header, text="≡ Меню", command=self._toggle_menu, width=10)
        self.menu_button.pack(side="left")

        parent = self.main_window
        if self.frame_1_visible:
            parent = self.frame_1
        elif self.frame_2_visible:
            parent = self.frame_2

        self.menu_frame = tk.Frame(parent,
                                   pady=10,
                                   relief='groove',
                                   borderwidth=2)
        self.menu_visible = False

        # ttk.Button(self.menu_frame, text='Конвертер').pack(fill='x', side='left')
        # ttk.Button(self.menu_frame, text='Калькулятор').pack(fill='x', side='bottom')

        # self.menu_frame.grid_columnconfigure(0, weight=1)
        # self.menu_frame.grid_columnconfigure(1, weight=1)

        ttk.Button(self.menu_frame, text='Конвертер',
                   width=20,
                   command=lambda: self.toggle_frames(1)).grid(row=0, column=0, padx=15, sticky='w')
        ttk.Button(self.menu_frame, text='Калькулятор',
                   width=20,
                   command=lambda: self.toggle_frames(2)).grid(row=1, column=0, padx=15, sticky='w')
        ttk.Button(self.menu_frame, text='Скоро..',
                   width=20,
                   command=lambda: self.toggle_frames(3)).grid(row=2, column=0, padx=15, sticky='w')

        '''
        Кнопка инфо
        '''
        # self.info_button = ttk.Button(self.header, text='Инфо', command=self._toggle_info)
        # self.info_button.pack(side="left")
        #
        # self.info_frame = tk.Frame(notebook, pady=10)
        # self.info_visible = False
        #
        # self.info_frame.grid_columnconfigure(0, weight=1)
        # self.info_frame.grid_columnconfigure(1, weight=1)
        #
        # ttk.Label(self.info_frame, text=f'App version: {CURRENT_VERSION}').grid(row=0, column=0, padx=15)
        # ttk.Label(self.info_frame, text='created by zondar__').grid(row=1, column=0, padx=15)
        # ttk.Button(self.info_frame, text='Обратная связь').grid(row=0, column=1, padx=15)

        self.main_window.bind("<Button-1>", self.hide_frame_on_click)

    # показать/скрыть меню
    def _toggle_menu(self):
        if self.menu_visible:
            self.menu_frame.place_forget()
        else:
            # if self.info_visible:
            #     self.info_frame.pack_forget()
            #     self.info_visible = not self.info_visible
            if platform.system() == 'Windows':
                self.menu_frame.place(x=0, y=370)
            else:
                self.menu_frame.place(x=0, y=299)
        self.menu_visible = not self.menu_visible

    # def _toggle_info(self):
    #     if self.info_visible:
    #         self.info_frame.pack_forget()
    #     else:
    #         if self.menu_visible:
    #             self.menu_frame.pack_forget()
    #             self.menu_visible = not self.menu_visible
    #         self.info_frame.pack(fill='x', side='bottom')
    #     self.info_visible = not self.info_visible

    def hide_frame_on_click(self, event):
        """Скрывает фрейм при клике вне его области"""
        clicked_widget = event.widget.winfo_containing(event.x_root, event.y_root)

        if (clicked_widget != self.menu_button and clicked_widget not in self.menu_frame.winfo_children() +
                [self.menu_frame]):
            if self.menu_visible:
                self.menu_frame.place_forget()
                self.menu_visible = not self.menu_visible

