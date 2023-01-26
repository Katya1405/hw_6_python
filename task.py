# Создайте список из случайных чисел. Найдите количество различных элементов в нем.

from random import randint
some_list = []
for i in range(10):
    some_list.append(randint(0, 11))
print(f'Созданный список: {some_list}')
count_el = len(set(some_list))
print(f'Количество неповторяющихся элементов: {count_el}')

# Фрукты Пользователь вводит число K - количество фруктов. Затем он вводит K фруктов в формате:
# название фрукта и его количество. Добавьте все фрукты в словарь, где название фрукта - это ключ, а количество - значение

countOfFruits = int(input('Количество фруктов: '))
fruits = {}
for i in range(countOfFruits):
    name = input('Название фрукта: ')
    countt = int(input('Количество этого фрукта: '))
    fruits[name] = countt
print(fruits)

# Пользователь вводит число N. Затем он вводит личные данные (имя и возраст) своих N друзей.
# Создайте список friends и добавьте в него N словарей с ключами name и age.
# Найдите самого младшего из друзей и выведите его имя.

N = int(input('Количество друзей: '))
friends = []
for i in range(N):
    friend_name = input('Имя друга: ')
    friend_age = int(input('Возраст друга: '))
    friends.append({'name': friend_name, 'age': friend_age})

age = 100
name = ''
for i in range(len(friends)):
    if friends[i]['age'] < age:
        age = friends[i]['age']
        name = friends[i]['name']
print(name)

# Пользователь вводит число N. Затем он вводит личные данные (имя и возраст) своих N друзей.
# Создайте список friends и добавьте в него N словарей с ключами name и age. Выведите средний возраст всех друзей и самое длинное имя.

N = int(input('Количество друзей: '))
friends = []
sum = 0
search_name = ''
for i in range(N):
    friend_name = input('Имя друга: ')
    if len(friend_name) > len(search_name):
        search_name = friend_name
    friend_age = int(input('Возраст друга: '))
    sum += friend_age
    friends.append({'name': friend_name, 'age': friend_age})

print(f'Средний возраст друзей: {sum/N}')
print(f'Самое длинное имя: {search_name}')

# Программа получает на вход слово на английском языке и несколько его переводов на русском языке.
# Составьте словарь, в котором ключ - это английское слово, а значение - это список русских слов.

translator = dict()
N = int(input('Количество слов: '))
for i in range(N):
    word = input('Введите слово и перевод: ').replace(',', '').split()
    for i in range(len(word)):
        if '-' in word:
            word.remove('-')
        translator[word[0]] = word[1:]
print(translator)
