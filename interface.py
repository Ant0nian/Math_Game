"""
В этом файле мы отрисовываем игру, создаем ее визуальную составляющую
"""

import PySimpleGUI as sg
import engine


def game():                         # Этот метод создает окно и наполняет его
    symbols = ["+", "-", "*", "/"]  # массив строк с действиями
    '''
    Ниже мы создаем нужные нам переменные из методов движка игры
    '''
    switch = engine.switch()
    s = engine.s_s(switch)
    f = engine.f_s(switch, s)
    res = engine.result(f, s, switch)
    l_o_a = engine.list_of_answers(res)
    r = engine.rand_ans()
    button1 = engine.button1(res, r, l_o_a)
    button2 = engine.button2(res, r, l_o_a)
    button3 = engine.button3(res, r, l_o_a)
    button4 = engine.button4(res, r, l_o_a)

    sg.theme('DarkAmber')  # выбираем цветовую тему нашей игры
    '''
    Ниже мы заполняем поля игры. 
    1 строчка: Текст с примером
    3 строчка: Кнопки варинтов
    5 строчка: кнопка отмена
    '''
    layout = [[sg.Text("Решите пример: " + str(f) + symbols[switch] + str(s) + " = \n", size=[30, 1])],
              [sg.Text("")],
              [sg.Button(button1), sg.Button(button2), sg.Button(button3), sg.Button(button4)],
              [sg.Text("")],
              [sg.Button('Exit')]]

    window = sg.Window('Math Game', layout)     # создаем само окно игры

    end = True      # Переменная для выхода из цикла
    while end:      # Цикл в котором написана логика поведения составляющих и игры в целом
        event, values = window.read()
        if r == 1:
            if event == str(button1):
                window.close()
                game()
            else:
                sg.Button(button1)
        if r == 2:
            if event == str(button2):
                window.close()
                game()
        if r == 3:
            if event == str(button3):
                window.close()
                game()
        if r == 4:
            if event == str(button4):
                window.close()
                game()
        if event == sg.WIN_CLOSED or event == 'Exit':
            end = False
            break


game()
