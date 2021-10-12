
# ------------- 指定自然数 -> 倍数list生成 interactive 完成------------- #


"""
            1 ~ 100までの自然数を入力する

        入力した数の倍数 list が生成出力される

"""


print('\n')
print('------- 課題 ②：指定自然数の100以下の倍数一覧生成 --------')


while True:
    natural_num = input('\n1~100以下の自然数を１つ入力して下さい >>> ')
    # 入力された値(string) が数値かどうか判定　ー＞ int(integer)型へ
    if natural_num.isdecimal():
        n_num = int(natural_num)

        # 判定後の処理　-> 正常な入力値か？の振り分け 1 ~ 100 の領域を指定
        match n_num:
            case int() if n_num >= 1 and n_num <= 100:
                n_list = [i for i in range(n_num, 100, n_num)]
                print(f'\n自然数の倍数list : {n_list}')
                break
            # 1 ~ 100 の領域を外れた場合の処理, その他例外全て (半角でなかった場合も含む)
            case _:
                print(f'\n入力 Error です\n 1~100以下の自然数ので入力して下さい')
                continue

    # 数字以外だった場合 & float(小数)の判定 -> float(小数)だった場合の処理
    elif not natural_num.isdecimal():
        try:
            n_fnum = float(natural_num)
            print(f'\n入力された値は >> {n_fnum} << です。\n 1~100以下の自然数ので入力して下さい')
            continue
        except ValueError:
            print(f'\n入力された値は >> {natural_num} << です。\n数字の 1~100以下の自然数ので入力して下さい')
            continue

    # その他の場合の処理
    else:
        print(f'\n入力された値は >> {natural_num} << です。\n数字の 1~100以下の自然数ので入力して下さい')
        continue
