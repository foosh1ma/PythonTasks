def max_odd(array):
    res = []
    for i in array:
        if isinstance(i, (int, float)) and i % 2 == 1:
            res.append(i)
    return max(res) if len(res) != 0 else None


print(max_odd([1, 2, 3, 4, 4]))                     # => 3
print(max_odd([21.0, 2, 3, 4, 4]))                  # => 21
print(max_odd(['ololo', 2, 3, 4, [1, 2], None]))    # => 3
print(max_odd(['ololo', 'fufufu']))                 # => None
print(max_odd([2, 2, 4]))                           # => None
