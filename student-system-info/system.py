import uuid


class StudentSystem:
    def __init__(self):
        self.students = {}

    def add_student(
        self,
        name: str,
        age: int,
        grades: list[int],
        faculty: tuple[str, str] = ("Unknown", "Unknown"),
        uid: set[int] | None = None,
    ):
        if uid is None:
            uid_value = uuid.uuid4().int
            uid = {uid_value}

        self.students[name] = {
            "name": name,
            "age": age,
            "grades": grades,
            "faculty": faculty,
            "uid": uid,
        }

    def average_grade(self, name: str) -> float:
        grades = self.students[name]["grades"]
        if not grades:
            return 0.0
        return sum(grades) / len(grades)

    def modify_grades(self, name: str, new_grades: list[int]):
        self.students[name]["grades"] = new_grades

    def modify_faculty(self, name: str, new_faculty: tuple[str, str]):
        # тут будет работать только если заменить весь кортеж
        self.students[name]["faculty"] = new_faculty

    def delete_student(self, name: str):
        del self.students[name]


def print_student_info(*, name: str, students: dict[str, dict]):
    """Выводит информацию о студенте по имени"""
    student = students.get(name)
    if student is None:
        print(f"Student '{name}' not found")
        return

    uid_value = next(iter(student["uid"]))
    university, faculty = student["faculty"]

    print(f"Name: {student['name']}")
    print(f"Age: {student['age']}")
    print(f"Grades: {student['grades']}")
    print(f"Faculty: {university} / {faculty}")
    print(f"UID: {uid_value}")


student_system = StudentSystem()

student_system.add_student(
    "John",
    20,
    [85, 90, 95],
    ("University of California", "Computer Science"),
)

# Вызов по условию (именованные аргументы):
print_student_info(name="John", students=student_system.students)