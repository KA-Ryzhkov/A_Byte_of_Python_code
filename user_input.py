def reverse(text):
    return text[::-1]


def is_palindrome(text):
    return text == reverse(text)


something = input('Введите текст: ')
if is_palindrome(something):
    print('Да, это палиндром')
else:
    print("Нет, это не палиндром")

# Домащенее задание

import re


def reverse(text):
    return text[::-1]


def is_palindrome(text):
    return text == reverse(text)


something = re.sub('[.,)(!@#$ ]', '', input('Введите текст: ')).lower()
if is_palindrome(something):
    print('Да, это палиндром')
else:
    print("Нет, это не палиндром")
