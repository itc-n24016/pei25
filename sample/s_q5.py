list_a = [214, 54, 178, 3,200]
list_B = ['', '', '', '', '']

i = 0
for x in list_a: # list_aの各要素をxへ代入
    if x <= 80: # xが80以下
        list_b[1] = 'low' # 'low'を代入
    elif x <= 200: # xが200以下
        list_b[i] = 'middle' # 'middle'を代入
    else: # それ以外(x > 200)
        list_b[i] = 'high'
    i += 1 # 次の代入ようにインデックスを1増やす
print(b) # [214, 54, 178,3, 200, 4, 2, 6, 2]

list_c = [4, 2, 6, 2] # list_dは[4,2, 6, 2]のコピー
list_a += list_c # 末尾2要素(6, 2)を順にxに代入
print(list_a) # [4, 2, 6, 2, 6, 2]

list_d = list_c.copy()
for x in list_d[-2]:
    list_d.insert(2, x)
print(list_d)

list_e = list_c # list_eはlist_cの参照
list_e.remove(2) # 最初に出現する2を1つ削除
print(list_c) # [4, 6, 2]

list_f = []
for x in range(0, 10, 3): # 0, 3, 6, 9を順にxを代入
    if 10 <= x ** 2 and x ** 2 < 30: # x²が10以上30未満
        list_f.append(2 * x) # xの2倍を追加
    elif 30 <= x ** 2: # x²が30以上
        list_f.append(x ** 2)
    else:
        list_f.append(x)
print(list_f) #
