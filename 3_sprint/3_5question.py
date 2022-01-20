"""5 question 3 sprint"""


def logger(f):
    def inner(*args, **kwargs):
        args_value = [str(i) for i in args]
        kwargs_values = [str(k) for k in kwargs.values()]
        res = f(*args, **kwargs)
        print(f'Executing of function {f.__name__} with arguments {", ".join(args_value+kwargs_values)}...')
        return res
    return inner


@logger
def print_arg(arg):
    print(arg)


@logger
def concat(*args, **kwargs):
    count = ''
    kw = kwargs.values()
    if len(args) == 1:
        count += str(args[0])
    else:
        for a in args:
            count += str(a)
    if len(kw) == 1:
        count += str(kw[0])
    else:
        for k in kw:
            count += str(k)
    return count


if __name__ == '__main__':
    print(print_arg(2))
    print(concat(1))
    print(concat('first string', second=2, third='second string'))
    print(concat('first string', {'first kwarg': 0, 'second kwarg': 'second kwarg'}))

