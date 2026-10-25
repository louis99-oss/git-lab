class Student:
    def __init__(self, name, marks):
        self.name = name
        self.marks = marks

    def __str__(self):
        return f"Student {self.name}, oceny: {self.marks}"

    def is_passed(self):
        total_marks = sum(self.marks)
        average_marks = total_marks / len(self.marks)
        return average_marks > 50


if __name__ == "__main__":
    student1 = Student("John", [60, 70, 80])
    student2 = Student("Alice", [40, 50, 60])
    print(student1.is_passed())  # Output: True
    print(student2.is_passed())  # Output: False
