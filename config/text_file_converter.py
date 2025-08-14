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
    output_file = os.path.join(output_dir, f'{filename}.{choice.lower()}')

    if ext.upper() == '.'+choice:
        messagebox.showinfo('Внимание', 'Входной и выходной форматы совпадают')
        return

    if ext.upper() == '.DOCX':
        text = get_text_from_docx(input_file)
    elif ext.upper() == '.PDF':
        text = get_text_from_pdf(input_file)

    # проверка, есть ли файл с таким же именем в дериктории
    if os.path.exists(output_file):
        examination_and_save(text, output_file, output_dir, filename, choice)
        return
    else:
        save_text_to_file(text, output_file, choice)


# сохраняет текст в файл
def save_text_to_file(text, output_file, choice):
    try:
        if choice == 'TXT':
            with open(output_file, "w", encoding="utf-8") as f:
                f.write(text)
        elif choice == 'PDF':
            pass
        elif choice == 'DOCX':
            write_text_to_docx(text, output_file)
        messagebox.showinfo('Успех', f'Тектовый файл сохранен как:\n{output_file}')
    except Exception as e:
        messagebox.showerror('Ошибка', f'Ошибка при записи в файл:\n{e}')


# извлекает текст из DOCX файла
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


# извлекает текст из PDF файла
def get_text_from_pdf(pdf_file):
    try:
        pdf_document = fitz.open(pdf_file)
        full_text = ''
        for page_num in range(pdf_document.page_count):
            page = pdf_document.load_page(page_num)
            text = page.get_text()
            full_text += text
        return full_text
    except Exception as e:
        messagebox.showerror('Ошибка', f'Ошибка при чтении PDF файла:\n{e}')
        return


# создает DOCX файл из текста
def write_text_to_docx(text, output_file):
    try:
        document = Document()
        for paragraph_text in text.splitlines():
            document.add_paragraph(paragraph_text)
        document.save(output_file)
    except Exception as e:
        messagebox.showerror('Ошибка', f'Ошибка при записи DOCX файла:\n{e}')
        return

# создает PDF файл из текста
def write_text_to_pdf(text, pdf_file):
    pass


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
            messagebox.showinfo('Успех', f'Текстовый файл сохранен как:\n{output_file}')
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
                    messagebox.showinfo('Успех', f'Текстовый файл сохранен как:\n{new_output_file}')
                except Exception as e:
                    messagebox.showerror('Ошибка', f'Ошибка при записи в файл:\n{e}')
                break
            counter += 1
    else:
        messagebox.showinfo("Внимание", "Сохранение отменено")
        return





