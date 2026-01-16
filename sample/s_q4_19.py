a = []#空リスト Noneではない
b = ''# 空文字 Noneではない
c = 1 == 2 # False Noneではない

if a is None and b is not None: # a = False, b = True
    print(a, b)
elif b is None or c is None:# b = False, c = False
    print(b, c)
elif c is not None and a is not None: # c = True, a = True
    print(c, a)
