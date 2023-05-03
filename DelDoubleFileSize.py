import os

# Директория, в которой нужно удалить дубликаты файлов
dir_path = "/mp3"

# Создаем словарь для хранения информации о файлах
files_dict = {}

# Проходим по всем файлам в директории
for root, dirs, files in os.walk(dir_path):
    for file in files:
        file_path = os.path.join(root, file)

        # Вычисляем вес файла
        file_size = os.path.getsize(file_path)

        # Если файл с таким весом уже существует, удаляем его, иначе добавляем в словарь
        if file_size in files_dict:
            os.remove(file_path)
            print(f"Файл {file_path} был удален как дубликат.")
        else:
            files_dict[file_size] = file_path

print("Удаление дубликатов завершено.")