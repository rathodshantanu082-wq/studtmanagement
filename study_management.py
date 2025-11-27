students = [] 
FILENAME = "students.txt"  

def load_students():
    """Read students from file when program starts"""
    global students
    try:
        with open(FILENAME, "r") as file:
            for line in file:
                parts = line.strip().split(",")
                if len(parts) == 4:
                    students.append({
                        "name": parts[0],
                        "rollno": parts[1],
                        "branch": parts[2],
                        "marks": float(parts[3])
                    })
        print(f"Loaded {len(students)} students from file")
    except FileNotFoundError:
        print("New file created")

def save_students():
    """Save all students to file"""
    with open(FILENAME, "w") as file:
        for student in students:
            file.write(f"{student['name']},{student['rollno']},{student['branch']},{student['marks']}\n")
    print("Data saved to file")

def add_student():
    """Add new student"""
    name = input("Enter name: ")
    rollno = input("Enter roll no: ")
    
    
    for student in students:
        if student["rollno"] == rollno:
            print("Roll no already exists!")
            return
    
    branch = input("Enter branch: ")
    marks = float(input("Enter marks: "))
    
    students.append({
        "name": name,
        "rollno": rollno,
        "branch": branch,
        "marks": marks
    })
    print("Student added!")

def show_all():
    """Show all students in table"""
    if not students:
        print("No students yet!")
        return
    
    print("\n ALL STUDENTS")
    print("ID | Name       | Roll | Branch  | Marks")
    print("-" * 40)
    for i, student in enumerate(students, 1):
        print(f"{i:<2} | {student['name']:<9} | {student['rollno']:<4} | {student['branch']:<7} | {student['marks']:.1f}")
    print("-" * 40)

def search_student():
    """Search by name or roll no"""
    search = input("Enter name or roll no: ").lower()
    found = []
    
    for student in students:
        if search in student["name"].lower() or search in student["rollno"].lower():
            found.append(student)
    
    if not found:
        print("❌ Not found!")
        return
    
    print(f"\n Found {len(found)} students:")
    print("Name      | Roll | Marks")
    print("-" * 25)
    for student in found:
        print(f"{student['name']:<9} | {student['rollno']:<4} | {student['marks']:.1f}")

def update_marks():
    """Update marks of a student"""
    rollno = input("Enter roll no: ")
    for student in students:
        if student["rollno"] == rollno:
            new_marks = float(input("Enter new marks: "))
            student["marks"] = new_marks
            print("Marks updated!")
            return
    print("Student not found!")

def delete_student():
    """Delete student"""
    rollno = input("Enter roll no to delete: ")
    for i, student in enumerate(students):
        if student["rollno"] == rollno:
            print(f"Deleting {student['name']}...")
            students.pop(i)
            print("Deleted!")
            return
    print("Not found!")

def show_stats():
    """Simple class stats"""
    if not students:
        print("No students!")
        return
    
    total = len(students)
    avg_marks = sum(student["marks"] for student in students) / total
    max_marks = max(student["marks"] for student in students)
    
    print(f"\n CLASS STATS")
    print(f"Total students: {total}")
    print(f"Average marks: {avg_marks:.1f}")
    print(f"Top marks: {max_marks:.1f}")

# MAIN PROGRAM STARTS HERE
print("SIMPLE STUDENT MANAGEMENT")
load_students()

while True:
    print("\n1. Add Student")
    print("2. Show All")
    print("3. Search")
    print("4. Update Marks")
    print("5. Delete")
    print("6. Stats")
    print("7. Exit")
    
    choice = input("Choose (1-7): ")
    
    if choice == "1":
        add_student()
    elif choice == "2":
        show_all()
    elif choice == "3":
        search_student()
    elif choice == "4":
        update_marks()
    elif choice == "5":
        delete_student()
    elif choice == "6":
        show_stats()
    elif choice == "7":
        save_students()
        print("👋 Bye!")
        break
    else:
        print("❌ Wrong choice!")
