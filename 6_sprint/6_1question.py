"""1 question 6 sprint"""
import json
from json import JSONDecoder


class PasswordDecoderFind2(JSONDecoder):
    def __init__(self, key, values_set):
        super().__init__(object_hook=self.dict_to_object)
        self.key = key
        self.got_values = values_set

    def dict_to_object(self, dictionary):
        if self.key in dictionary:
            value = dictionary[self.key]
            self.got_values.update(value) if isinstance(value, list) else self.got_values.add(value)


def find2(file, key):
    with open(file, 'r') as f:
        passwords_set = set()
        json.load(f, object_hook=PasswordDecoderFind2(key, passwords_set).dict_to_object)
        return list(passwords_set)


def find(file, key):
    passwords_set = set()
    with open(file, 'r') as f:
        def get_password(dct):
            if key in dct:
                value = dct.get(key)
                passwords_set.update(value) if isinstance(value, list) else passwords_set.add(value)
        json.load(f, object_hook=get_password)
        return list(passwords_set)


if __name__ == '__main__':
    print(find("1.json", "password"))  # returns["pass_1", "qwerty"]
    print(find("2.json", "password"))  # returns["1234qweQWE", "pass_1", "qwerty"]
    print(find("3.json", "password"))  # returns["1234qweQWE"]
