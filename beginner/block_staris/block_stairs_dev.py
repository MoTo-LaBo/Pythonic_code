
# ------------- Stairs with blocks (ブロック階段) ver 1 ------------- #


def block_stairs(n):

    # 1<= n <= 10*10 判定
    if 1 <= n <= 10 ** 10:

        # block の箱と階段の数を count　変数宣言
        block = ''
        count = 0

        # 入力値 1 の場合だけ 0 になってしまうので,　予防処理
        if n == 1:
            n = n + 1

        # range 1 ~ 入力値分回す必要はないですが, loop を回す為に入力値を入れる
        for i in range(1, n):

            # 入力値がなくなるまで, i の値で引いていく
            n = n - i

            # 入力値がなくなるまで 階段生成 & count, 引けなくなったら終了
            if n >= 0:
                count = i
                block = (i * "□")
                print(f'{i} : {block}')
            else:
                break
    else:
        return

    return count


def main():

    print('------- Stairs with blocks (ブロック階段) ver 1 --------')

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
