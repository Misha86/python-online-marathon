"""3 question 3 sprint"""
import re
import collections


def create_account(user_name: str, password: str, secret_words: list):
    # match = re.match(r'^(?=.*[0-9].*)(?=.*[@#$*%^!&+=_].*)(?=.*[a-z].*)(?=.*[A-Z].*)[0-9a-zA-Z@#*$%^!&+=_]{6,}$',
    #                  password)
    match = re.match(r'^(?=.*[0-9])(?=.*[\W_])(?=.*[a-z])(?=.*[A-Z])[0-9a-zA-Z\W_]{6,}$',
                     password)
    if not match:
        raise ValueError

    def check(password_check: str, secret_words_check: list):
        if password == password_check and len(secret_words) == len(secret_words_check):
            secret_words_copy = secret_words[:]
            check_l = [secret_words_copy.remove(x) if x in secret_words_copy else False for x in secret_words_check]
            count_false = collections.Counter(check_l)[False]
            if count_false > 1:
                return False
            else:
                return True
            # m = 0
            # secret_words_copy = secret_words[:]
            # for c in secret_words_check:
            #     if c in secret_words_copy:
            #         secret_words_copy.remove(c)
            #     elif not m:
            #         m += 1
            #     else:
            #         return False
            # return True
        else:
            return False
    return check


if __name__ == '__main__':
    # val1 = create_account("123", "qQ1!45", ["1", "word"])
    # # check1 = val1("Qwerty1_", ["1", "word"])

    tom = create_account("Tom", "Qwerty1_", ["1", "word"])
    check1 = tom("Qwerty1_", ["1", "word"])
    check2 = tom("Qwerty1_", ["word"])
    check3 = tom("Qwerty1_", ["word", "2"])
    check4 = tom("Qwerty1!", ["word", "12"])
    print(f"Check1: {check1}")
    print(f"Check2: {check2}")
    print(f"Check3: {check3}")
    # print(f"Check4: {check4}")
    print('-'*50)
    tom2 = create_account("123", "qQ1!45", ['1', '2', '1'])
    check1 = tom2("qQ1!45", ['2', '2', '1'] )
    check2 = tom2("qQ1!45", ['1', 'word'])
    check3 = tom2("qQ1!45", ["word", "3"])
    print(f"Check1: {check1}")
    print(f"Check2: {check2}")
    print(f"Check3: {check3}")
