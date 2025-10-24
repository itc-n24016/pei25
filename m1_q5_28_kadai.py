day = ['月','月','火','水','木','金','金']

day.remove('月') # 月の重複の削除
day.remove('金') # 金の重複を削除
day.insert(5, '土') # 6番目に土を追加
day.insert(0, '日') # 0番目に日を追加
print(day)
