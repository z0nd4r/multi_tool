import tkinter as tk
from tkinter import ttk

class TextFileConverter:
    def __init__(self, parent):
        self.root = parent

        self._create_interface()


    def _create_interface(self):
        self.main_frame = ttk.Frame(self.root)
        self.main_frame.pack(padx=10, pady=1)

        ttk.Label(self.main_frame, text='Скоро..').pack(pady=100)