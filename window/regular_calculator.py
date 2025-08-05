import tkinter as tk
from tkinter import ttk

class RegularCalculator:
    def __init__(self, parent):
        self.root = parent

        self._create_interface()

    def _create_interface(self):
        self.main_frame = ttk.Frame(self.root)
        self.main_frame.pack(padx=10, pady=1)

        tk.Label(self.main_frame, text='Скоро..').pack(pady=100)
