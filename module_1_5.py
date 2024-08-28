immutable_var = ([1,2],3,"Я строка кортежа", True)
print(immutable_var)
immutable_var[0][0] = 5
print(immutable_var)
# Даю развернутый ответ, опираясь на информацию из интернета,
# несмотря на то,что кортеж и список являются # ссылками набор данных в памяти
# кортежи нельзя изменять, потому, что на уровне разработки языка Python
# в него не заложены методы позволяющие быть кортежу динамическим (как список(List)

mutable_list = ["Я строка списка", True]
print(mutable_list)
mutable_list.remove("Я строка списка")
print(mutable_list)
mutable_list.extend(["А я новая строка списка", 2231231])
print(mutable_list)







# Списки
# food = ["apple", "coconut", "banana"]
# food.append(True)
# print(food)
# food.extend(["string", 2231231])
# print(food)
# food.remove("string")
# print(food)
# print("coconut" in food)
# print("coconut" not in food)
# print(food[0:2:5])


#Кортежи
# tuple_ = ([1,2],3,4) + (1, 2)
# print(tuple_.__sizeof__())
# print(tuple_)
# tuple_[0][0] = 2
# print(tuple_)
# tuple_ = (1, 2) * 2
# print(tuple_)