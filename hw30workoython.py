
# def proverka(n):
#     if len(n)!=6:
#         return 'не правильная длина'
#     elif not n[0].isalpha():
#         return 'начинатся не с буквы'
#     else:
#         return 'все ок'
#     pass
#
#
# number = input('введи номер')
# proverka(number)
# res = proverka(number)
# print(res)
import random

# n1 = ['Alex','Vova',['vadim','dima']]   #list
# n2 = ('Alex','Vova')   #tuple
# n3 = {'name':'Alex','sosed':'Vova'}     #dict
# # ключ name, значение Alex
# print(n1[2][0])
# print(n2[0])
# print(n3['name'])
#
# print(n3.values())      # все значения
# print(n3.keys())        # все ключи
# print(n3.items())       # все содержимое
#
# n3.pop('sosed')         #удаление по ключу
# print(n3)
# n3.update({'sosed':'Vadim'})     # добавить еще одну пару
# print(n3)
#
# print(n3.get('name'))     # получить значение под ключом name
#
# n3['name'] = 'Dima'
# print(n3)
#
# a = {'name':'Ivaan','surname':'Ivanov','adres':'Moscow','pet':['cat','dog','pig']}
# print(*a.items())
import random
import time

sword = {'material': 'bronze', 'min': 10, 'max': 12}
stone = {'material': 'stone', 'min': 7, 'max': 15}
pistol = {'material': 'stone', 'min': 8, 'max': 16}
nife = {'material': 'stone', 'min': 3, 'max': 20}
tank = {'material': 'stone', 'min': 15, 'max': 50}

warrior1 = {'name': 'Boris', 'nick': 'Britva', 'hp': 100, 'weapon': None}
warrior2 = {'name': 'Bob', 'nick': 'Gubka', 'hp': 100, 'weapon': None}
warrior3 = {'name': 'man', 'nick': 'man', 'hp': 100, 'weapon': None}
warrior4 = {'name': 'billi', 'nick': 'billi', 'hp': 100, 'weapon': None}
warrior5 = {'name': 'gena', 'nick': 'gena', 'hp': 100, 'weapon': None}

spisok = [warrior1, warrior2, warrior3, warrior4, warrior5]
weapons = [sword, stone, pistol, nife, tank]

def battle(b1, b2):
    print('На арену выходят')
    print(b1['name'], b1['nick'])
    print(b2['name'], b2['nick'])
    print('Начинаем поединок')

    while b2['hp'] > 0 and b1['hp'] > 0:
        udar(b1, b2)
        if b2['hp'] <= 0:
            break
        else:
            udar(b2, b1)

    time.sleep(0.5)
    if b2['hp'] <= 0:
        print('Победитель:')
        print(b1['name'], b1['nick'])
    elif b1['hp'] <= 0:
        print('Победитель:')
        print(b2['name'], b2['nick'])

def udar(b1, b2):
    time.sleep(0.5)
    r = random.randint(b1['weapon']['min'], b1['weapon']['max'])
    print(b1['name'], 'ударил на', r)
    b2['hp'] -= r
    print('У', b2['name'], 'осталось здоровья', b2['hp'])


print('Выберите воинов:')
for i, warrior in enumerate(spisok):
    print(f'{i+1}. {warrior["name"]}, {warrior["nick"]}')


i1 = int(input('Первый воин: '))
i2 = int(input('Второй воин: '))


print('Выберите оружие:')
for i, weapon in enumerate(weapons):
    print(f'{i+1}. {weapon["material"]} ({weapon["min"]}-{weapon["max"]})')


w1 = int(input('Оружие для первого воина: '))
w2 = int(input('Оружие для второго воина: '))


spisok[i1-1]['weapon'] = weapons[w1-1]
spisok[i2-1]['weapon'] = weapons[w2-1]

# Запуск битвы
battle(spisok[i1-1], spisok[i2-1])
