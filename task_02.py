def coincidence(lst=[], rng=[]):
    # res = []
    # for i in lst:
    #     if isinstance(i, (int, float)):
    #         if rng[0] <= i <= rng[-1]:
    #             res.append(i)
    # return res
    return [i for i in lst if isinstance(i, (int, float)) and rng[0] <= i <= rng[-1]]


print(coincidence([1, 2, 3, 4, 5], range(3, 6)))                # => [3, 4, 5]
print(coincidence())                                            # => []
print(coincidence([None, 1, 'foo', 4, 2, 2.5], range(1, 4)))    # => [1, 2, 2.5]
