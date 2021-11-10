from random import sample
from collections import Counter

# ------------------ refactoring ① ------------------ #

# def shout_backwards(string):
#     all_caps = string.upper()
#     backwards = all_caps[::-1]
#     result = backwards + "!!!"
#     return result


# print(shout_backwards('DataScienceHub'))


print('\n')
print('-------------- refactoring (simple) ① ---------------')

"""
上記の関数をシンプルに refactoring する
"""

"""
lambda 関数を変数に入れる事は推奨されていないので修正
"""
# shout_backwards = lambda x: x[::-1].upper() + '!!!'


def shout_backwards(x): return x[::-1].upper() + '!!!'


print(shout_backwards('DataScienceHub'))


# ------------------ refactoring ② ------------------ #

# def squared_primes(array):
#     squared_primes = [z*z for z in [x for x in array if (len([y for y in range(2, x) if x % y == 0]) == 0) & (x > 1)]]
#     return squared_primes


# print(squared_primes([1, 3, 4, 7, 9, 10, 11, 13, 16, 43]))


"""
上記の code list内包表記１行だと見にくいので,可読性を良くするために refactoring する


        「 素数は１と自身の数(n)でしか割り切れない 」
         割り切れる要素が２つしかないという事 = 素数

    ・　python 標準ライブラリ collections　を使用
        - 割り切れた数が 2つの要素を抽出する為に使用

    ・　array の要素の数値を変えても対応できるように変更
        - ランダムに要素を生成する

    ・ import library

        from collections import Counter
        from random import sample

"""
array = [0, 1, 3, 4, 7, 9, 10, 11, 13, 16, 43]
# array = sample(range(0, 100), 10)

print('\n')
print('--------------- prime (素数の抽出のみ) ----------------')


# def primes(array):

#     prime = []

#     for i in array:
#         m = max(array)+1
#         for j in range(1, m):
#             if i % j == 0:
#                 prime.append(i)
#                 c = Counter(prime)

#     primes_list = [i for i in c if c[i] == 2]
#     return primes_list


# print(f'配列要素 : {array}')
# print(f'素数 : {primes(array)}')

"""
    上記の code 改善

    ・　余計なものを省いて分かりやすくする
        - Counter() いらない
        - max() いらない
        - list内包表記もいらない
"""


def primes(array):

    prime = []

    for i in array:
        if not i > 1:
            continue

        for j in range(2, i):
            if i % j == 0:
                break
        else:
            prime.append(i)

    return prime


print(f'配列要素 : {array}')
print(f'素数 : {primes(array)}')


print('\n')
print('------------------- refactoring ② --------------------')


"""
     code 改善

    ・　余計なものを省いて分かりやすくする
        - Counter() いらない
        - max() いらない
        - list内包表記もいらない
"""


def squared_primes(array):

    # prime = []

    # for i in array:
    #     m = max(array)+1
    #     for j in range(1, m):
    #         if i % j == 0:
    #             prime.append(i)
    #             c = Counter(prime)

    # s_p_list = [i*i for i in c if c[i] == 2]
    # return s_p_list

    prime = []

    for i in array:
        if not i > 1:
            continue

        for j in range(2, i):
            if i % j == 0:
                break
        else:
            prime.append(i*i)

    return prime


print(f'配列要素 : {array}')
print(f'素数 : {primes(array)}')
print(f'素数の2乗 : {squared_primes(array)}')
