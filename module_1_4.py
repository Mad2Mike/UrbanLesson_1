my_string = input("Введите любой текст:")

print(f'Ваш текст в верхнем регистре: {my_string.upper()}')
print(f'Ваш текст в нижнем регистре: {my_string.lower()}')
print(f'Ваш текст без пробелов: {my_string.replace(' ', '')}')
print(f'Первый символ вашего текста: "{my_string[0]}"')
print(f'Последний символ вашего текста: "{my_string[-1]}"')