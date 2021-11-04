
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

    block = '□'
    stairs = 1
    total = 1
    inupt_num = num

    while total <= inupt_num:

        print(block)
        stairs += 1
        block += '□'

        total = sum_total(stairs)

    else:
        return stairs


# ---------- main( ) function : Stairs with blocks ---------- #


def main():

    print('------- Stairs with blocks (ブロック階段) --------')

    while True:

        num = input('\n 1以上 ~ 10 x 10 (100億)以下の自然数を入力して下さい >> ')
        # 入力された値(str) が数値かどうか判定　ー＞ int(integer)型へ & # 1<= n <= 10*10 判定
        if num.isdecimal():
            i_num = int(num)

            # 1<= n <= 10*10 判定
            if 1 <= i_num <= 10 ** 10:

                # block_stairs　func で段数を数えて出力
                stairs = block_stairs(i_num)
                print(f'入力値 : {num}, setps : {stairs}')
                break

            else:
                print(f'入力値 >> {num} << は範囲外です\n')

        # 数字以外だった場合 & float(小数)の判定 -> float(小数)だった場合の処理
        elif not num.isdecimal():
            try:
                n_fnum = float(num)
                print(f'\n入力値が小数です >> {n_fnum} << 1~100以下の自然数ので入力して下さい')

            except ValueError:
                print(f'\n入力Errorです >> {num} << 正しい値を入力して下さい')

        # その他処理
        else:
            print(f'\n入力 Error です >> {num} << 1~100億以下の自然数ので入力して下さい')


if __name__ == "__main__":
    main()
