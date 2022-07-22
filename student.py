"""
creating a list of students with grades
and making a decision on admission to the university
"""


def add_students():
    name = input("Enter name: ")
    while True:
        try:
            grade = int(input("Enter grade: "))
            return name, grade
        except ValueError:
            print("you didn't enter a number")
            continue


def sort_students(students):
    good_grade = "entered the University:"
    bad_grade = "didn't go to university:"
    for name, grade in students.items():
        if grade >= 4:
            good_grade += f'\n{name} - {grade}'
        elif grade <= 3:
            bad_grade += f'\n{name} - {grade}'
    print(good_grade)
    print(bad_grade)


def main():
    students = {}
    while True:
        command = input("1 - Add\n2 - View\nEnter the command: ")
        if command == '1':
            name, grade = add_students()
            students[name] = grade

        elif command == '2':
            sort_students(students)


if __name__ == "__main__":
    main()
