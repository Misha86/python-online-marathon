"""4 question 4 sprint"""


class Testpaper:
    """
    Class Testpaper for Student
    """

    def __init__(self, subject: str, markscheme: list, pass_mark: str):
        self.subject = subject
        self.markscheme = markscheme
        self.pass_mark = pass_mark


class Student:
    """
    Class Student check tests
    """

    def __init__(self):
        self._tests_taken = {}
        self._test_check = {}

    @property
    def tests_taken(self):
        if not self._test_check:
            return 'No tests taken'
        else:
            self.__check_test()
            return self._tests_taken

    def take_test(self, test_paper, check_list):
        self._test_check[test_paper] = check_list

    def __check_test(self):
        for test_paper, check_list in self._test_check.items():
            count_true = len(list(filter(lambda x: x is True,
                                         list(map(lambda x, y: x == y, test_paper.markscheme, check_list)))))
            true_degree = round(count_true / len(test_paper.markscheme) * 100)
            if int(test_paper.pass_mark.rstrip('%')) > true_degree:
                self._tests_taken.update({test_paper.subject: f"Failed! ({true_degree}%)"})
            else:
                self._tests_taken.update({test_paper.subject: f"Passed! ({true_degree}%)"})


if __name__ == '__main__':
    paper1 = Testpaper("Maths", ["1A", "2C", "3D", "4A", "5A"], "60%")
    paper2 = Testpaper("Chemistry", ["1C", "2C", "3D", "4A"], "75%")
    paper3 = Testpaper("Computing", ["1D", "2C", "3C", "4B", "5D", "6C", "7A"], "75%")

    student1 = Student()
    student2 = Student()
    print(student1.tests_taken)  # No tests taken
    student1.take_test(paper1, ["1A", "2D", "3D", "4A", "5A"])
    print(student1.tests_taken)  # { "Maths": "Passed! (80%)"}

    student2.take_test(paper2, ["1C", "2D", "3A", "4C"])
    student2.take_test(paper3, ["1A", "2C", "3A", "4C", "5D", "6C", "7B"])
    print(student2.tests_taken)  # {"Chemistry": "Failed! (25%)", "Computing": "Failed! (43%)"}
