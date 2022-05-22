def sort_list(lst):
    if lst:
        res = []
        minimum = min(lst)
        maximum = max(lst)
        for elem in lst:
            if elem == maximum:
                res.append(minimum)
            elif elem == minimum:
                res.append(maximum)
            else:
                res.append(elem)
        res.append(minimum)
        return res
    else:
        return []


print(sort_list([]))            # => []
print(sort_list([2, 4, 6, 8]))  # => [8, 4, 6, 2, 2]
print(sort_list([1]))           # => [1, 1]
print(sort_list([1, 2, 1, 3]))  # => [3, 2, 3, 1, 1]
