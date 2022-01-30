"""1 question 6 sprint"""
import json


def find(file, key):
    with open(file, 'r') as f:
        passwords_set = set()

        def get_password(dct):
            if key in dct:
                d = dct.get(key)
                if isinstance(d, list):
                    passwords_set.update(d)
                else:
                    passwords_set.add(d)
        load_f = json.load(f, object_hook=get_password)
        return list(passwords_set)


if __name__ == '__main__':
    print(find("1.json", "password"))  # returns["pass_1", "qwerty"]
    print(find("2.json", "password"))  # returns["1234qweQWE", "pass_1", "qwerty"]
    print(find("3.json", "password"))  # returns["1234qweQWE"]
