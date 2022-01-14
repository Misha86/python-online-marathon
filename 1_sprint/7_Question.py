"""7 question 1 sprint"""


def Cipher_Zeroes(N: str):
    """
    Find visible zero
    :param N: str
    :return: int
    """
    points = 0
    if 1 <= len(N) <= pow(10, 3) and N.isalnum():
        for s in N:
            if s in '069':
                points += 1
            if s == '8':
                points += 2
    if points:
        if points % 2:
            points += 1
        else:
            points -= 1
    # points_bin = int(bin(points).partition('b')[-1])
    # return points_bin
    return int(format(points, 'b'))


if __name__ == '__main__':
    N = "4900"
    res = Cipher_Zeroes(N)
    print(res)


