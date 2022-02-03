"""4 question 2 sprint"""

import re


def pretty_message(s: str) -> str:
    str_re = re.sub(r'([a-z]|[a-z]{2,3})\1+\b', r'\1', s)
    return str_re


if __name__ == '__main__':
    data = "Thisssssssss isisisis echooooooo stringggg. Replaceaceaceace repeatedededed groupssss of symbolssss"
    result = pretty_message(data)
    print(result)
