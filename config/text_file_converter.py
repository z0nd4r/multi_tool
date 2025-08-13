import os
from tkinter import messagebox
from docx import Document  # Для DOCX
import fitz  # PyMuPDF для PDF

def convert_text(combo, file_path, output_path):
    input_file = file_path.get()
    output_dir = output_path.get()

    choice = combo.get()

    if not input_file or not output_dir:
        messagebox.showerror("Ошибка", "Пожалуйста, выберите текстовый файл и папку для сохранения")
    if not choice:
        messagebox.showerror("Ошибка", "Пожалуйста, выберите выводимый формат")

    filename, ext = os.path.splitext(os.path.basename(input_file))

    if ext.upper() == '.'+choice:
        messagebox.showinfo('Внимание', 'Входной и выходной форматы совпадают')

    if choice == 'TXT': # конвертация в txt
        if ext.upper() == '.DOCX':
            text = get_text_from_docx(input_file)
            output_file = os.path.join(output_dir, f'{filename}.{choice.lower()}')
            if os.path.exists(output_file):
                examination_and_save(text, output_file, output_dir, filename, choice)
                return
            else:
                try:
                    save_text_to_file(text, output_file)
                    messagebox.showinfo('Успех', f'Тектовый файл сохранен как:\n{output_dir}')
                except Exception as e:
                    messagebox.showerror('Ошибка', f'Ошибка при записи в файл:\n{e}')
    elif choice == '.PDF': # конвертация в pdf
        pass
    elif choice == '.DOCX': # конвертация в docx
        pass


# извлекает текст из DOCX-файла.
def get_text_from_docx(docx_file):
    try:
        document = Document(docx_file)
        full_text = []
        for paragraph in document.paragraphs:
            full_text.append(paragraph.text)
        return '\n'.join(full_text)
    except Exception as e:
        messagebox.showerror('Ошибка', f'Ошибка при чтении DOCX-файла:\n{e}')
        return

# сохраняет текст в файл
def save_text_to_file(text, output_file):
    with open(output_file, "w", encoding="utf-8") as f:
        f.write(text)

# вывод диалогового окна, если файл существует в выбранной директории и сохранение файла
def examination_and_save(text, output_file, output_dir, filename, choice):
    response = messagebox.askyesnocancel(
        title='Конфликт файла',
        message=f"Файл {os.path.basename(output_file)} уже существует!\n"
                "Хотите перезаписать его?",
        detail="Нажмите\n"
               "• 'Да' — перезаписать\n"
               "• 'Нет' — сохранить с новым именем\n"
               "• 'Отмена' — не сохранять",
        icon=messagebox.WARNING
    )

    if response is True:
        try:
            save_text_to_file(text, output_file)
            messagebox.showinfo('Успех', f'Тектовый файл сохранен как:\n{output_dir}')
        except Exception as e:
            messagebox.showerror('Ошибка', f'Ошибка при записи в файл:\n{e}')
    elif response is False:
        counter = 1
        while True:
            new_filename = f"{filename}_{counter}.{choice.lower()}"
            new_output_file = os.path.join(output_dir, new_filename)
            if not os.path.exists(new_output_file):
                try:
                    save_text_to_file(text, new_output_file)
                    messagebox.showinfo('Успех', f'Тектовый файл сохранен как:\n{output_dir}')
                except Exception as e:
                    messagebox.showerror('Ошибка', f'Ошибка при записи в файл:\n{e}')
                break
            counter += 1
    else:
        messagebox.showinfo("Внимание", "Сохранение отменено")
        return None





