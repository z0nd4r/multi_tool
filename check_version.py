import tkinter as tk
import requests
import os
import sys
import subprocess

from packaging import version

from tkinter import messagebox

GITHUB_API = "https://api.github.com/repos/z0nd4r/multi_tool/releases/latest"
CURRENT_VERSION = "1.0.0"

def update_app(parent):
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

        exe_url = r.json()["assets"][0]["browser_download_url"]
        temp_path = os.path.join(os.getenv("TEMP"), "new_version.exe") # сюда будет скачана новая версия
        bat_path = os.path.join(os.getenv("TEMP"), "update.bat") # он будет выполнять обновление
        current_exe = sys.argv[0] # путь к текущему исполняемому файлу

        # скачиваем новый файл
        with requests.get(exe_url, stream=True) as f:
            f.raise_for_status()
            with open(temp_path, "wb") as out:
                out.write(f.content)

        # создаём BAT-файл
        old_exe = current_exe + ".old"
        bat_script = f"""@echo off
        chcp 65001 > nul
        title Application Update
        
        echo Waiting for the current version to close...
        timeout /t 2 /nobreak > NUL
        
        echo Renaming the current file...
        ren "{current_exe}" "{os.path.basename(old_exe)}"
        if errorlevel 1 (
            echo Failed to rename the file. The application may still be running.
            echo Please close the application and try again.
            pause
            exit /b 1
        )
        
        echo Copying the new version...
        copy /Y "{temp_path}" "{current_exe}"
        if errorlevel 1 (
            echo Failed to copy the new version. Please check your permissions.
            echo Aborting update...
            ren "{os.path.basename(old_exe)}" "{current_exe}"
            pause
            exit /b 1
        )
        
        echo Deleting temporary files...
        del "{temp_path}" > NUL 2>&1
        del "{old_exe}" > NUL 2>&1
        pause
        exit /b 0
        """

        with open(bat_path, "w") as bat:
            bat.write(bat_script)

        messagebox.showinfo("Успех", "Обновлено до последней версии.\nПрограмма перезапустится.")

        # Запускаем батник и выходим
        subprocess.Popen(["cmd", "/c", bat_path], creationflags=subprocess.CREATE_NO_WINDOW) # еще скрываем окно cmd
        sys.exit()

    except requests.exceptions.RequestException as e:
        messagebox.showerror('Ошибка', f'Ошибка при скачивании: {e}')
    except OSError as e:
        messagebox.showerror('Ошибка', f'Ошибка при работе с файлами: {e}')
    except Exception as e:
        messagebox.showerror("Ошибка", f'Неизвестная ошибка: {e}')


        #
        #         echo Starting the new version...
        #         start "" "{current_exe}"
        #         if errorlevel 1 (
        #             echo Oshibka: Ne udalos' zapustit' novuyu versiyu.
        #             pause
        #             exit /b 1
        #         )
        #
        #         echo Waiting for the new version to start...
        #         timeout /t 2 /nobreak > NUL