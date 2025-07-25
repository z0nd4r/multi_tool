import tkinter as tk
from tkinter import ttk

class ImageConverter:
    def __init__(self, parent):
        self.root = parent

        self.file_path = tk.StringVar()
        self.output_path = tk.StringVar()

