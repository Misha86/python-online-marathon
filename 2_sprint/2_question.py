"""2 question 2 sprint"""


def morse_number(num: str) -> str:
    """Encrypt a number in a three-digit format in Morse code
    :param num:
    :return:
    """
    tr = ''.strip()
    for n in num:
        i = int(n)
        if n in '12345':
            tr += f"{'.' * i}{'-' * (5 - i)} "
        elif n in '6789':
            tr += f"{'-' * (i - 5)}{'.' * (10 - i)} "
        else:
            tr += '----- '
    return tr


if __name__ == '__main__':
    data = '780'
    result = morse_number(data)
    print(result)
