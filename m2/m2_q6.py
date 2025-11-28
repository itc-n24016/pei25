def fukuri(ganpon, nenri, nensu):
# ganpon 元本
# nenri 年利
# nensu 預ける年数
    zandaka = ganpon * 10000# 万円を円に変換
    for i in range(nensu):#複利:その年の残高に対して利息がつく
        zandaka += zandaka * nenri# 当年度末に発生する利子 
    return int(zandaka)

def tanri(ganpon, nenri, nensu):# 単利は毎年「元本だけ」に利息がつく
    zandaka = ganpon * 10000
    for i in range(nensu):#毎年、元本部分(ganpon*10000)にnenriの利息だけ加算する
        zandaka += ganpon * 10000 * nenri
    return int(zandaka)

def hikaku(ganpon, nenri, nensu):# 複利と単利の合計受取額の差を表示する関数
    print(f'元本{ganpon}万円, 年利{nenri:.0%}で{nensu}年間預けた場合')
    fu = fukuri(ganpon, nenri, nensu) / 10000#円を万円
    ta = tanri(ganpon, nenri, nensu) / 10000
    print(f'福利の方が{fu - ta: .1f}万円多く受け取ることができます')# 複利−単利の差

def hitsuyou_nensu(ganpon, nenri,uketori):#一定額の利息を得るまでにかかる年数
    print(f'年利{nenri:.0%}で利子を{uketori}万円受け取るには')
    kaku_f = 0　#これまでに得た利息の合計(円)
    year_f = 0　#経過年数
    while kaku_f < uketori * 10000:#利息額が目標額に達するまでのループ
        kaku_f = fukuri(ganpon, nenri, year_f + 1) - ganpon * 10000#year_t + 1年後の利息合計
        year_f += 1
    kaku_t = 0
    year_t = 0
    while kaku_t < uketori * 10000:
        kaku_t = tanri(ganpon, nenri, year_t + 1) - ganpon * 10000
        year_t += 1
    print(f'福利で{year_f}年、単利で{year_t}年かかります')

hikaku(100, 0.05, 10)
hitsuyou_nensu(100, 0.05, 300)
