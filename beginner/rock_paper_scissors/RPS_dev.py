import re
import random


def main():

    print('------- Stairs with blocks (ブロック階段) --------')

    user_txt = """
    r, p, s の中から一つ選んで下さい\n
    r: rock(グー)
    p: paper(パー)
    s: scissors(チョキ)\n
    """

    while True:
        user = input(user_txt)
        try:
            result = re.fullmatch('\w+ |r|p|s{1}$', user)

            if result:
                rps = ["r", "p", "s"]
                rps_list = ["rock", "paper", "scissors"]

                pc = random.choice(rps)

                for i, v in enumerate(rps):
                    if user == v:
                        user = i

                for i2, v2 in enumerate(rps_list):
                    if user == i2:
                        user_v = v2

                for i3, v3 in enumerate(rps):
                    if pc == v3:
                        pc = i3

                for i4, v4 in enumerate(rps_list):
                    if pc == i4:
                        pc_v = v4

                if user == pc:
                    print(f'\nDRAW\nYour choice: {user_v}\nPC\'s choice: {pc_v}')
                    break
                elif user == 2 and pc == 1 or user == 1 and pc == 0 or user == 0 and pc == 2:
                    print(f'\nWIN\nYour choice: {user_v}\nPC\'s choice: {pc_v}')
                    break
                elif user == 0 and pc == 1 or user == 1 and pc == 2 or user == 2 and pc == 0:
                    print(f'\nLOSE\nYour choice: {user_v}\nPC\'s choice: {pc_v}')
                    break
            else:
                print(f'r, p, s の中から選んで下さい: {user} ?')
                continue

        except:
            print(f'入力値は正しいですか: {user} ?')
            continue


if __name__ == "__main__":
    main()
