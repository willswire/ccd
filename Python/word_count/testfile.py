# Refer to README.md for the problem instructions
import re


def word_count(fname):
    res_words = {}
    try:
        with open(fname) as file:
            for line in file:
                for word in line.split():
                    fword = re.sub(r"[^\w\s]", "", word)
                    fword = fword.lower()
                    print(fword)
                    if fword in res_words:
                        res_words[fword] += 1
                    else:
                        res_words[fword] = 1
    except:
        return None

    res_tot = sum(res_words.values())
    if res_tot == 0:
        return None

    res_max = max(res_words, key=res_words.get)

    return res_words, res_max, res_tot
