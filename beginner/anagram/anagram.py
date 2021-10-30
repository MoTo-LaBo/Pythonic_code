# ---------- anagram-challenge: アナグラムの課題 ----------
import re


def is_anagram(word1, word2):
    """word1, word2のAnagram 判定

    Args:
        word1 (str): 任意のローマ字・英単語
        word2 (str): 任意のローマ字・英単語

    Returns:
        boolean: Anagram = True | Not Anagrame != False
    """

    # re.sub で特殊文字・空白を置き換え & lower で小文字へ変換
    w1 = re.sub(r'[\t\n\r\[\]{}!@#$%^&*()-=_+;:~\'\"<>/?,.|]', '', word1).lower()
    w2 = re.sub(r'[\t\n\r\[\]{}!@#$%^&*()-=_+;:~\'\"<>/?,.|]', '', word2).lower()

    # sorted で a, b, c 順に整える
    list1 = sorted(w1)
    list2 = sorted(w2)

    # Anagram 判定
    if list1 == list2:
        return True
    else:
        return False


def main():

    print('\n\t---------- Anagram Judgment ---------- \n')

    while True:
        try:
            # .split で入力値を複数取得
            w1, w2 = input('英単語を2つ入力して下さい(Listen, Silent) >> ').split()

            # 入力された文字が適切な word かを判定
            result = re.match('\w[a-zA-Z]', w1) and re.match('\w[a-zA-Z]', w2)

            if result:
                try:
                    print(f'\ninput word :\t{w1} {w2}\nAnagrame :\t{is_anagram(w1, w2)}')
                    break

                except:
                    print(f'\n入力値は正しいですか ? >> {w1}, {w2}\n')

            else:
                print(f'\n入力値は正しいですか ? >> {w1}, {w2}\n')

        except:
            print('\n入力は英単語 2つ にして下さい\n')


if __name__ == "__main__":
    main()
