import os
import time
import zipfile

source = ['C:\\test', 'C:\\test 2']
target_dir = "X:\\Backup\\"

today = target_dir + os.sep + time.strftime('%Y%m%d') + '\\'
now = time.strftime('%H%M%S_')

comment = input('Введите комментарий --> ')
if len(comment) != 0:  # проверяем, введён ли комментарий
    now += comment.replace(' ', '_')

# Создаём каталог если его ещё нет
if not os.path.exists(today):
    os.mkdir(today)  # Создание каталога
print('Каталог успешно создан', today)

z = zipfile.ZipFile(today + now + ".zip", 'w')  # Создание нового архива

files = {}
for so in source:
    for root, dirs, file in os.walk(so):
        files[so] = file

for root, files in files.items():
    for file in files:
        print('Файл добавлен:', root, file)
        z.write(os.path.join(root, file))

z.close()
