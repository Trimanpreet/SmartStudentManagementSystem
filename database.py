import json
import os
from student import Student


class Database:

    def __init__(self):
        self.filename = "students.json"

    def load_students(self):

        if not os.path.exists(self.filename):
            return []

        with open(self.filename, "r") as file:
            data = json.load(file)

        return data

    def save_students(self, students):

        with open(self.filename, "w") as file:
            json.dump(students, file, indent=4)

    def add_student(self, student):

        students = self.load_students()

        print(students)  # <-- Add this line temporarily

        for existing_student in students:

            if existing_student["roll"] == student.roll:

                print("\nStudent with this roll number already exists!")
                return False

        students.append(student.to_dict())

        self.save_students(students)

        print("\nStudent added successfully!")

        return True

    def view_students(self):

        students = self.load_students()

        return students

    def search_student(self, roll):

        students = self.load_students()

        for student in students:

            if student["roll"] == roll:
                return student

        return None

    def update_student(self, roll, updated_data):

        students = self.load_students()

        for student in students:

            if student["roll"] == roll:

                student["name"] = updated_data["name"]
                student["age"] = updated_data["age"]
                student["course"] = updated_data["course"]
                student["marks"] = updated_data["marks"]

                self.save_students(students)

                return True

        return False

    def delete_student(self, roll):

        students = self.load_students()

        for student in students:

            if student["roll"] == roll:

                students.remove(student)

                self.save_students(students)

                return True

        return False

    def generate_report(self):

        students = self.load_students()

        if len(students) == 0:
            return None

        total_students = len(students)

        total_marks = 0

        for student in students:
            total_marks += student["marks"]

        average_marks = total_marks / total_students

        topper = max(students, key=lambda x: x["marks"])

        lowest = min(students, key=lambda x: x["marks"])

        course_count = {}

        for student in students:

            course = student["course"]

            if course in course_count:

                course_count[course] += 1

            else:

                course_count[course] = 1

        report = {
            "total_students": total_students,
            "average_marks": average_marks,
            "topper": topper,
            "lowest": lowest,
            "course_count": course_count,
        }

        return report
