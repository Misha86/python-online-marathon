"""3 question 1 sprint"""


def isPalindrome(str):
    """
    Check string is palindrome
    :param str: str
    :return: bool
    """
    d = ''
    for s in str:
        c = str.count(s)
        if c % 2 and s not in d:
            d += s
    res = True if len(d) == 1 or d == '' else False
    return res


if __name__ == '__main__':
    s = "A"
    res = isPalindrome(s)
    print(res)


