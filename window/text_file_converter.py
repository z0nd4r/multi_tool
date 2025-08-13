import os.path
import tkinter as tk
from tkinter import filedialog, ttk, W, E, N, S, messagebox

from config import convert_text


class TextFileConverter:
    def __init__(self, parent):
        self.root = parent

        self._create_interface()

    def _create_interface(self):
        self.file_path = tk.StringVar()
        self.file_name = tk.StringVar()
        self.output_path = tk.StringVar()
        self.output_path_name = tk.StringVar()

        self.formats = ["TXT", "PDF", "DOCX"]

        self.root.grid_columnconfigure(0, weight=1)  # Column 0 expands
        self.root.grid_columnconfigure(1, weight=1)  # Column 1 expands
        # parent.grid_rowconfigure(0, weight=1)  # Row 0 expands
        # parent.grid_rowconfigure(1, weight=1)

        ttk.Label(self.root, text="Выберите \nтекстовый файл:").grid(row=0, column=0, sticky=W + E, padx=15,
                                                                     pady=(5, 1))  # windows
        ttk.Button(self.root, text="Обзор", command=self._browse_file).grid(row=0, column=1, sticky=E, padx=15,
                                                                            pady=(5, 1))
        ttk.Label(self.root, width=12, textvariable=self.file_name).grid(row=1, column=1, sticky=E, padx=15, pady=(0, 5))

        ttk.Label(self.root, text="Выберите папку для \nсохранения:").grid(row=2, column=0, sticky=W + E, padx=15,
                                                                           pady=(5, 1))  # windows
        ttk.Button(self.root, text="Обзор", command=self._browse_output_dir).grid(row=2, column=1, sticky=E, padx=15,
                                                                                  pady=(5, 1))
        ttk.Label(self.root, width=12, textvariable=self.output_path_name).grid(row=3, column=1, sticky=E, padx=15,
                                                                                pady=(0, 15))

        ttk.Label(self.root, text='Конвертировать в').grid(row=4, column=0, sticky=W + E, padx=15, pady=(5, 5))  # windows
        self.combo = ttk.Combobox(self.root, width=6, values=self.formats, state='readonly')
        self.combo.grid(row=4, column=1, sticky=E, padx=15, pady=(5, 5))

        ttk.Button(self.root, text="Конвертировать", command=lambda: convert_text(self.combo,
                                                                                  self.file_path,
                                                                                  self.output_path)).grid(row=5,
                                                                                                          columnspan=2,
                                                                                                          padx=15,
                                                                                                          pady=20)

    # открывает диалоговое окно для выбора текстового файла
    def _browse_file(self):
        filename = filedialog.askopenfilename(initialdir='.',
                                              title='Выберите текстовый файл',
                                              filetypes=(("Текстовые файлы", "*.txt *.pdf *.docx"),
                                                         ("Все файлы", "*.*")))

        print(f"Результат filedialog: {filename}")
        if filename:
            self.file_path.set(filename)
            filename, ext = os.path.splitext(os.path.basename(filename))
            new_ext = ext.replace('.', '')
            if new_ext.upper() in self.formats:
                self.file_name.set(f'...{filename[-5:]}{ext}')
            else:
                messagebox.showerror("Ошибка", f"Пожалуйста, выберите поддерживаемый формат текстового файла")
                return
    # открывает диалоговое окно для выбора пути сохранения
    def _browse_output_dir(self):
        output_dir = filedialog.askdirectory(initialdir='.', title='Выберите папку для сохранения')
        if output_dir:
            self.output_path.set(output_dir)
            self.output_path_name.set('.../' + os.path.basename(output_dir))
