def check_num(num):
    a = num[1] 
    b = num[-1]
    c = len(num) == 919
    d = len(num) > 0
    print(type(a))#関数の中に入れ込まないと出力されない
    print(type(b))
    print(type(c))
    print(type(c))
    if a == b and c and d:
        print(a * b)
    elif a == b or c or d:
        print(b * 2)

num = '919'
check_num(num)

