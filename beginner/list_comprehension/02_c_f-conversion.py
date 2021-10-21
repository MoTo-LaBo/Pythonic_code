
# ------------- 摂氏 -> 華氏 (conversion) error handlig 漏れ有り ------------- #

"""
        C° ー＞ °F conversion を interactive にする

        「 今日の気温を入力すれば華氏へ変換して出力してくれる 」

・error handling 漏れ発覚...
    - 全角文字に対して program が強制終了してしまう
    - 半角でも文字列同じ現象が起きる
"""

# while True:
#     celsius_num = input('今日の気温を入力して下さい >>> ')
#     # 入力された値(string) が数値かどうか判定　ー＞ int(integer)型へ
#     if celsius_num.isdecimal():
#         c_num = int(celsius_num)

#         # 判定後の処理　-> 正常な入力値か？(正常な気温か？の振り分け)　-20°C ~ 40°C の一般的な領域を指定
#         match c_num:
#             case int() if c_num >= -20 and c_num < 40:
#                 print(f'華氏 : {1.8 * c_num + 32:.3g} °Fです')
#                 break
#             # -20°C ~ 40°C の領域を外れた場合の処理, その他例外全て (半角でなかった場合も含む)
#             case _:
#                 print(f'入力 Error です\n -20 ~ 40 or -20.0 ~ 40.0 の間で入力をお願いします >>> ')
#                 continue

#     # 数字入力でなかった場合の処理 & 小数点込みの入力だった場合の処理
#     else:
#         c_fnum = float(celsius_num)
#         match c_fnum:
#             case float() if c_fnum >= -20 and c_fnum < 40:
#                 print(f'華氏 : {1.8 * c_fnum + 32:.3g} °Fです')
#                 break
#             # -20°C ~ 40°C の領域を外れた場合の処理, その他例外全て (半角でなかった場合も含む)
#             case _:
#                 print(f'入力 Error です\n -20 ~ 40 or -20.0 ~ 40.0 の間で入力をお願いします >>> ')
#                 continue



# ------------- 摂氏 -> 華氏 (conversion) interactive 完成 ------------- #
"""
        C° ー＞ °F conversion を interactive にする

        「 今日の気温を入力すれば華氏へ変換して出力してくれる 」

"""

print('\n')
print('------------ 摂氏 -> 華氏 interactive 完成 -------------')


while True:
    celsius_num = input('\n今日の気温を入力して下さい >>> ')
    # 入力された値(string) が数値かどうか判定　ー＞ int(integer)型へ
    if celsius_num.isdecimal():
        c_num = int(celsius_num)

        # 判定後の処理　-> 正常な入力値か？(正常な気温か？の振り分け)　-20°C ~ 40°C の一般的な領域を指定
        match c_num:
            case int() if -20 <= c_num <= 40:
                print(f'\n華氏 -> {1.8 * c_num + 32:.1f} °Fです')
                break
            # -20°C ~ 40°C の領域を外れた場合の処理, その他例外全て (半角でなかった場合も含む)
            case _:
                print(f'\n入力 Error です\n -20 ~ 40 or -20.0 ~ 40.0 の間で入力して下さい')
                continue

    # 数字以外だった場合 & float(小数)の判定 -> float(小数)だった場合の処理
    elif not celsius_num.isdecimal():
        try:
            c_fnum = float(celsius_num)
            match c_fnum:
                case float() if -20 <= c_fnum <= 40:
                    print(f'\n華氏 -> {1.8 * c_fnum + 32:.1f} °Fです')
                    break
                # -20°C ~ 40°C の領域を外れた場合の処理, その他例外全て (半角でなかった場合も含む)
                case _:
                    print(f'\n入力 Error です\n -20 ~ 40 or -20.0 ~ 40.0 の間で入力して下さい')
                    continue
        except ValueError:
            print(f'\n入力された値は >> {celsius_num} << です。\n数字の 20 ~ 40 or -20.0 ~ 40.0 の間で入力して下さい')
            continue

    # その他の場合の処理
    else:
        print(f'\n入力された値は >> {celsius_num} << です。\n数字の 20 ~ 40 or -20.0 ~ 40.0 の間で入力して下さい')
        continue
