from tkinter import messagebox
from PIL import Image
import os

def convert_image(combo, file_path, output_path):
    input_file = file_path.get()
    output_dir = output_path.get()

    choice = combo.get()

    if not input_file or not output_dir:
        messagebox.showerror("Ошибка", "Пожалуйста, выберите изображение и папку для сохранения")
    else:
        try:
            image = Image.open(input_file)
            filename, ext = os.path.splitext(os.path.basename(input_file))
            if ext == '.png' and choice == 'JPEG':
                image = image.convert('RGB')
            output_file = os.path.join(output_dir, f'{filename}.{choice.lower()}')

            if os.path.exists(output_file):
                # диалоговое окно с кнопками
                response = messagebox.askyesnocancel(
                    title="Конфликт файла",
                    message=f"Файл {os.path.basename(output_file)} уже существует!\n"
                            "Хотите перезаписать его?",
                    detail="Нажмите:\n"
                           "• 'Да' — перезаписать\n"
                           "• 'Нет' — сохранить с новым именем\n"
                           "• 'Отмена' — не сохранять",
                    icon=messagebox.WARNING
                )

                if response is True:
                    image.save(output_file, format=choice)
                    messagebox.showinfo("Успех", f"Изображение сохранено как:\n{output_file}")
                elif response is False:
                    counter = 1
                    while True:
                        new_filename = f"{filename}_{counter}.{choice.lower()}"
                        new_output_file = os.path.join(output_dir, new_filename)
                        if not os.path.exists(new_output_file):
                            image.save(new_output_file, format=choice)
                            messagebox.showinfo("Успех", f"Изображение сохранено как:\n{new_output_file}")
                            break
                        counter += 1
                else:
                    messagebox.showinfo("Внимание", "Сохранение отменено")
                    return None
            else:
                image.save(output_file, format=choice)
                messagebox.showinfo("Успех", "Файл сохранён!")

        except Exception as e:
            messagebox.showerror("Ошибка", f"Выберите поддерживаемый формат изображения:{e}")