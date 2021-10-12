# import numpy as np
from random import sample

# ------------- 摂氏 -> 華氏 (conversion) prototype 1 ------------- #
"""
1. numpy randint で 0 ~ 40 の乱数生成を 10 個生成
   vector（配列）なので, list へ変換

2. list comprehension -> for loop & enumerate で index, value　を取得
　　value は list に変換したが, str型なので -> int型に変換

3. f string で出力 : 小数点以下の桁数、有効桁（有効数字）
> https://note.nkmk.me/python-f-strings/

"""

# Celsius = list(np.random.randint(0, 40, 10))
# Fahrenheit = [f'{1.8 * int(v) + 32:.3g}°F' for _, v in enumerate(Celsius)]
# print(Fahrenheit)


# ------------- 摂氏 -> 華氏 (conversion) 完成　list内包 version ------------- #
"""
## 上記の改善 code

・np.random.randint を使用しない

    - 配列の変換が不必要
    - numpy を install する必要性がない
    - python でも random な数は生成できる
    - code の短縮・可読性・分かり易さを考慮

    list内包表記を使用した program

"""

celsius2 = sample(range(0, 40), 10)
fahrenheit = [f'{1.8 * i + 32:.1f}°F' for i in celsius2]
print(fahrenheit)
