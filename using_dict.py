# 'ab' - сокращение от 'a'address'b'ook

ab = {'Swaroop': 'swaroop@swaroop.com',
      'Larry': 'larry@wall.org',
      'Matsumoto': 'matz@ruby-lang.org',
      'Spammer': 'spammer@hotmail.com'
      }
print("Адрес Swaroop'a:", ab['Swaroop'])

# Удаление пары ключ-значение

del ab['Swaroop']

print('\nВ адресной книге {0} контактов\n'.format(len(ab)))

for name, address in ab.items():
    print('Контакт {0} с адресом {1}'.format(name, address))

# Добавления пары ключ-значение
ab['Guido'] = 'guido@python.org'

if 'Guido' in ab:
    print("\nАдрес Guido:", ab['Guido'])
