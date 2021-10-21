
# ------------- Linear Search (線形探索) ① ------------- #
from random import sample

numbers = sample(range(0, 11), 10)


def linear_search(num, numbers):
    for i, v in enumerate(numbers):
        if num == v:
            return i
        else:
            continue
    return


ls = linear_search(5, numbers)
print(f'list: {numbers}\nindex: {ls}')


# ------------- Global Linear Search ② ------------- #

letters = "datasciencehub"


def global_linear_search(word, obj):
    idx_list = [i for i, v in enumerate(obj) if word == v]
    return idx_list


gls = global_linear_search('e', letters)
print(f'letter: {letters}\nindex: {gls}')
