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
        result = re.fullmatch('\W+ |r|p|s|R|P|S{1}$', user)

        if result:

            rps = {"r": "rock", "p": "paper", "s": "scissors"}
            rps_k = list(rps.keys())

            pc = random.choice(rps_k)
            user = user.lower()

            for i, v in enumerate(rps):
                if user == v:
                    user = i

            for i2, v2 in enumerate(rps):
                if pc == v2:
                    pc = i2

            if user == pc:
                print(f'\nDRAW\nYour choice: {user}\nPC\'s choice: {pc}')
                continue
            elif user == 2 and pc == 1 or user == 1 and pc == 0 or user == 0 and pc == 2:
                print(f'\nWIN\nYour choice: {user}\nPC\'s choice: {pc}')
                break
            elif user == 0 and pc == 1 or user == 1 and pc == 2 or user == 2 and pc == 0:
                print(f'\nLOSE\nYour choice: {user}\nPC\'s choice: {pc}')
                break
        else:
            print(f'r, p, s の中から選んで下さい: {user} ?')
            continue


if __name__ == "__main__":
    main()
