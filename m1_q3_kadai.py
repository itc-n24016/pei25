a = 12
b = 5

print(abs(b - a))
print(2 * b - a)
print(b - abs(2 * b - a) * 3)
print("{0:08b}".format(64))

c = [2, 7, 15, 12, 9]
c.sort(reverse=True)

print(c)
print(c[1:4])
print(f'{(a - b) / c[1]:_<8.1f}')#f文字列で「全体8桁・小数点以下1桁・左寄せ・右側を _ で埋める」
