from student import Student
from database import Database
from tabulate import tabulate
from utils import get_integer, get_float

db = Database()


while True:

    print("\n======================================")
    print(" SMART STUDENT MANAGEMENT SYSTEM")
    print("======================================")
    print("1. Add Student")
    print("2. View Students")
    print("3. Search Student")
    print("4. Update Student")
    print("5. Delete Student")
    print("6. Generate Report")
    print("7. Exit")

    choice = input("\nEnter your choice: ")

    if choice == "1":

        roll = get_integer("Enter Roll Number: ")
        name = input("Enter Student Name: ")
        age = get_integer("Enter Age: ")
        course = input("Enter Course: ")
        marks = get_float("Enter Marks: ")

        student = Student(roll, name, age, course, marks)

        db.add_student(student)
    elif choice == "2":

        students = db.view_students()

        if len(students) == 0:
            print("\nNo students found.")

        else:

            print("\n===== STUDENT RECORDS =====\n")

            headers = ["Roll", "Name", "Age", "Course", "Marks"]

            table = []

            for student in students:

                table.append(
                    [
                        student["roll"],
                        student["name"],
                        student["age"],
                        student["course"],
                        student["marks"],
                    ]
                )

            print(tabulate(table, headers=headers, tablefmt="grid"))

            input("\nPress Enter to return to the menu...")

    elif choice == "3":

        roll = get_integer("Enter Roll Number to Search: ")

        student = db.search_student(roll)

        if student:

            print("\n===== STUDENT FOUND =====")

            print(f"Roll Number : {student['roll']}")
            print(f"Name        : {student['name']}")
            print(f"Age         : {student['age']}")
            print(f"Course      : {student['course']}")
            print(f"Marks       : {student['marks']}")

        else:

            print("\nStudent not found.")

        input("\nPress Enter to return to the menu...")

    elif choice == "4":

        roll = get_integer("Enter Roll Number to Update: ")

        student = db.search_student(roll)

        if student:

            print("\n===== CURRENT DETAILS =====")

            print(f"Name   : {student['name']}")
            print(f"Age    : {student['age']}")
            print(f"Course : {student['course']}")
            print(f"Marks  : {student['marks']}")

            print("\nEnter New Details")

            name = input("Enter New Name: ")

            age = get_integer("Enter New Age: ")

            course = input("Enter New Course: ")

            marks = get_float("Enter New Marks: ")

            updated_data = {"name": name, "age": age, "course": course, "marks": marks}

            result = db.update_student(roll, updated_data)

            if result:

                print("\nStudent updated successfully!")

            else:

                print("\nUpdate failed.")

        else:

            print("\nStudent not found.")

        input("\nPress Enter to return to menu...")

    elif choice == "5":

        roll = get_integer("Enter Roll Number to Delete: ")

        student = db.search_student(roll)

        if student:

            print("\n===== STUDENT DETAILS =====")

            print(f"Roll Number : {student['roll']}")
            print(f"Name        : {student['name']}")
            print(f"Course      : {student['course']}")
            print(f"Marks       : {student['marks']}")

            confirm = input("\nAre you sure you want to delete? (yes/no): ")

            if confirm.lower() == "yes":

                result = db.delete_student(roll)

                if result:

                    print("\nStudent deleted successfully!")

            else:

                print("\nDelete cancelled.")

        else:

            print("\nStudent not found.")

        input("\nPress Enter to return to menu...")

    elif choice == "6":

        report = db.generate_report()

        if report:

            print("\n========== STUDENT REPORT ==========")

            print(f"\nTotal Students : {report['total_students']}")

            print(f"Average Marks  : {report['average_marks']:.2f}")

            print("\n===== TOPPER =====")

            print(f"Name  : {report['topper']['name']}")

            print(f"Marks : {report['topper']['marks']}")

            print("\n===== LOWEST MARKS =====")

            print(f"Name  : {report['lowest']['name']}")

            print(f"Marks : {report['lowest']['marks']}")

            print("\n===== COURSE COUNT =====")

            for course, count in report["course_count"].items():

                print(f"{course} : {count}")

        else:

            print("\nNo student data available.")

        input("\nPress Enter to return to menu...")

    elif choice == "7":

        print("\nThank you for using Smart Student Management System!")
        break

    else:

        print("\nThis feature will be added in the next steps.")
