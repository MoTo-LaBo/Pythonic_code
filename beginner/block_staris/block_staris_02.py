
# ------------- Stairs with blocks (ブロック階段) ver 2 ------------- #


# ---------- 総和を求める function ---------- #
def sum_total(num: int):
    if num % 2 == 0:
        odd = (num / 2) * (num + 1)
        return int(odd)
    else:
        even = ((num + 1) / 2) * num
        return int(even)


# ---------- block_staris function ---------- #

def block_stairs(num):

    block = ''
    count = 0

    # 1<= n <= 10*10 判定
    if 1 <= num <= 10 ** 10:

        if num == 1:
            num = num + 1

        # range 1 ~ 入力値分回す
        for i in range(1, num):

            # i の総和を求めて, 入力値から i の総和を引く(num の値が引けなくなるまで loop)
            n = num - (sum_total(i))

            # 総和を引いた値 n の値で階段を出力範囲を判定
            if n >= 0:
                count = i
                block = i * "□"
                print(f'{block}')
            # num (入力値) が引けなくなった時点で終了
            else:
                break
    else:
        return

    return count


def main():

    print('------- Stairs with blocks (ブロック階段) ver 2 --------')

    while True:

        num = input('\n 1以上 ~ 10 x 10 (100億)以下の自然数を入力して下さい >> ')
        # 入力された値(string) が数値かどうか判定　ー＞ int(integer)型へ
        if num.isdecimal():
            i_num = int(num)

            # block_stairs　func で段数を数えて出力
            stairs = block_stairs(i_num)
            if stairs != None:
                print(f'steps: {stairs} 入力値: {num}')
                break
            else:
                print(f'入力値 >> {num} << は範囲外です\n')

        # 数字以外だった場合 & float(小数)の判定 -> float(小数)だった場合の処理
        elif not num.isdecimal():
            try:
                n_fnum = float(num)
                print(f'\n入力が少数です >> {n_fnum} << 1~100以下の自然数ので入力して下さい')

            except ValueError:
                print(f'\n入力Errorです >> {num} << 正しい値を入力して下さい')

        # その他処理
        else:
            print(f'\n入力 Error です >> {num} << 1~100億以下の自然数ので入力して下さい')


if __name__ == "__main__":
    main()
