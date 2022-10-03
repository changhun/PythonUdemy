import math


def paint_calc(height, width, cover):
    ret = math.ceil(height * width / cover)
    return ret


l = input("Input height, width, cover (separated with space)").split(" ")
cans = paint_calc(int(l[0]), int(l[1]), int(l[2]))
print(f"{cans} can is needed")