from random import randint


def switch():  # generate random num for definition of our operations
    return randint(0, 3)


def f_s(sw, s):
    if sw == 0 or sw == 1:
        f = randint(1, 1000)
    if sw == 2:
        f = randint(1, 100)
    if sw == 3:
        f = randint(1, 1000)
        if f % s != 0:
            f = f - (f % s)
    return f


def s_s(sw):
    if sw == 0:
        s = randint(1, 1000)
    if sw == 1:
        s = randint(1, 1000)
    if sw == 2:
        s = randint(1, 100)
    if sw == 3:
        s = randint(1, 10)
    return s


def result(f, s, sw):
    if sw == 0:
        res = f + s
    if sw == 1:
        res = f - s
    if sw == 2:
        res = f * s
    if sw == 3:
        res = int(f / s)
    return res


def list_of_answers(res):
    rnd_opts = [randint(res - 10.0, res + 10.0) for i in range(4)]
    for a in rnd_opts:
        if a == res:
            a = a - 1
    return rnd_opts


def rand_ans():
    return randint(1, 4)


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
