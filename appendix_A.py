# A.1データ型

# 数値型
x = 2 - 3j
type(x)
# 実行結果
'''
>>> x = 2 - 3j
>>> type(x)
<class 'complex'>
'''
# 解説
'''
type()は変数の型を見ることができる
complexは複素数
3jのjは複素数のiに対応
＊型に注意*整数÷整数は必ず実数になるらしい
'''

# コンテナデータ型 
''' データの集合をメモリに格納するが、その後の行う処理に応じて適切なデータ構造を選ばなければならない 
メモリ上にデータを格納する型をコンテナと呼ぶ 
コンテナデータ型は4種類 
1,リストlist 
2,タプルtuple 
3,辞書dict 
4,集合set ''' 

# リスト型 
x = [1, 2.0, "apple"] # case1 
print(x) 
x = [] #case2
x.append(1)
x.append(2.0) 
x.append("apple") 
print(x) 
# 実行結果 
''' 
>>> x = [1, 2.0, "apple"] # case1 
>>> print(x) [1, 2.0, 'apple'] 
>>> x = [] #case2 
>>> x.append(1) 
>>> x.append(2.0) 
>>> x.append("apple") 
>>> print(x) [1, 2.0, 'apple'] 
''' 
#解説
'''
0から始まるラベル付けされた1次元配列
case1)生成と同時に初期化を行う
case2)一旦からのリストを作っておいてからappendメソッドを使って要素を追加
リストにはどんな型のデータでも格納できる(ただしごちゃ混ぜは推奨しない)
'''
fruits = ['apple', 'orange', 'grape']
for fruit in fruits:  #case1
    print(fruit)
#実行結果
'''
>>> fruits = ['apple', 'orange', 'grape']
>>> for fruit in fruits:
...     print(fruit)
... 
apple
orange
grape
'''
for i, fruit in enumerate(fruits):  #case2
    print(i, fruit)
#実行結果
'''
>>> for i, fruit in enumerate(fruits):
...     print(i, fruit)
... 
0 apple
1 orange
2 grape
'''
#解説
'''
case2はインデックスが必要な場合
enumerate関数を使用している。
この関数は、ループの各繰り返しでアイテムのインデックスとその値を与える。
ここでは、iがインデックス（0から始まる）を、fruitがその時点でのアイテムの値を保持する。
この方法は、アイテムの値だけでなく、その位置（インデックス）も重要な場合に便利。
'''
Fruits = [fruit.capitalize() for fruit in fruits]
print(Fruits)
# 実行結果
'''
>>> Fruits = [fruit.capitalize() for fruit in fruits]
>>> print(Fruits)
['Apple', 'Orange', 'Grape']
'''
# 解説
'''
上の記法をリスト内表記という
forループを使って新しいリストを作成する際に使える
単純なforループで書くと下の通り
Fruits = []
for fruit in fruits:
    Fruits.append(fruit.capitalize())  # 文字列の頭文字を大文字に変換
print(Fruits)
'''
