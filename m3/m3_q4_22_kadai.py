a = b = [1, 2, 3]
c = a + b

if a is b:
    print(1)
# isは同一性の比較：オブジェクトの場所が同じか
# 別々のリストに作ったリストは別のオブジェクト
elif a + b is c:
    print(2)
# 新しいリストを作り、リストとして保持
# 両者は違うオブジェクト
elif a == b:
    print(3)
# 等価性の比較：中身が同じか
# オブジェクトの中身が同じかの比較
elif a + b == c:
    print(4)

print(bool(a is b))
