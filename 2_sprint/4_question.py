"""4 question 2 sprint"""

import re


def pretty_message(s: str) -> str:
    str_re = re.sub(r'([a-z])\1+', r'\1', s)
    str_re1 = re.sub(r'([a-z]{2,3})\1+', r'\1', str_re)

    return str_re1


if __name__ == '__main__':
    data = "Thisssssssss isisisis echooooooo stringggg. Replaceaceaceace repeatedededed groupssss of symbolssss"
    result = pretty_message(data)
    print(result)
