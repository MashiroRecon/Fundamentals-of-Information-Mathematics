#  [6] リスト

#  リストの作成

#  リスト型
#  -書式-
#  'リスト変数' = ['0番目の要素', '1番目の要素', ...]
#  --

#  リストの指定
#  -書式-
#  list
#  (リスト全体を指定)
#  --
#  list['指定したい要素の番号']
#  (指定した番号の要素を指定)
#  --

list_a = [10, 20, 30, 40, 50]
print(list_a[2])

list_b = [10, 20, 30, 40, 50]
list_b[3] = 100
print(list_b)

#  要素の追加

#  appendメゾット
#  リスト末尾に要素を追加する
#  -書式-
#  'リスト変数'.append('追加したい要素')
#  --
#  (追記:リストを引数として渡した場合は、結合されず要素として追加される)

list_c = []
list_c.append(10)
list_c.append(20)
print(list_c)
print(list_c[0])

list_d = list(range(3))
print(list_d)
list_d.append([3, 4, 5])
print(list_d)

#  その他書き残し

#  insertメゾット
#  リストの指定位置に要素を挿入する
#  -書式-
#  'リスト変数'.insert('追加したい位置の要素番号', '挿入する要素')
#  --
#  (追記:リストを引数とした場合は、結合されずに要素として追加される)

list_e = list(range(3))
print(list_e)
list_e.insert(0, 100)
list_e.insert(-1, 200)
print(list_e)

list_e.insert(0, [-1, -2, -3])
print(list_e)

#  extendメゾット
#  リスト末尾に他のリストやタプルを結合する
#  -書式-
#  'リスト変数'.extend('結合したいリストなど')
#  --
#  (追記:文字列は一文字づつリストに追加される)

list_f = list(range(3))
print(list_f)
list_f.extend([100, 200, 300])
print(list_f)
list_f.extend((-1, -2, -3))
print(list_f)

list_f.extend("new")
print(list_f)

#  +,+=演算子
#  extendメゾットと同じくリストの結合を行う
#  -書式-
#  '新しいリスト変数' = '元になるリスト変数' + '結合したいリストなど'
#  --
#  'リスト変数' += '結合したいリスト'
#  -- 

list_g = list_f + [5, 6, 7]
print(list_g)

list_f += [5,6,7]
print(list_f)

#  スライス指定
#  スライスで指定した範囲に挿入もしくは置換を行う
#  -書式-
#  'リスト変数'['追加したい位置の要素番号', '追加したい位置の要素番号'] = '追加したいリストなど'
#  (指定した位置の要素番号を先頭にして要素を挿入する形で結合する)
#  --
#  'リスト変数'['追加したい位置の先頭の要素番号', '置換する要素の最後の要素番号'] = '追加したいリストなど'
#  (指定した位置の要素番号が先頭になるように、指定した最後の要素番号までを置換する形で結合する)
#  --

list_h = list(range(3))
print(list_h)
list_h[1:1] = [100, 200, 300]
print(list_h)

list_i = list(range(3))
print(list_i)
list_i[1:2] = [100, 200, 300]
print(list_i)
