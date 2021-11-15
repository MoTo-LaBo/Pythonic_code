# ---------- Prepare Coins (利用硬貨の最適化) ----------

def coin_num(price: int):
    """入力値 price から最小の硬貨の枚数を出力

    Args:
        price (int): 0 ~ 1000円までの金額

    Returns:
        [int]: [count] 硬貨の枚数
    """

    if not 0 < price <= 1000:
        return

    coins = [500, 100, 50, 10, 5, 1]
    count = 0

    for pay in coins:
        coin_num, price = divmod(price, pay)
        if price >= 0:
            count += coin_num

    return count


def main():
    print('\n ---------- Prepare Coins (利用硬貨の最適化) ---------- \n')
    while True:
        try:
            input_value = int(input('1000円以下の金額を入力して下さい >> '))
            result = coin_num(input_value)

            if result:
                print(f'\n硬貨の枚数: {result} 枚')
                break
            else:
                print(f'1 ~ 1000円以内で入力して下さい: {input_value} 円?\n')
                continue

        except ValueError:
            print(f'入力 Errorです。数字を入力して下さい\n')
            continue


if __name__ == "__main__":
    main()
