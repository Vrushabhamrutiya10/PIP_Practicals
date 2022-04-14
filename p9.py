
class Student:
    def __init__(self, r_no, name, div):
        self.r_no = r_no
        self.name = name
        self.div = div


class Exam(Student):
    def __init__(self, r_no, name, div):
        super().__init__(r_no, name, div)
        self.mark = []

    def marks(self):
        print(f"Enter marks for six subject of {self.name} (out of 100): ")
        for i in range(6):
            temp = int(input())
            self.mark.append(temp)


class Result(Exam):
    def __init__(self, r_no, name, div):
        super().__init__(r_no, name, div)
        self.total = 0

    def final_result(self):
        for i in range(6):
            self.total += self.mark[i]

        print(f"-----------------RESULT----------------"
              f"\nName: \t{self.name}\nRoll No: \t{self.r_no}\nDivision: \t{self.div}\nTotal Marks : \t{self.total}")


result = Result('20CS004','Vrushabh Amrutiya','CS-1')
result.marks()
result.final_result()
