"""Bonus task 8 sprint"""
import json
import string
import random
from enum import Enum
from typing import List
import re
import uuid


class Role(Enum):
    Mentor = 0
    Trainee = 1


class Subject:
    subjects = []

    def __init__(self, title, id=None):
        self.title = title
        self.id = self._set_id(id)
        self.subjects.append(self)

    @classmethod
    def create_subject(cls, title, id):
        return cls(title, id)

    def _set_id(self, id):
        if self.subjects:
            exist_id = [subject.id for subject in self.subjects if id == subject.id]
            if not exist_id:
                new_id = ''.join([random.choice(string.ascii_lowercase + string.digits) for n in range(32)])
                return new_id
        return id


class Score:
    A = "A"
    B = "B"
    C = "C"
    D = "D"

    def __init__(self, score, user_id=None, subject_id=None):
        self.score = score
        self.user_id = user_id
        self.subject_id = subject_id


class User:
    users = []

    def __init__(self, username, password, role, id=None):
        self.username = username
        self.password = password
        self.role = role
        self.id = self._set_id(id)
        self.score_list = []
        self.users.append(self)
        self.validate_password(self.password)

    def __str__(self):
        return f"{self.username} with role {self.role}: {self.score_list}"

    @classmethod
    def create_user(cls, username, password, role, id=None):
        return cls(username, password, role, id)

    def _set_id(self, id):
        exist_id = [subject.id for subject in self.users if id == subject.id]
        if id is None and not exist_id:
            return uuid.UUID(uuid.uuid4().hex)
        else:
            return uuid.UUID(id)

    def add_score_for_subject(self, subject: Subject, score: Score):
        self.score_list.append({subject.title: score})
        return self.score_list

    @classmethod
    def validate_password(cls, password):
        match = re.match(r'^(?=.*[0-9])(?=.*[\W_])(?=.*[a-z])(?=.*[A-Z])[0-9a-zA-Z\W_]{6,}$',
                         password)
        if match:
            return password
        else:
            raise PasswordValidationException("Invalid password")


class NonUniqueException(Exception):
    def __init__(self, massage):
        self.massage = massage

    def __str__(self):
        return self.massage


class PasswordValidationException(Exception):
    def __init__(self, massage):
        self.massage = massage

    def __str__(self):
        return self.massage


class ForbiddenException(Exception):
    pass


def get_subjects_from_json(subjects_json):
    with open(subjects_json) as s_file:
        subjects = json.load(s_file, object_hook=lambda dct: Subject.create_subject(**dct))
        return subjects


def get_users_with_grades(users_json, subjects_json, grades_json):
    def get_user(dct):
        user = User.create_user(**dct)
        return user

    def get_users_grades(dct):
        for user in users:
            if dct["user_id"] == user.id.hex:
                for subject in subjects:
                    if dct["subject_id"] == subject["id"]:
                        user.add_score_for_subject(Subject(**subject), dct['score'])
            else:
                return dct
    with open(users_json) as u_file, open(subjects_json) as s_file, open(grades_json) as g_file:
        users = json.load(u_file, object_hook=get_user)
        subjects = json.load(s_file)
        json.load(g_file, object_hook=get_users_grades)
        return users


def add_user(user: User, users: List[User]):
    username_exist = [u.username for u in users if u.username == user.username]
    if not username_exist:
        users.append(user)
    else:
        raise NonUniqueException(f"User with name {user.username} already exists")


def add_subject(subject, subjects):
    subject_exist = [s.title for s in subjects if s.title == subject.title]
    if not subject_exist:
        subjects.append(subject)
    else:
        raise NonUniqueException(f"Subject with name {subject.title} already exists")


def check_if_user_present(username, password, users: List[User]):
    username_exist = (True for u in users if u.username == username and u.password == password)
    return next(username_exist, False)


def get_grades_for_user(username: str, user: User, users: List[User]):
    user_exist = [usr for usr in users if usr.username == username and
                  (username == user.username or user.username == "Mentor")]
    if user_exist:
        return user_exist[0].score_list
    raise ForbiddenException


class UserEncoder(json.JSONEncoder):
    def default(self, user):
        user.id = user.id.hex
        dct = user.__dict__
        if 'role' in dct and isinstance(user.role, Enum):
            user.role = user.role.value
        updated_user = {key: value for key, value in dct.items() if key != "score_list"}
        return updated_user


def users_to_json(users, json_file):
    with open(json_file, "w") as f:
        json.dump(users, f, cls=UserEncoder, indent=4)


def subjects_to_json(subjects, json_file):
    with open(json_file, "w") as f:
        json.dump(subjects, f, default=lambda o: o.__dict__, indent=4)


def grades_to_json(users, subjects, json_file):
    scores_ = []
    for user in users:
        if isinstance(user, User) and user.score_list:
            for sc in user.score_list:
                score_data = list(sc.items())
                get_subject_id = (s.id for s in subjects if s.title == score_data[0][0])
                subject_id = next(get_subject_id, None)
                if subject_id:
                    scores_.append(Score(score_data[0][1], user.id.hex, subject_id))

    with open(json_file, "w") as f:
        json.dump(scores_, f, default=lambda o: o.__dict__, indent=4)


if __name__ == '__main__':
    users = get_users_with_grades("users.json", "subjects.json", "grades.json")
    mentor = User.create_user("Mentor", "!1qQ456", Role.Mentor)
    add_user(mentor, users)
    print(get_grades_for_user("Mentor", users[1], users))