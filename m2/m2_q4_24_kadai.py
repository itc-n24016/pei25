def func(a, b):
    if a ** b <= 64:
        return 1
    else:
        return 0
x = func(4, 3)
y = func(3, 4)
v = func(5, 6)
z = [bool(x), bool(y), bool(v)]
print(z)
