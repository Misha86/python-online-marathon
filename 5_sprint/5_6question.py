"""5 question 5 sprint"""
import re


def valid_email(email):
    try:
        match = re.fullmatch(r"[a-z]+@[a-z.]+", email)
        if match:
            return "Email is valid"
        else:
            return "Email is not valid"
    except Exception as e:
        return e


if __name__ == '__main__':
    print(valid_email("trafik@ukr.tel.com"))  # output:   "Email is valid"
    print(valid_email("trafik@ukr_tel.com"))  # output:   "Email is not valid"
    print(valid_email("tra@fik@ukr.com"))  # output:   "Email is not valid"
    print(valid_email("ownsite@our.c0m"))  # output:   "Email is not valid"
    print(valid_email(1111))  # output:   "Email is not valid"

