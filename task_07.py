def combine_anagrams(words_array):
    anagrams = {}
    for word in words_array:
        key = ''.join(sorted(word))
        if key in anagrams:
            anagrams[key].append(word)
        else:
            anagrams[key] = [word]
    return list(anagrams.values())


print(combine_anagrams(['cars', 'for', 'potatoes', 'racs', 'four', 'scar', 'creams', 'scream']))
# => [["cars", "racs", "scar"], ["four"], ["for"], ["potatoes"], ["creams", "scream"]]
