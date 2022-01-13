"""1 question 1 sprint"""


def kthTerm(n, k) -> int:
    """
    [3**0] = > [1]
    [1,        3**1, 3**1 + 1] = > [1, 3, 4]
    [1, 3, 4,  3**2, 3**2 + 1, 3**2 + 3, 3**2 + 4] = > [1, 3, 4, 9, 10, 12, 13]
    """
    res = []
    for i in range(k):
        if len(res) > k:
            break
        for j in range(len(res) + 1):
            if j == 0:
                lis = n ** i
            else:
                lis = n ** i + res[j-1]
            res.append(lis)
    return res[k-1]


if __name__ == '__main__':
    result = kthTerm(3, 4)
    print(result)
