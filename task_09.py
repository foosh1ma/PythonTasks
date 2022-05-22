def connect_dicts(dict1, dict2):
    sum_1 = sum(dict1.values())
    sum_2 = sum(dict2.values())
    if sum_1 > sum_2:       # dict1 priority
        a, b = dict1, dict2
    else:           # dict2 priority
        a, b = dict2, dict1

    a = {key: value for key, value in a.items() if value >= 10}
    b = {key: value for key, value in b.items() if value >= 10}

    b.update(a)
    return dict(sorted(b.items(), reverse=True))


print(connect_dicts({"a": 2, "b": 12}, {"c": 11, "e": 5}))
print(connect_dicts({"a": 13, "b": 9, "d": 11}, {"c": 12, "a": 15}))
print(connect_dicts({"a": 14, "b": 12}, {"c": 11, "a": 15}))
