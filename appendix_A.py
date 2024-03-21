# A.1　データ型

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

# A.2　リスト型 
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
上の記法をリスト内包表記という
forループを使って新しいリストを作成する際に使える
[式 for アイテム in イテラブル if 条件]
↑公式
式: 新しいリストの各要素に対して評価される式。これには、ループの各アイテムを使って計算を行うことができる。
アイテム: イテラブルから取り出される現在のアイテム。
イテラブル: リスト、タプル、辞書、セット、ジェネレータなど、繰り返し処理が可能なオブジェクト。
条件: オプション。真の場合にのみ、アイテムが新しいリストに含まれる。
単純なforループで書くと下の通り
Fruits = []
for fruit in fruits:
    Fruits.append(fruit.capitalize())  # 文字列の頭文字を大文字に変換
print(Fruits)
'''

# A.3　辞書型
prices = {
    'apple' : '100',
    'orange' : '150',
    'grape' : '300',
}
#解説
'''
コロン前の'apple'や'orange'はkey等という。最後のカンマは付けておくとエラーが減らせる
'''
prices = dict(
    apple = 300,
    orange = 150,
    grape = 300,
)
# 解説
'''
こっちはkeyにstringのみ使える。上の{}ではintやtupleを指定できる
'''
prices = {}
prices['apple'] = 100
prices['grape'] = 150
prices['orange'] = 300
# 解説
'''
一旦からの辞書を作っておいて後から要素を追加
もしキーがすでに存在している場合、保存されているデータが上書きされる
'''
test1 = prices.get('banana', 0)
test2 = prices.get('banana')
print(test1)
print(test2)
# 実行結果
'''
>>> print(test1)
0
>>> print(test2)
None
'''
#解説
'''
この.get()メソッドは、辞書から指定されたキーの値を取得するために使用され、
キーが存在しない場合にデフォルト値を指定できる。
上の上書き方式で初期化するとき、キーがないとエラーがでるが
.get()を使えばデフォルト値を設定できてエラーを避けることができる。
'''
for key in prices.keys():  #case1(key)
    print(key)

for val in prices.values():  #case2(value)
    print(val)

for key, val in prices.items():
    print(key, val)
#実行結果
'''>>> for key in prices.keys():  #case1(key)
...     print(key)
...
apple
grape
orange
>>> for val in prices.values():  #case2(value)
...     print(val)
...
100
150
300
>>> for key, val in prices.items():
...     print(key, val)
...
apple 100
grape 150
orange 300
'''
# 解説
'''
辞書型変数ループには、目的に応じてkeys(),values(),items()の3つのメソッドを使い分ける
case1はkeyのみ必要な場合、case2は値のみ必要な場合、case3はkeyと値が必要な場合
ループで現れる要素の順番は追加した順番と必ずしも一致する訳ではない
順番を保持したい場合はdictの代わりにcollection.OrderDictを利用する
'''
prices = {fruit.capitalize(): price for fruit, price in prices.items()}
print(prices)
# 実行結果
'''
>>> print(prices)
{'Apple': 100, 'Grape': 150, 'Orange': 300}
'''

# A.4　その他のコンテナデータ型
# tuple
x = (1.0, 2)
'''
tupleは変更不可能な配列
リストに似ているが、使い分けとして特定の場面でtupleを使うことが多い
<特定の場面>
1, 配列の中身を変更したくない
2, 辞書型のキーに使う場合
辞書型のキーは変更可能であるリストを受け付けないため
例x = {}
  x[(0,1)] = 1.5
Pythonの辞書xを定義して、キーとしてタプル(0, 1)を使って、その値に1.5を割り当てている。
Pythonの辞書は、特有なキーとそれに関連する値のペアの集合。
ここで、キーはtuple(0, 1)で、対応する値は浮動小数点数の1.5。
3, tupleと==で比較する場合
NumPy配列で比較する場合(未習)
'''
# 集合型(set)
'''
集合を表す為のコンテナ。要素の重複を許さず、順番は保持されない。
和集合や積集合等の演算が利用できる。ただ、数値計算の使い方は限られる。
'''
v = [1, 5, 3, 5, 1, 4]
list(set(v))
# 実行結果
'''
>>> v = [1, 5, 3, 5, 1, 4]
>>> list(set(v))
[1, 3, 4, 5]
'''
# 解説
'''
リストvから重複を排除して、その要素を持つ新しいリストを作成している。
step1) vとして[1, 5, 3, 5, 1, 4]のリストが定義されている。
step2)set(v)を使ってリストvの要素から重複を排除し、集合（set）を作成している。
      集合は重複を許さないので、set(v)の結果は重複のない要素{1, 3, 4, 5}となる。
step3)この集合をlist()関数に通すことで、重複のない要素を持つ新しいリスト[1, 3, 4, 5]が得られる。
注意点:集合をリストに変換する際、要素の順序が元のリストvの順序とは異なる場合がある。
この例では偶然にもソートされたように見えるが、実際には集合の実装によって順序が保証されていないため、異なる順序で要素が返されることがある。
順番が不定になることを避けるにはsorted(set(v))等とする必要がある。
'''
# collectionモジュール
'''
ライブラリのはなし。メソッドとか多く出てくるからこれは本章に回すことにする。(いつか加筆するかも)
'''



