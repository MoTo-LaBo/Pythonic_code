
# ---------- roman-numerals : ローマ数字変換の課題 ----------

numerical_value = {
    1000: 'M',
    900: 'CM',
    500: 'D',
    400: 'CD',
    100: 'C',
    90: 'XC',
    50: 'L',
    40: 'XL',
    10: 'X',
    9: 'IX',
    5: 'V',
    4: 'IV',
    1: 'I'
}


def convert_to_roman(num):
    roman_list = []
    for a_num, r_num in numerical_value.items():
        i, num = divmod(num, a_num)
        if i != 0:
            roman_list.append(r_num * i)
        elif num == 0:
            break
    return ''.join(roman_list)


def main():

    print('\n ----- Conversion to Roman numerals ----- \n')

    while True:
        input_value = input('1 ~ 3999以下の自然数を入力してください >>> ')
        # 入力された値(string) が数値かどうか判定　ー＞ int(integer)型へ
        if input_value.isdecimal():
            i_num = int(input_value)

            # 判定後の処理　-> 正常な入力値か？の振り分け 1 ~ 3999 の領域を指定
            if 1 <= i_num <= 3999:
                # Roman Numerals に変換
                print(
                    f'\nArabic Number : {i_num}\nRoman Numerals: {convert_to_roman(i_num)}')
                break

            # 1 ~ 3999 の領域を外れた場合の処理, その他例外全て
            else:
                print(f'\n{i_num}は値の範囲以外です\n1 ~ 3999以下の自然数ので入力して下さい\n')
                continue

        # 数字以外だった場合 & float(小数)の判定 -> float(小数)だった場合の処理
        elif not input_value.isdecimal():
            try:
                f_num = float(input_value)
                print(f'\n入力された値は >> {f_num} << です\n1 ~ 3999以下の自然数を入力してください\n')
                continue

            except ValueError:
                print(
                    f'\n入力された値は >> {input_value} << です。\n1 ~ 3999以下の自然数を入力してください\n')

        # その他の例外処理
        else:
            print(
                f'\n入力された値は >> {input_value} << です。\n1 ~ 3999以下の自然数を入力してください\n')
            continue


if __name__ == "__main__":
    main()
