import os
import time

path = 'C:\\Users\\Роман\\PycharmProjects\\HomeWork\\Module#7'

for dirpath, dirnames, filenames in os.walk(path):
    for file in filenames:
        file_path = os.path.join(dirpath, file)
        file_time = os.path.getmtime(file_path)
        last_format_time = time.strftime('%d.%m.%Y %H:%M', time.localtime(file_time))
        file_size = os.path.getsize(file_path)
        parent_dir = os.path.dirname(file_path)
    print(f'По адресу: {file_path}\nОбнаружен файл: {file}\nРазмером: {file_size} байт\nДата и время последнего изменения: {last_format_time}\nРодительская директория: {parent_dir}')