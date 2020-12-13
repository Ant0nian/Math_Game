import PySimpleGUI as sg
import engine


def game():
    symbols = ["+", "-", "*", "/"]
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
    sg.theme('DarkAmber')

    layout = [[sg.Text("Решите пример: " + str(f) + symbols[switch] + str(s) + " = \n", size=[30, 1])],
                  [sg.Button(button1), sg.Button(button2), sg.Button(button3), sg.Button(button4)],
                  [sg.Button('Cancel')]]

    window = sg.Window('Math Game', layout)

    end = True
    while end:
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
        if event == sg.WIN_CLOSED or event == 'Cancel':
            end = False
            break


game()
