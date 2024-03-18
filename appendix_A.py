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



