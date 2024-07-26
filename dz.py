import subprocess

def test_command(command, text):
    """Проверяет выполнение команды и наличие текста в её выводе."""
    process = subprocess.Popen(command, stdout=subprocess.PIPE, stderr=subprocess.STDOUT, shell=True)
    output = process.communicate()[0].decode('utf-8')
    return text in output

def test_l():
    """Тестирует команду вывода списка файлов."""
    command = 'ls'
    text = 'file1.txt'
    assert test_command(command, text), f'Text "{text}" not found in the output of command "{command}"'

def test_x():
    """Тестирует команду разархивирования."""
    command = 'unzip archive.zip'
    text = 'extracting'
    assert test_command(command, text), f'Text "{text}" not found in the output of command "{command}"'

# Задание 2
import os

def test_h():
    """Тестирует команду расчета хеша."""
    # Создаем временный файл для тестирования
    with open('/tmp/test_file', 'wb') as file:
        file.write(b'Test data for hash calculation')

    # Вычисляем хеш файла
    command = f'crc32 /tmp/test_file'
    expected_hash = int(os.popen(command).read().strip(), 16)

    # Проверяем, что хеш совпадает с рассчитанным командой crc32
    command = f'python -m zipfile -c /tmp/test_file'
    actual_hash = int(os.popen(command).read().strip(), 16)
    assert expected_hash == actual_hash, f'Hashes do not match: expected {expected_hash}, got {actual_hash}'

    # Удаляем временный файл
    os.remove('/tmp/test_file')

# Запуск тестов
if __name__ == '__main__':
    test_l()
    test_x()
    test_h()