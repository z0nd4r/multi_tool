import tkinter as tk
from tkinter import ttk
from check_version import CURRENT_VERSION, update_app

class Menu:
    def __init__(self, parent, notebook):

        self.header = tk.Frame(parent, height=50)
        self.header.pack(fill="x")

        self.button = ttk.Button(self.header, text="≡ Меню", command=self._toggle_menu)
        self.button.pack(side="left")

        self.menu_frame = tk.Frame(notebook, width=3300, height=100)
        self.menu_visible = False

        ttk.Label(self.menu_frame, text=f'App version: {CURRENT_VERSION}').grid(row=0, column=0, padx=15)
        ttk.Label(self.menu_frame, text='created by zondar__').grid(row=1, column=0, padx=15)
        ttk.Button(self.menu_frame, text='Обновить', command=lambda: update_app(parent)).grid(row=0, column=1, padx=15)



    def _toggle_menu(self):
        if self.menu_visible:
            self.menu_frame.place_forget()
        else:
            self.menu_frame.place(relx=0.0, rely=0.85)
        self.menu_visible = not self.menu_visible


