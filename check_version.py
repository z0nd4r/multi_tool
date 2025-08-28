import tkinter as tk
import webbrowser

import requests
import os
import sys
import subprocess

from packaging import version

from tkinter import messagebox

GITHUB_API = "https://api.github.com/repos/z0nd4r/multi_tool/releases/latest"
CURRENT_VERSION = "2.0.0"
LINK_TO_PROGRAM = "https://github.com/z0nd4r/multi_tool/releases/latest"

def update_app():
    try:
        r = requests.get(GITHUB_API)
        latest_tag = r.json()["tag_name"]
        print(r.json()["tag_name"])

        latest_version = version.parse(latest_tag)
        current_version = version.parse(CURRENT_VERSION)

        if latest_version <= current_version:
            messagebox.showinfo("Внимание", "Установлена последняя версия")
            print("Уже последняя версия.")
            return
        else:
            response = messagebox.askyesno(
                title='Внимание',
                message=f'Доступна новая версия {latest_version}\nХотите скачать?',
                icon=messagebox.INFO
            )

            if response:
                webbrowser.open_new(LINK_TO_PROGRAM)
            else:
                return None

    except requests.exceptions.RequestException as e:
        messagebox.showerror('Ошибка', f'Ошибка при скачивании: {e}')
    except OSError as e:
        messagebox.showerror('Ошибка', f'Ошибка при работе с файлами: {e}')
    except Exception as e:
        messagebox.showerror("Ошибка", f'Неизвестная ошибка: {e}')
