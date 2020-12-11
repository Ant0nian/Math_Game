from random import randint
import defs
switch = randint(0, 3)
r_opt = randint(1, 4)
symbols = ["+", "-", "*", "/"]
if switch == 0:
    f = randint(1, 1000)
    s = randint(1, 1000)
    res = f + s
elif switch == 1:
    f = randint(1, 1000)
    s = randint(1, f)
    res = f - s
elif switch == 2:
    f = randint(1, 100)
    s = randint(1, 100)
    res = f * s
elif switch == 3:
    f = randint(1, 1000)
    s = randint(1, 10)
    if f % s == 0:
        res = f / s
    else:
        f = f - (f % s)
        res = int(f / s)

print("Решите пример: " + str(f) + symbols[switch] + str(s) + " = \n")
defs.option(r_opt, res)
u_res = int(input())
if u_res != r_opt:
    print("Loser")
else:
    print("Good man")