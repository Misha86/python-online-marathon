"""6 question 8 sprint"""
import unittest
from unittest.mock import patch, mock_open


def file_parser(file_path, find_str: str, replace_str: str = None) -> str:
    with open(file_path, 'r+') as f:
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

    str_f = "These are short, famous texts in English from classic sources like the Bible " \
            "or Shakespeare. Some texts have word definitions and explanations to help you."

    def setUp(self):
        self.file_parser = file_parser
        self.search_string = "texts"

    def test_count_string(self):
        with patch('builtins.open', mock_open(read_data=self.str_f)) as file:
            result = self.file_parser(file, self.search_string)
            self.assertEqual(result, "Found 2 strings")
            file.assert_called_once()

    def test_replace_string(self):
        with patch('builtins.open', mock_open(read_data=self.str_f)) as file:
            result = self.file_parser(file, self.search_string, "No data")
            self.assertEqual(result, "Replaced 2 strings")
            file.assert_called_once()

    @unittest.expectedFailure
    def test_file_exist(self):
        self.file_parser("not_exist_file.txt", "string")

    @patch("__main__.file_parser", return_value=f"Found 3 strings")
    def test_file_parser(self, parser_mock):
        self.file_parser = parser_mock
        self.assertEqual(self.file_parser("file.txt", "string"), "Found 3 strings")
        self.file_parser.assert_called_once_with("file.txt", "string")


if __name__ == '__main__':
    print(file_parser("grades.json", "subject_id"))
    # unittest.main(verbosity=2)


