import random #shuffleやrandintで利用可
import sys

words = [('apple', 'リンゴ'), ('banana', 'バナナ'), 
        ('coconut','ココナッツ'), ('doughnut','ドーナッツ'),  
        ('effort', '努力'), ('future', '未来'), ('gorilla', 'ゴリラ'), 
        ('house', '家'), ('information', '情報'), ('journey', '旅')]

questions = int(input('出題数を入力:'))

length = len(words)
if length < questions:
    print('登録された単語数以下の数値を入力してください:')
    sys.exit()

count = 0
correct = 0

while count < questions:
    random.shuffle(words)
    ans_index = random.randint(0, 3)
    print(f'問題{count + 1}:{words[ans_index][0]}の意味は?')

    for i in range(2):
        print(f'{i * 2 + 1}:{words[i * 2][1]}, {i * 2 + 2}:{words[i * 2 + 1][1]}')
    answer = input('1から4の数字で解答(終了する場合は"x"を入力):')
    if answer == "x":
        break
    print(f'あなたの解答:{answer}')
    if answer == str(ans_index + 1):
        print('正解!')
        correct += 1
    else:
        print('不正解! 正解は{ans_index + 1}の{words[ans_index][1]}でした')
    count += 1

print(f'成績:正解{correct}問 (全{count}問)')
