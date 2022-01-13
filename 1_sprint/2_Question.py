"""2 question 1 sprint"""


def filterBible(scripture, book, chapter) -> list:
    """
    Filter verses from Bible
    :param scripture: list
    :param book: str
    :param chapter: str
    :return: list
    """
    verses = [verse for verse in scripture if verse.startswith(book + chapter)]

    return verses


if __name__ == '__main__':
    scrip = ["01001001", "01001002", "01002001", "01002002", "01002003", "02001001", "02001002", "02001003"]
    b = "01"
    chap = "001"
    result = filterBible(scrip, b, chap)
    print(result)
