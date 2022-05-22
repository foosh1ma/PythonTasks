import re


def multiply_numbers(inputs=[]):
    res = 1
    inputs = re.findall(r'\d', str(inputs))
    if inputs:
        for number in inputs:
            res *= int(number)
        return res
    else:
        return None


print(multiply_numbers())            # => None
print(multiply_numbers('ss'))        # => None
print(multiply_numbers('1234'))      # => 24
print(multiply_numbers('sssdd34'))   # => 12
print(multiply_numbers(2.3))         # => 6
print(multiply_numbers([5, 6, 4]))   # => 120
