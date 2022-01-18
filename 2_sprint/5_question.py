"""5 question 2 sprint"""
import re


def max_population(data: list) -> tuple:
    """Get info about location with the highest population
    :param data: list
    :return: tuple
    """
    regex_com = re.compile(r'\d+\W(?P<city>\w+)\W(?P<popul>\d+)\W\w')
    match = sorted([(i, int(j)) for i, j in regex_com.findall("".join(data))],
                   key=lambda x: x[1], reverse=True)
    return match[0]


if __name__ == '__main__':
    data = ["id,name,poppulation,is_capital",
            "3024,eu_kyiv,24834,y",
            "3025,eu_volynia,20231,n",
            "3026,eu_galych,23745,n",
            "4892,me_medina,18038,n",
            "4401,af_cairo,18946,y",
            "4700,me_tabriz,13421,n",
            "4899,me_bagdad,22723,y",
            "6600,af_zulu,09720,n"]
    result = max_population(data)
    print(result)
