"""6 question 3 sprint"""
from random import choice


def randomWord(data: list) -> str:
    if not data:
        while True:
            yield None
    data_copy = data[:]
    while True:
        item = choice(data_copy)
        data_copy.remove(item)
        yield item
        if not data_copy:
            data_copy += data[:]


if __name__ == '__main__':
    data = ['book', 'apple', 'word']
    books = randomWord(data)
    print(next(books))
    print(next(books))
    print(next(books))
    print(next(books))

    no_data = []
    empty = randomWord(no_data)
    print(next(empty))
    print(next(empty))
    print(next(empty))
    print(next(empty))
