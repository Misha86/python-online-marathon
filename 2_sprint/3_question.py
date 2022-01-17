"""3 question 2 sprint"""
import re
import math


def figure_perimetr(s: str) -> float:
    """Find figure perimetr
    :param s: str
    :return: float
    """
    d = [(int(x[0]), int(x[1])) for x in re.findall(r'(\d):(\d)', s)]
    s1 = math.sqrt((d[0][0] - d[1][0])**2 + (d[0][1] - d[1][1])**2)
    s2 = math.sqrt((d[0][0] - d[2][0])**2 + (d[0][1] - d[2][1])**2)
    s3 = math.sqrt((d[2][0] - d[3][0])**2 + (d[2][1] - d[3][1])**2)
    s4 = math.sqrt((d[1][0] - d[3][0])**2 + (d[1][1] - d[3][1])**2)
    perimetr = s1 + s2 + s3 + s4

    return round(perimetr, 14)


if __name__ == '__main__':
    string = "#LB0:1#RB5:1#LT4:5#RT8:3"
    result = figure_perimetr(string)
    print(result)
