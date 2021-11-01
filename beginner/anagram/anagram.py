# ---------- anagram : アナグラム ----------
import re


def is_anagram(word1, word2):
    """word1, word2のAnagram 判定

    Args:
        word1 (str): 任意のローマ字・英単語
        word2 (str): 任意のローマ字・英単語

    Returns:
        boolean: Anagram = True or False
        None
    """

    # 入力された文字が適切な word かを判定
    result = re.match('\w[a-zA-Z]', word1) and re.match('\w[a-zA-Z]', word2)

    # 適切な word であれば　判定処理
    if result:

        # re.sub で特殊文字・空白を置き換え & lower で小文字へ変換
        w1 = re.sub(r'[\t\n\r\[\]{}!@#$%^&*()-=_+;:~\'\"<>/?,.|]', '', word1).lower()
        w2 = re.sub(r'[\t\n\r\[\]{}!@#$%^&*()-=_+;:~\'\"<>/?,.|]', '', word2).lower()

        # sorted で a, b, c 順に整える, return True or False
        return sorted(w1) == sorted(w2)

    # 不適切な word であれば　None
    else:
        return


def main():

    print('\n\t---------- Anagram Judgment ---------- \n')

    while True:
        try:
            # .split で入力値を複数取得
            w1, w2 = input('英単語を2つ入力して下さい(Listen, Silent) >> ').split()

            # Anagram 判定結果 or 入力値のfilterの結果 (True, False, None)
            judg = is_anagram(w1, w2)

            # return が None でなければ
            if judg != None:
                print(f'\ninput word :\t{w1} {w2}\nAnagrame :\t{judg}')
                break
            # return が None
            else:
                print(f'\n入力値は正しいですか ? >> {w1}, {w2}\n')

        except:
            print('\n入力は英単語 2つ にして下さい\n')


if __name__ == "__main__":
    main()
