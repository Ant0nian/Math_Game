"""
В этом файле хранятся основные методы, нужные для создания игры.
По сути здесь мы создаем ее движок
"""


from random import randint


def switch():                   # Этот метод возвращает рандомное число от 0 до 3 для определения действия
    return randint(0, 3)


def f_s(sw, s):                 # В этом методе мы создаем первое число в зависимости от того, какое действие нам выпало
    if sw == 0 or sw == 1:
        f = randint(1, 1000)
    if sw == 2:
        f = randint(1, 100)
    if sw == 3:
        f = randint(1, 1000)
        if f % s != 0:
            f = f - (f % s)
    return f


def s_s(sw):                    # Создаем второе число в зависимости от действия
    if sw == 0:
        s = randint(1, 1000)
    if sw == 1:
        s = randint(1, 1000)
    if sw == 2:
        s = randint(1, 100)
    if sw == 3:
        s = randint(1, 10)
    return s


def result(f, s, sw):           # На вход здесь подаются оба числа и определитель действий. Тут мы получаем ответ
    if sw == 0:
        res = f + s
    if sw == 1:
        res = f - s
    if sw == 2:
        res = f * s
    if sw == 3:
        res = int(f / s)
    return res


def list_of_answers(res):       # Здесь мы генерируем список неправильных ответов
    rnd_opts = [randint(res - 10.0, res + 10.0) for i in range(4)]
    for a in rnd_opts:
        if a == res:
            a = a - 1
    return rnd_opts


'''
В методе ниже
Генерируем определитель сценария ответов. 
Это нужно для того, чтобы правильный ответ находился все время в разном месте
'''


def rand_ans():
    return randint(1, 4)


'''
В методах ниже мы создаем нужные нам кнопки вариантов ответов
Они создаются на основе счетчика неправильных ответов, 
результата выполнения действия и списка неправильных ответов
'''


def button1(res, r, l_o_a):
    if r == 1:
        return res
    else:
        return l_o_a[0]


def button2(res, r, l_o_a):
    if r == 2:
        return res
    else:
        return l_o_a[1]


def button3(res, r, l_o_a):
    if r == 3:
        return res
    else:
        return l_o_a[2]


def button4(res, r, l_o_a):
    if r == 4:
        return res
    else:
        return l_o_a[3]
