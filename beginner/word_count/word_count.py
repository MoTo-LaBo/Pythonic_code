# ---------- word-count : 単語カウントの課題 ----------
import re
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
        input_value = input('.txt file を入力してください(xxx.txt) >>> ')
        # 入力された値が適切な file かどうか判定
        result = re.fullmatch('\w+\.txt$', input_value)
        if result:
            try:
                word_count(input_value)
                break
            except:
                print(f'そのような file はありません >> {input_value} ?\n')
        else:
            print(f'入力が正しくありません >> {input_value} <<\n')
        continue


if __name__ == "__main__":
    main()
