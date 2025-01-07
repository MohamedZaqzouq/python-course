class Student:
    def __init__(self, name, age, grades=None):
        self.name = name
        self.age = age
        self.grades = grades if grades is not None else []

    def display_info(self):
        print(f"Name: {self.name}, Age: {self.age}, Grades: {self.grades}")

    def calculate_average_grade(self):
        if not self.grades:
            return 0
        return sum(self.grades) / len(self.grades)

class StudentDatabase:
    def __init__(self):
        self.students = []

    def add_student(self, student):
        self.students.append(student)

    def display_all_students(self):
        for student in self.students:
            student.display_info()

    def calculate_all_averages(self):
        for student in self.students:
            avg_grade = student.calculate_average_grade()
            print(f"{student.name}'s average grade: {avg_grade:.2f}")

# Example usage
if __name__ == "__main__":
    # Create a student database
    db = StudentDatabase()

    # Add students to the database
    student1 = Student("Alice", 20, [85, 90, 78])
    student2 = Student("Bob", 22, [88, 92, 80])
    student3 = Student("Charlie", 19, [90, 85, 95])

    db.add_student(student1)
    db.add_student(student2)
    db.add_student(student3)

    # Display all students
    print("All students:")
    db.display_all_students()

    # Calculate and display average grades for all students
    print("\nAverage grades:")
    db.calculate_all_averages()