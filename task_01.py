import re


def is_palindrome(string):
    cleared = re.sub(r'[^a-zа-яё]', '', str(string).lower(), flags=re.IGNORECASE)
    return cleared == cleared[::-1]


print(is_palindrome("A man, a plan, a canal -- Panama"))    # => True
print(is_palindrome("Madam, I'm Adam!"))                    # => True
print(is_palindrome(333))                                   # => True
print(is_palindrome(None))                                  # => False
print(is_palindrome("Abracadabra"))                         # => False
