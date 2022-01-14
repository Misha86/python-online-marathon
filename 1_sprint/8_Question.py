"""8 question 1 sprint"""


def studying_hours(a: list) -> int:
    """
    Length of the maximum non-decreasing contiguous subarray
    :param a: list
    :return: int
    """
    j = 0
    count_list = []
    for i in a:
        count = 0
        max_i = 0
        for q in a[j:]:
            if q >= max_i:
                max_i = q
                count += 1
            else:
                break
        j += 1
        count_list.append(count)
    return max(count_list)


if __name__ == '__main__':
    a = [2, 2, 1, 3, 4, 5, 5]
    res = studying_hours(a)
    print(res)
