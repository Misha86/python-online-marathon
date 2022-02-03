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


def double_string_mentor(data: list) -> int:
    double = [i+j for i in data for j in data]
    count = 0
    for i in data:
        if i in double:
            count += 1
    return count


if __name__ == '__main__':
    data = ['aa', 'aa', 'aaaa', 'aaaaaaaa', 'aaaa', 'qwer']
    result = double_string(data)
    print(result)

    data_m = ['aa', 'aa', 'aaaa', 'aaaaaaaa', 'aaaa', 'qwer']
    result_m = double_string_mentor(data_m)
    print(result_m)

