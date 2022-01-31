"""4 question 6 sprint"""
import json
from json import JSONEncoder


import json
from json import JSONEncoder


class Student:
    def __init__(self, full_name: str, avg_rank: float, courses: list):
        self.full_name = full_name
        self.avg_rank = avg_rank
        self.courses = courses

    def __str__(self):
        return f"{self.full_name} ({self.avg_rank}): {self.courses}"

    @classmethod
    def from_json(cls, json_file):
        with open(json_file) as f:
            return cls(**json.load(f))


class Group:
    def __init__(self, title: str, students: list):
        self.title = title
        self.students = students

    def __str__(self):
        return f"{self.title}: {[s.__str__() for s in self.students]}"

    @staticmethod
    def serialize_to_json(list_of_groups, filename):
        with open(filename, 'w') as f:
            return json.dump(list_of_groups, f, default=lambda o: o.__dict__)

    @classmethod
    def create_group_from_file(cls, students_file):
        with open(students_file) as f:
            load_data = json.load(f)
            return cls(students_file.rstrip('.json'),
                       [Student(**i) for i in load_data] if isinstance(load_data, list) else [Student(**load_data)])


if __name__ == '__main__':
    g = Group.create_group_from_file("students.json")
    print(g.students)
    print(g.title)
