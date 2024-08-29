
print(' \nСловари:\n ')

my_dict = {'Mike': 1996, 'Avdotiy': 2001} #   - Создайте переменную my_dict и присвойте ей словарь из нескольких пар ключ-значение.
print(my_dict) # - Выведите на экран словарь my_dict.
print(my_dict.get('Mike')) #  - Выведите на экран одно значение по существующему ключу
print(my_dict.get('Nike', 'Нет такого'))# одно по отсутствующему из словаря my_dict без ошибки.
my_dict.update({'Avkakiy': 1882,
                'Avgustiniy': 1971}) # - Добавьте ещё две произвольные пары того же формата в словарь my_dict.
a = my_dict.pop('Mike') #Удалите одну из пар в словаре по существующему ключу из словаря my_dict
print(a) # и выведите значение из этой пары на экран.
print(my_dict) # Выведите на экран словарь my_dict.

print(' \nМножества:\n ')

my_set = {1, 'String', 1, 'String'}  # Создайте переменную my_set и присвойте ей множество, состоящее из разных типов данных с повторяющимися значениями.
print(my_set) # Выведите на экран множество my_set (должны отобразиться только уникальные значения).
my_set.update({22, 'MikeS'}) # Добавьте 2 произвольных элемента в множество my_set, которых ещё нет.
my_set.remove('MikeS') # Удалите один любой элемент из множества my_set.
print(my_set) # Выведите на экран измененное множество my_set.


# Множества
# set_ = {1, 2, 3, 4, 5, 6, 1, 2, 3, 4}
# print(set_)
# list_ = [1, 2, 3, 4, 1, 6, 1, 2, 3, 4]
# print(list_)
# list_=set(list_)
# print(list_.discard(1))


# Словари
#
# phone_book = {'Mike': [88005553535, 91812831], 'Max': 88005553535}
# phone_book['Denis'] = 15213123123
# phone_book['Anton'] = 1521312312123
# del phone_book['Anton']
#
# phone_book.update({'Sasha': 2112312313123,
#                    'Alex':  12312312312312})
#
#
#
# print(phone_book.keys())
# print(phone_book.items())
# a = phone_book.pop('Alex') #такой же метод работает для списков
#
# print(a)
# print(phone_book.get('Mike', 'Такого ключа нет'))
