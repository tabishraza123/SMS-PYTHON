import json

def display_menu():
    print("_menu_")
    print("1. Register a new student")
    print("2. Display all students")
    print("3. Search students by Qualification")
    print("4. Search students by contact number")
    print("5. Exit")

def register_student():
    
    newdict = {}
    
    while True:
        student_id = input("Enter your student ID (only integers): ")
        if student_id.isdigit():
            student_id = int(student_id)  
            break  
        else:
            print("Invalid input. Please enter a student ID with only integers.")

    while True:
        name = input("Enter your name: ")
        if name.isalpha() and (len(name) > 2 and len(name) <= 20):
            break
        else:
            print("Invalid input! Please enter a valid name.")

    while True:
        try:
            age = int(input("Enter your age: "))
            if age >= 0:
                break
            else:
                print("Age cannot be negative. Please enter a valid age.")
        except ValueError:
            print("Invalid input! Please enter a valid integer for age.")

    while True:
        address = input("Enter your address: ")
        if address.isalpha() and (len(address) > 2 and len(address) <= 30):
            break
        else:
            print("Invalid input! Please enter a valid address.")

    while True:
        try:
            mobile_number = input("Enter your mobile number: ")
            if mobile_number.isdigit() and len(mobile_number) == 10:
                break
            else:
                print("Invalid input. Please enter a 10-digit mobile number.")
        except ValueError:
            print("Invalid input. Please enter digits only.")

    qualifications = []
    while True:
        qualification = input("Please enter student qualification: ")
        qualifications.append(qualification)
        more_qualifications = input("Do you want to add more qualifications? (yes/no): ").strip().lower()
        if more_qualifications != 'yes':
            break
    
    
    newdict["student_id"] = student_id
    newdict["name"] = name
    newdict["age"] = age
    newdict["address"] = address
    newdict["mobile_number"] = mobile_number
    newdict["qualification"] = qualifications
    
    return newdict


def display_all_students():
    try:
        with open(path, "r") as f:
            students = json.load(f)
        print(json.dumps(students, indent=2))
    except FileNotFoundError:
        print("No student records found.")

def save_to_file(students):
    with open(path, "w") as f:
        json.dump(students, f, indent=2)


path = r"c:\pythonSMS"


# def load_students():
#     try:
#         with open(path, "r") as f:
#             students = json.load(f)
#     except (FileNotFoundError, json.JSONDecodeError):
#         students = []   
#     return students


# def search_student_by_qualification():
#     """Search and display students by qualification."""
#     qualification = input("Enter the qualification to search detail: ").strip()
#     students = load_students()

#     filtered_students = [
#         student for student in students if qualification in student.get("qualification", [])
#     ]
    
#     if filtered_students:
#         print(f"\nStudents with qualification '{qualification}':")
#         print(json.dumps(filtered_students, indent=2))
#     else:
#         print(f"No students found with qualification '{qualification}'.")


# def search_student_by_contactnumber():
#     """Search and display students by contact number."""
#     contactnumber = input("Enter the number to search detail: ").strip()
#     students = load_students()

#     filtered_students = [
#         student for student in students if contactnumber in student.get("mobile_number", "")
#     ]
    
#     if filtered_students:
#         print(f"\nStudents with contact number '{contactnumber}':")
#         print(json.dumps(filtered_students, indent=2))
#     else:
#         print(f"No students found with contact number '{contactnumber}'.")


# while True:
#     display_menu()
#     choice = input("Enter your choice (1-5): ")

#     if choice == '1':  
#         new_student = register_student()
#         students_list = load_students()  
#         students_list.append(new_student) 
#         save_to_file(students_list)  
#         print("Student registered successfully.")
    
#     elif choice == '2':  
#         display_all_students()

#     elif choice == '3':  
#         search_student_by_qualification()

#     elif choice == '4':  
#         search_student_by_contactnumber()       

#     elif choice == '5':  
#         print("*  YOU HAVE EXITED FROM THIS PROGRAM   *")
#         print("        ..   GOODBYE  ..")
#         break
    
#     else:
#         print("Invalid choice. Please try again.")