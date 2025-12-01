import os
import random

def secure_delete(file_path, passes=5):
    """
    Надежно удаляет файл путем многократной перезаписи случайными данными.
    
    :param file_path: путь к файлу
    :param passes: количество проходов перезаписи (по умолчанию 5)
    """
    if not os.path.exists(file_path):
        print(f'Файл {file_path} не найден.')
        return
    
    # Получаем размер файла
    size = os.path.getsize(file_path)
    print(f'Размер файла: {size} байт. Начинается процесс уничтожения...')
    
    with open(file_path, 'wb') as f: # открываем файл в бинарном режиме для записи
        for _ in range(passes):
            # Генерируем случайные байты и записываем их в файл
            data = bytearray(random.getrandbits(8) for _ in range(size)) # создаем случайные байты размера файла
            f.write(data) # записываем случайные байты в файл
            print(_)
            f.flush()  # принудительный сброс данных на диск
            os.fsync(f.fileno()) # гарантируем, что данные записаны на диск
    
    # Окончательно удаляем файл
    try:
        # os.remove(file_path) # удаляет файл из файловой системы
        print(f'Файл {file_path} успешно уничтожен!')
    except OSError as e:
        print(f'Ошибка при удалении файла: {e}')

# Пример использования
if __name__ == "__main__":
    filename = input("Введите полный путь к файлу для уничтожения: ")
    secure_delete(filename)