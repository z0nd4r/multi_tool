import tkinter as tk
import requests
import os
import sys
import subprocess

from tkinter import messagebox

GITHUB_API = "https://api.github.com/repos/z0nd4r/multi_tool/releases/latest"
CURRENT_VERSION = "v1.2.0"

def update_app(parent):
    try:
        r = requests.get(GITHUB_API)
        latest = r.json()["tag_name"]
        print(r.json()["tag_name"])
        if latest <= CURRENT_VERSION:
            messagebox.showinfo("Внимание", "Установлена последняя версия")
            print("Уже последняя версия.")
            return

        exe_url = r.json()["assets"][0]["browser_download_url"]
        temp_path = os.path.join(os.getenv("TEMP"), "new_version.exe")
        bat_path = os.path.join(os.getenv("TEMP"), "update.bat")
        current_exe = sys.argv[0]

        # скачиваем новый файл
        with requests.get(exe_url, stream=True) as f:
            with open(temp_path, "wb") as out:
                out.write(f.content)

        # создаём BAT-файл
        bat_script = f"""
        @echo off
        timeout /t 2 /nobreak
        move /Y "{temp_path}" "{current_exe}"
        exit
        """

        with open(bat_path, "w") as bat:
            bat.write(bat_script)

        messagebox.showinfo("Успех", "Обновлено до последней версии. Откройте программу заново.")

        # Запускаем батник и выходим
        subprocess.Popen(["cmd", "/c", bat_path])
        sys.exit()



    except Exception as e:
        messagebox.showerror("Ошибка", f'Ошибка при обновлении: {e}')
        print("Ошибка при обновлении:", e)

        # start "" "{current_exe}"