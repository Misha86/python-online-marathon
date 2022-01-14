"""5 question 1 sprint"""
"""For expression = ["2","+","3"] the output should be ["2","3","+"]"""

def toPostFixExpression(e):
    """
    Convert expression in a postfix notation.
    :param e: list
    :return: list
    """
    output = []
    for i in e:
        if i.isalnum():
            output.append(i)
            continue
        else:
            output.append(i)


    return output


if __name__ == '__main__':
    expression = ["2", "+", "3"]
    res = toPostFixExpression(expression)
    print(res)


