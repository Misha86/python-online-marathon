"""1 question 3 sprint"""


def outer(name):
    def inner():
        print(f"Hello, {name}!")
    return inner


if __name__ == '__main__':
    olha = outer("Olha")
    olha()
