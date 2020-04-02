import sys
import os

print(os.getcwd()) # Выводит текущий каталог
print('Аргументы командной строки:')
for i in sys.argv:
    print(i)

print('\n\nПеременная PYTHONPATH содержит', sys.path, '\n')