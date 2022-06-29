class Student:
    name: str = None

    def __init__(self, name: str):
        self.name = name

    def __str__(self):
        return "Студент: " + self.name

    __repr__ = __str__


students = [Student(f"Студент_{i}") for i in range(20)]
print(students)