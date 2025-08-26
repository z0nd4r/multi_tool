import tkinter as tk
from tkinter import ttk, E
from check_version import CURRENT_VERSION, update_app

class Menu:
    def __init__(self, parent, notebook):
        self.header = tk.Frame(parent, height=50)
        self.header.pack(fill="x")

        '''
        Кнопка меню
        '''
        self.menu_button = ttk.Button(self.header, text="≡ Меню", command=self._toggle_menu)
        self.menu_button.pack(side="left")

        self.menu_frame = tk.Frame(notebook, pady=10)
        self.menu_visible = False

        self.menu_frame.grid_columnconfigure(0, weight=1)
        self.menu_frame.grid_columnconfigure(1, weight=1)

        ttk.Label(self.menu_frame, text=f'App version: {CURRENT_VERSION}').grid(row=0, column=0, padx=15)
        ttk.Label(self.menu_frame, text='created by zondar__').grid(row=1, column=0, padx=15)
        ttk.Button(self.menu_frame, text='Обновить', command=lambda: update_app(parent)).grid(row=0, column=1, padx=15)

        '''
        Кнопка инфо
        '''
        self.info_button = ttk.Button(self.header, text='Инфо', command=self._toggle_info)
        self.info_button.pack(side="left")

        self.info_frame = tk.Frame(notebook, pady=10)
        self.info_visible = False

        self.info_frame.grid_columnconfigure(0, weight=1)
        self.info_frame.grid_columnconfigure(1, weight=1)

        ttk.Label(self.info_frame, text=f'App version: {CURRENT_VERSION}').grid(row=0, column=0, padx=15)
        ttk.Label(self.info_frame, text='created by zondar__').grid(row=1, column=0, padx=15)
        ttk.Button(self.info_frame, text='Обратная связь').grid(row=0, column=1, padx=15)

    def _toggle_menu(self):
        if self.menu_visible:
            self.menu_frame.pack_forget()
        else:
            if self.info_visible:
                self.info_frame.pack_forget()
                self.info_visible = not self.info_visible
            self.menu_frame.pack(fill='x', side='bottom')
        self.menu_visible = not self.menu_visible

    def _toggle_info(self):
        if self.info_visible:
            self.info_frame.pack_forget()
        else:
            if self.menu_visible:
                self.menu_frame.pack_forget()
                self.menu_visible = not self.menu_visible
            self.info_frame.pack(fill='x', side='bottom')
        self.info_visible = not self.info_visible


