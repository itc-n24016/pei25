a = [2.02, 2.03, 2.04]
b = [2.05, 2.06, -2.07]

c = a + b
print(c)
print(max(c))
print(min(c[2:5]))
print(round(c[2], 1))
print(round(c[5], 1))
print(round(c[3], 1)) # c[3]は2.05であり、四捨五入が5までを切り捨てて、6から繰り上げになっている
