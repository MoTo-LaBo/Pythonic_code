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

Celsius2 = sample(range(0, 40), 10)
Fahrenheit = [f'{1.8 * i + 32:.3g}°F' for i in Celsius2]
print(Fahrenheit)



# ------------- 摂氏 -> 華氏 (conversion) error handlig 漏れ有り ------------- #
"""
・C° ー＞ °F conversion を interactive にする

        - 今日の気温を入力すれば華氏へ変換して出力してくれる

・error handling 漏れ発覚...

    - 全角文字に対して program が強制終了してしまう
    - 半角でも文字列同じ現象が起きる
"""
"""
while True:
    celsius_num = input('今日の気温を入力して下さい >>> ')
    # 入力された値(string) が数値かどうか判定　ー＞ int(integer)型へ
    if celsius_num.isdecimal():
        c_num = int(celsius_num)

        # 判定後の処理　-> 正常な入力値か？(正常な気温か？の振り分け)　-20°C ~ 40°C の一般的な領域を指定
        match c_num:
            case int() if c_num >= -20 and c_num < 40:
                print(f'華氏 : {1.8 * c_num + 32:.3g} °Fです')
                break
            # -20°C ~ 40°C の領域を外れた場合の処理, その他例外全て (半角でなかった場合も含む)
            case _:
                print(f'入力 Error です\n -20 ~ 40 or -20.0 ~ 40.0 の間で入力をお願いします >>> ')
                continue

    # 数字入力でなかった場合の処理 & 小数点込みの入力だった場合の処理
    else:
        c_fnum = float(celsius_num)
        match c_fnum:
            case float() if c_fnum >= -20 and c_fnum < 40:
                print(f'華氏 : {1.8 * c_fnum + 32:.3g} °Fです')
                break
            # -20°C ~ 40°C の領域を外れた場合の処理, その他例外全て (半角でなかった場合も含む)
            case _:
                print(f'入力 Error です\n -20 ~ 40 or -20.0 ~ 40.0 の間で入力をお願いします >>> ')
                continue
"""


while True:
    celsius_num = input('今日の気温を入力して下さい >>> ')
    # 入力された値(string) が数値かどうか判定　ー＞ int(integer)型へ
    if celsius_num.isdecimal():
        c_num = int(celsius_num)

        # 判定後の処理　-> 正常な入力値か？(正常な気温か？の振り分け)　-20°C ~ 40°C の一般的な領域を指定
        match c_num:
            case int() if c_num >= -20 and c_num < 40:
                print(f'華氏 -> {1.8 * c_num + 32:.3g} °Fです')
                break
            # -20°C ~ 40°C の領域を外れた場合の処理, その他例外全て (半角でなかった場合も含む)
            case _:
                print(f'入力 Error です\n -20 ~ 40 or -20.0 ~ 40.0 の間で入力して下さい')
                continue

    # 数字以外だった場合 & float(小数)の判定 -> float(小数)だった場合の処理
    elif not celsius_num.isdecimal():
        try:
            c_fnum = float(celsius_num)
            match c_fnum:
                case float() if c_fnum >= -20 and c_fnum < 40:
                    print(f'華氏 : {1.8 * c_fnum + 32:.3g} °Fです')
                    break
                # -20°C ~ 40°C の領域を外れた場合の処理, その他例外全て (半角でなかった場合も含む)
                case _:
                    print(f'入力 Error です\n -20 ~ 40 or -20.0 ~ 40.0 の間で入力して下さい')
                    continue
        except ValueError:
            print(f'入力された値は{celsius_num}です。\n数字の 20 ~ 40 or -20.0 ~ 40.0 の間で入力して下さい')
            continue

    # その他の場合の処理
    else:
        print(f'入力された値は{celsius_num}です。\n数字の 20 ~ 40 or -20.0 ~ 40.0 の間で入力して下さい')
        continue
