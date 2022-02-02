"""4 question 6 sprint"""
import json


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
        return f"{self.title}: {list(map(str, self.students))}"

    @staticmethod
    def serialize_to_json(list_of_groups, filename):
        with open(filename, 'w') as f:
            return json.dump(list_of_groups, f, default=lambda o: o.__dict__)

    @classmethod
    def create_group_from_file(cls, students_file):
        with open(students_file) as f:
            students = json.load(f, object_hook=lambda dct: Student(**dct))
            return cls(students_file.rstrip('.json'), students if isinstance(students, list) else [students])


if __name__ == '__main__':
    g1 = Group.create_group_from_file("2020_2.json")
    print(g1)
    g2 = Group.create_group_from_file("2020-01.json")
    print(g2)
    Group.serialize_to_json([g1, g2], "g1.json")
    f1 = open("g1.json")
    d = json.load(f1)
    s = [{"title": "2020_2", "students": [{"full_name": "Student 1 from second Group", "avg_rank": 98, "courses": ["Python"]}, {"full_name": "Student 2 from second Group", "avg_rank": 70.34, "courses": ["Ruby", "Python", "Frontend development"]}]}, {"title": "2020-01", "students": [{"full_name": "Student2 from group2", "avg_rank": 50.4, "courses": ["C++"]}]}]
    print(d == s)
    print(d)
    f1.close()
