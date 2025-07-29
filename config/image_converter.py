from tkinter import messagebox
from PIL import Image
import os

def convert_image(combo, file_path, output_path):
    input_file = file_path.get()
    output_dir = output_path.get()

    choice = combo.get()

    if not input_file or not output_dir:
        messagebox.showerror("Ошибка", "Пожалуйста, выберите изображение и папку для сохранения.")

    try:
        image = Image.open(input_file)
        filename, ext = os.path.splitext(os.path.basename(input_file))
        output_file = os.path.join(output_dir, f'{filename}.{choice.lower()}')
        image.save(output_file, format=choice)

        messagebox.showinfo("Успех", f"Изображение сохранено как {output_file}")

    except Exception as e:
        messagebox.showerror("Ошибка", f"Произошла ошибка: {e}")