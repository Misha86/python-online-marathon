"""1 question 2 sprint"""


def double_string(d: list) -> int:
    """Concatenate of two strings from this arguments  list
    :param d: list
    :return: int
    """
    total_count = 0
    for s in d:
        if s*2 in d:
            total_count += 1
        else:
            for j in set(d):
                total_count += True if (s + j) in d else False
    return total_count


if __name__ == '__main__':
    data = ['aa', 'aaaa', 'aaaaaaaa', 'aaaa', 'qwer', 'qweraaaa']
    result = double_string(data)
    print(result)
