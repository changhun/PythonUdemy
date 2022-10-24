# example of many positional arguments
def add(*args):
    total = 0
    for num in args:
        total += num

    return total


print(add(1, 2, 3, 4, 5))


def calculation(n, **kwargs):
    n += kwargs["add"]
    n *= kwargs["multi"]
    return n


ret = calculation(2, add=3, multi=2)
print(ret)
