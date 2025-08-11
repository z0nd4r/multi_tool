import os.path
import tkinter as tk
from getpass import win_getpass
from tkinter import filedialog, ttk, W, E, N, S, messagebox

from config import convert_image


class ImageConverter:
    def __init__(self, parent):
        self.root = parent

        self.file_path = tk.StringVar()
        self.file_name = tk.StringVar()
        self.output_path = tk.StringVar()
        self.output_path_name = tk.StringVar()

        formats = ["PNG", "JPEG", "WebP", "TIFF", "BMP", "ICO"]

        parent.grid_columnconfigure(0, weight=1)  # Column 0 expands
        parent.grid_columnconfigure(1, weight=1)  # Column 1 expands
        # parent.grid_rowconfigure(0, weight=1)  # Row 0 expands
        # parent.grid_rowconfigure(1, weight=1)

        ttk.Label(parent, text="Выберите \nизображение:").grid(row=0, column=0, sticky=W+E,  padx=15, pady=(5, 1)) # windows
        # ttk.Label(parent, text="Выберите изображение:").grid(row=0, column=0, sticky=W+E,  padx=11, pady=5) # linux
        ttk.Button(parent, text="Обзор", command=self._browse_file).grid(row=0, column=1, sticky=E, padx=15, pady=(5, 1))
        ttk.Label(parent, width=12, textvariable=self.file_name).grid(row=1, column=1, sticky=E, padx=15, pady=(0, 5))

        ttk.Label(parent, text="Выберите папку для \nсохранения:").grid(row=2, column=0, sticky=W+E, padx=15, pady=(5, 1)) # windows
        # ttk.Label(parent, text="Выберите папку для \nсохранения:").grid(row=2, column=0, sticky=W+E, padx=11, pady=5) # linux
        ttk.Button(parent, text="Обзор", command=self._browse_output_dir).grid(row=2, column=1, sticky=E, padx=15, pady=(5, 1))
        ttk.Label(parent, width=12, textvariable=self.output_path_name).grid(row=3, column=1, sticky=E, padx=15, pady=(0, 15))

        ttk.Label(parent, text='Конвертировать в').grid(row=4, column=0, sticky=W+E, padx=15, pady=(5, 5)) # windows
        # ttk.Label(parent, text='Конвертировать в').grid(row=4, column=0, sticky=W+E, padx=11, pady=5) # linux
        self.combo = ttk.Combobox(parent, width=6, values=formats, state='readonly')
        self.combo.grid(row=4, column=1, sticky=E, padx=15, pady=(5, 5))

        # button_frame = ttk.Frame(parent)
        # button_frame.grid(row=5, columnspan=2, padx=15, pady=10)
        ttk.Button(parent, text="Конвертировать", command=lambda: convert_image(self.combo,
                                                                                self.file_path,
                                                                                self.output_path)).grid(row=5, columnspan=2, padx=15, pady=20)
        # convert_button.pack()

    # открывает диалоговое окно для выбора файла изображения
    def _browse_file(self):
        filename = filedialog.askopenfilename(initialdir='.',
                                              title='Выберите изображение',
                                              filetypes=(("Image files", "*.png *.jpg *.jpeg *.bmp *.gif *.webp *.tif *.tiff *.ico"),
                                                         ("All files", "*.*")))
        print(f"Результат filedialog: {filename}")
        if filename:
            self.file_path.set(filename)
            filename, ext = os.path.splitext(os.path.basename(filename))
            self.file_name.set(f'...{filename[-5:]}{ext}')

    # открывает диалоговое окно для выбора пути сохранения
    def _browse_output_dir(self):
        output_dir = filedialog.askdirectory(initialdir='.', title='Выберите папку для сохранения')
        if output_dir:
            self.output_path.set(output_dir)
            self.output_path_name.set('.../' + os.path.basename(output_dir))


