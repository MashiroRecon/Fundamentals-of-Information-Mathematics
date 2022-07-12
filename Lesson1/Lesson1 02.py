#  [3] 条件分岐

#  if文
#  条件式がTrueの時に処理を追加
#  -書式-
#  if '条件式':
#      '条件式がTrueの時に実行される処理'
#  --

#  その他書き残し

#  imput文
#  入力待機状態を作成し入力を文字として返す
#  -書式-
#  imput("'直前に出力させたい文字'")
#  --
#  値の変換
#  代入式に型指定を付与することで変換が可能
#  -書式(char型->int型)-
#  a = int(b)
#  --

a = int(input())
if a < 10:
    #  print("10未満です")
    print("Less than 10.")
    a + 10
a = a * 10
print(a)

#  if-else文
#  条件式によって処理を分岐
#  -書式-
#  if '条件式':
#      '条件式がTrueの時に実行される処理'
#  else :
#      '条件式がFalseの時に実行される処理'
#  --

b = int(input())
if b < 10:
    print("Less than 10.")
else:
    print("More than 10.")

c = int(input())
if c < 10:
    print("Less than 10.")
else:
    if c < 20:
        print("10 to less than 20.")

#  if-elif文
#  条件によって処理を複数に分岐
#  -書式-
#  if '条件式':
#      '条件式がTrueの時に実行される処理'
#  elif '条件式':
#      '前の条件式がFalseかつ条件式がTrueの時に実行される処理'
#  else :
#      '前の条件式が全てFalseの時に実行される処理'
#  --

d = int(input())
if d < 10:
    print("Less than 10.")
elif d < 20:
    print("10 to less than 20.")
elif d < 30:
    print("20 to less than 30.")
else:
    print("More than 30.")

#  [4] 繰り返し処理

#  while文
#  条件式がTrueの間、内部の処理を繰り返す
#  -書式-
#  while '条件式':
#      '条件式がTrueの間、繰り返される処理'
#  --

e = 1
sum_e = 0
while e < 11:
    print(e)
    sum_e = sum_e + e
    e = e + 1
print("Sum = ", sum_e)

#  for文
#  条件式での指定したものを指定変数に代入し、内部の処理を繰り返す
#  指定が終了した場合、繰り返し処理を終了する
#  -書式-
#  for '指定変数' in '代入の条件式':
#      '変数に値が代入される間、繰り返される処理'
#  --

#  その他書き残し

#  range文
#  引数で指定した条件で返り値を返す
#  -書式-
#  range('返り値を返す条件値(未満)')
#  (指定値未満の間、0~順に返す)
#  --
#  range('出力する最小値', '返り値を返す条件値(未満)')
#  (指定値未満の間、指定した最小値から順に返す)
#  --
#  range('出力する最小値', '返り値を返す条件値(未満)', '増加量')
#  (指定値未満の間、指定した最小値から増加量ずつ増加させて返す)
#  --

sum_f = 0
for f in range(11):
    print(f)
    sum_f = sum_f + f
print("Sum = ", sum_f)

sum_g = 0
for g in [1, 10, 100, 1000]:
    print(g)
    sun_g = sum_g + g
print("Sum = ", sum_g)

sum_h = ""
for h in ["a", "b", "c", "d"]:
    print(h)
    sum_h = sum_h + h
print("Sum = ", sum_h)
