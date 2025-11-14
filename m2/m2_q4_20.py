num = 3
list_a = []
while num < 5 :
    for i in range(num, 10, 3): # i から 10 未満までを 3 ずつ増やしながらループする
        print(list_a)
        i -= 6
        list_a.append(i)
    num += 1
print(sum(list_a))# 合計
print(list_a)
