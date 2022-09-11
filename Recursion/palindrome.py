"""
def reverse(s):
    assert isinstance(s, str), 'Not a string'
    if len(s) in (0, 1):
        return s
    return s[-1] + reverse(s[:-1])


def isPalindrome(strng):
    first_half = (len(strng) // 2) + +1
    first_half = strng[:first_half]
    if reverse(first_half) == strng[first_half:]:
        return True
    else:
        return False
"""


def isPalindrome(strng):
    assert isinstance(strng, str), 'Not a string'
    if len(strng) in (0, 1):
        return True
    if strng[0] == strng[-1] and isPalindrome(strng[1:-1]):
        return True
    return False
