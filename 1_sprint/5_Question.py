"""5 question 1 sprint"""


def toPostFixExpression(e: list) -> list:
    """
    Convert expression to expression in a postfix notation.
    :param e: list
    :return: list
    """
    prec = {}
    prec["*"] = 3
    prec["/"] = 3
    prec["+"] = 2
    prec["-"] = 2
    prec["("] = 1
    opStack = []
    postfixList = []

    for token in e:
        if token.isalnum():
            postfixList.append(token)
        elif token == '(':
            opStack.append(token)
        elif token == ')':
            topToken = opStack.pop()

            while topToken != '(' and opStack:
                postfixList.append(topToken)
                topToken = opStack.pop()
        else:

            while opStack and (prec[opStack[-1]] >= prec[token]):
                  postfixList.append(opStack.pop())
            opStack.append(token)

    while opStack:
        postfixList.append(opStack.pop())
    return postfixList


if __name__ == '__main__':
    expression = ["(", "(", "(", "1", "+", "2", ")", "*", "3", ")", "+", "6", ")", "/", "(", "2", "+", "3", ")"]
    res = toPostFixExpression(expression)
    print(res)
