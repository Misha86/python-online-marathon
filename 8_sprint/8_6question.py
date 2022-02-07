"""6 question 8 sprint"""
import unittest
from unittest.mock import Mock


def file_parser(file_path, find_str: str, replace_str: str = None) -> str:
    with open(file_path, 'r') as f:
        data = f.read()
        count = data.count(find_str)
        if replace_str:
            data = data.replace(find_str, replace_str)
            f.seek(0)
            f.truncate()
            f.write(data)
            return f"Replaced {count} strings"
        return f"Found {count} strings"


class ParserTest(unittest.TestCase):
    pass


if __name__ == '__main__':
    print(file_parser("grades.json", "subject_id"))
    # unittest.main()


