a = 'わたしはサッカーが好きです。'
b = 'サッカーはスポーツです。'

if 'サッカー' in a and 'バスケット' in b:#aにサッカー、bにバスケットがはいってる、真か偽か
    print(a + b)
elif a.startswith('サッカー'):#サッカーが先頭にあるかどうか
    print(a.replace('サッカー', 'ゴルフ'))
elif b.find('は') == 4:#'は'の位置が4の場所にあるか
    print(b)
