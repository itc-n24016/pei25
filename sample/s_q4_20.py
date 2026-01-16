a = 0
counter = 0
while counter < 6:
    a += counter# 1, 3, 6
    counter += 1# 1, 2, 3
    if a > 4:#3回目で a > 4になる
        break
print(a, counter)
