# ---------- word-count : 単語カウントの課題 ----------
import re
import os
from collections import Counter


def word_count(file):
    with open(file) as f:
        txt = f.read()
        word = re.findall(r'\w+', txt.lower())
        words = Counter(word).most_common()
        for i in words:
            k, v = i
            print(f'{k} : {v}')


def main():

    print('\n\t---------- Word Count ---------- \n')

    while True:
        input_value = input('file を入力してください(xxx.txt | xxx/yyy/zzz.py) >>> ')
        # 入力された値が適切な file or path かどうか判定
        result = re.fullmatch('\w+\.[a-zA-Z]{1,4}$', os.path.basename(input_value))
        if result:
            try:
                word_count(input_value)
                break
            except:
                print(f'No such file or directory: {input_value} ?')
        else:
            print(f'{input_value}: 入力が正しくありません\n')
            continue


if __name__ == "__main__":
    main()
