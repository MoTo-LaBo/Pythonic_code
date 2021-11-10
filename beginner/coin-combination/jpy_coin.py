def cul_price(five, ten, five_hundred):

    f_num = five * 5
    t_num = ten * 10

    # 5円が2枚以上 and 10円が1枚以上 and 5円と10円の合計が 500円以下
    if five >= 2 & ten >= 1 & f_num + t_num < 500:

        # 10円を5円に両替する -> (five + 1)通り
        five = five + (ten * 2) + 1

        # 0 = 1通りなので
        five_hundred += 1
        return five * five_hundred - 1

    # 500円以上であれば 500円も5円に両替 : 全て(five + 1) 通りにする
    elif f_num + t_num >= 500:
        return five + (five_hundred * 100) - 1

    # 上記以外の場合
    else:
        five += 1
        ten += 1
        five_hundred += 1

        return five * ten * five_hundred - 1


def main():

    explanation = '''
    5円, 10円, 500円 の制限枚数 ↓\n
    0 <= 5円の枚数   <= 10000
    0 <= 10円の枚数  <= 10000
    0 <= 500円の枚数 <= 10000
    '''

    print('\n--- coin-combination:(支払い金額の組み合わせ) ---')
    print(f'\t{explanation}')

    while True:
        try:
            five = int(input('5円の枚数を入力して下さい >> '))
            ten = int(input('\n10円の枚数を入力して下さい >> '))
            five_hundred = int(input('\n500円の枚数を入力して下さい >> '))

            print(f'\n\t{cul_price(five, ten, five_hundred)} 通り')
            break

        except:
            print(f'\t入力値は正しいですか ↑ ↑ ↑\n')
            continue


if __name__ == "__main__":
    main()
