"""1 question 1 sprint"""


def kthTerm(n, k) -> int:
    """
    n1, n1+n0,
    n2, n2+n0, n2+n1, n2+n1+n0,
    n3, n3+n0, n3+n1, n3+n1+n0, n3+n2, n3+n2+n1, n3+n2+n1+n0]
    """
    res = []
    for i in range(k):
        if len(res) > k:
            break
        res_copy = list(res)
        res.append(n**i)
        for j in res_copy:
            res.append(j + n**i)
    return res[k-1]


if __name__ == '__main__':
    result = kthTerm(3, 4)
    print(result)
