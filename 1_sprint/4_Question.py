"""4 question 1 sprint"""


def findPermutation(n, p, q):
    """
    Find a permutation
    :param n: int
    :param p: list
    :param q: list
    :return: list
    """
    r = [p.index(q[i]) + 1 for i in range(n)]
    return r


if __name__ == '__main__':
    n = 3
    p = [3, 1, 2]
    q = [2, 1, 3]
    res = findPermutation(n, p, q)
    print(res)


