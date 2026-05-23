class Student:
    def __init__(self, student_id, name, marks):
        self.student_id = student_id
        self.name = name
        self.marks = marks

    def display(self):
        print(f"ID: {self.student_id}")
        print(f"Name: {self.name}")
        print(f"Marks: {self.marks}")


students = []


def add_student():
    student_id = input("Enter Student ID: ")
    name = input("Enter Name: ")
    marks = input("Enter Marks: ")

    student = Student(student_id, name, marks)
    students.append(student)

    with open("students.txt", "a") as file:
        file.write(f"{student_id},{name},{marks}\n")

    print("Student Added Successfully")


def view_students():
    print("\nStudent Records\n")

    try:
        with open("students.txt", "r") as file:
            data = file.readlines()

            if not data:
                print("No records found")
                return

            for line in data:
                student_id, name, marks = line.strip().split(",")
                print(f"ID: {student_id}")
                print(f"Name: {name}")
                print(f"Marks: {marks}")
                print("-------------------")

    except FileNotFoundError:
        print("No student records found")


while True:
    print("\n1. Add Student")
    print("2. View Students")
    print("3. Exit")

    choice = input("Enter choice: ")

    if choice == "1":
        add_student()

    elif choice == "2":
        view_students()

    elif choice == "3":
        print("Exiting...")
        break

    else:
        print("Invalid Choice")