# %% [markdown]
# # Linear Search
# - 線形探索
# %%
from random import sample
# %%
numbers = sample(range(0, 11), 10)
numbers
# %%


def linear_searcth(num, numbers):
    for i, v in enumerate(numbers):
        if num == v:
            return i
        else:
            continue


# %%
print(f'list: {numbers}')
ls = linear_searcth(11, numbers)
print(f'index: {ls}')

# %% [markdown]
# # Global Linear Search
# - 要素が見つかった index を全て list 形式で返す
# %%
letters = "datasciencehub"


def global_linear_search(word, obj):

    idx_list = []

    for i, v in enumerate(obj):
        if word == v:
            idx_list.append(i)
    return idx_list


global_linear_search('e', letters)
# %%


def global_linear_search(word, obj):
    idx_list = [i for i, v in enumerate(obj) if word == v]
    return idx_list


# %%
gls = global_linear_search('e', letters)
print(f'index: {gls}')
# %%
