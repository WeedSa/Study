import random

num_passwords = int(input('Введите количество паролей: '))
len_password = int(input('Введите длину пароля: '))

dig = input('Включать цифры? (д/н) ')
while dig != 'д' and dig != 'н':
    print('Некорректный ответ. Попробуйте еще раз')
    dig = input('Включать цифры? (д/н) ')

up_letters = input('Включать прописные буквы? (д/н) ')
while up_letters != 'д' and up_letters != 'н':
    print('Некорректный ответ. Попробуйте еще раз')
    up_letters = input('Включать прописные буквы? (д/н) ')

low_letters = input('Включать строчные буквы? (д/н) ')
while low_letters != 'д' and low_letters != 'н':
    print('Некорректный ответ. Попробуйте еще раз')
    low_letter = input('Включать строчные буквы? (д/н) ')

symb = input('Включать символы? (д/н) ')
while symb != 'д' and symb != 'н':
    print('Некорректный ответ. Попробуйте еще раз')
    symb = input('Включать символы? (д/н) ')

digits = '0123456789'
lowercase_letters = 'abcdefghijklmnopqrstuvwxyz'
uppercase_letters = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
punctuation = '!#$%&*+-=?@^_'


def generate_password():
    chars = ''
    password = ''
    if dig == 'д':
        chars += digits
    if up_letters == 'д':
        chars += uppercase_letters
    if low_letters == 'д':
        chars += lowercase_letters
    if symb == 'д':
        chars += punctuation
    for j in range(num_passwords):
        for i in range(len_password):
            password += random.choice(chars)
        print(password)
        password = ''


generate_password()