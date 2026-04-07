students = []

def add_student():
    name = input("Enter Name: ")
    roll = input("Enter Roll No: ")
    course = input("Enter Course: ")

    students.append({"name": name, "roll": roll, "course": course})
    print("Student Added Successfully\n")


def view_students():
    if not students:
        print("No students found\n")
        return

    for s in students:
        print(s["roll"], "-", s["name"], "-", s["course"])
    print()


def search_student():
    roll = input("Enter Roll No to search: ")
    for s in students:
        if s["roll"] == roll:
            print("Found:", s)
            return
    print("Student not found\n")


def update_student():
    roll = input("Enter Roll No to update: ")
    for s in students:
        if s["roll"] == roll:
            s["name"] = input("New Name: ")
            s["course"] = input("New Course: ")
            print("Updated Successfully\n")
            return
    print("Student not found\n")


def delete_student():
    roll = input("Enter Roll No to delete: ")
    for s in students:
        if s["roll"] == roll:
            students.remove(s)
            print("Deleted Successfully\n")
            return
    print("Student not found\n")


while True:
    print("1.Add 2.View 3.Search 4.Update 5.Delete 6.Exit")
    choice = input("Enter choice: ")

    if choice == "1":
        add_student()
    elif choice == "2":
        view_students()
    elif choice == "3":
        search_student()
    elif choice == "4":
        update_student()
    elif choice == "5":
        delete_student()
    elif choice == "6":
        break
    else:
        print("Invalid choice\n")




