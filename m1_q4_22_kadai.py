a = 17
b = 5
dm = divmod(a,b) # 商の余りをタプルで返す
p = pow(dm[0], dm[1]) # 3 ** 2 = 9
all_num = [a, b, dm[0], dm[1], p] # [17,5,3,2,9]
min_all = min(all_num) # 2
max_all = max(all_num) # 17
sum_all = sum(all_num) # 36
print(f'{min_all}, {max_all}, {sum_all}')
print(all_num)
