"""5 question 3 sprint"""


def logger(f):
    def inner(*args, **kwargs):
        args_kwargs = ", ".join(list(map(str, args)) + list(map(str, kwargs.values())))
        res = f(*args, **kwargs)
        print(f'Executing of function {f.__name__} with arguments {args_kwargs}...')
        return res
    return inner


@logger
def print_arg(arg):
    print(arg)


@logger
def concat(*args, **kwargs):
    count = ''
    ar_kw = list(map(str, args)) + list(map(str, kwargs.values()))
    for ak in ar_kw:
        count += ak
    return count


if __name__ == '__main__':
    print(print_arg(2))
    print(concat(1))
    print(concat('first string', second=2, third='second string'))
    print(concat('first string', {'first kwarg': 0, 'second kwarg': 'second kwarg'}))

