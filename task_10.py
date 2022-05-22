import re


def count_words(string):
    res = {}
    words = re.sub(r'[^a-zа-яё]', ' ', string.lower()).split()
    for word in words:
        if word in res:
            res[word] += 1
        else:
            res[word] = 1
    return res


print(count_words("A man, a plan, a canal -- Panama"))  # {'a': 3, 'man': 1, 'plan': 1, 'canal': 1, 'panama': 1}
print(count_words("Doo bee doo bee doo"))               # {'doo': 3, 'bee': 2}
