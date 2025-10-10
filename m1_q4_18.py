phrase = 'PythonProgramming'
list_p = []#空リストの作成

for p in phrase:
    if  p not in list_p:
        list_p.append(p)#list_pに同じ文字がなければ追加する関数
print(list_p)
print(len(phrase), len(list_p))
print(len(phrase) - len(list_p))
