import json

def display_menu():
    print("menu:")
    print("1. Register a new student")
    print("2. Display all students")
    print("3. Search students by Qualification")
    print("4. Search students by contact number")
    print("5. Exit")

def register_student():
    # Create a new dictionary for student data
    newdict = {}
    
    newdict["id"] = int(input("Please enter student ID: "))
    newdict["name"] = input("Please enter student name: ")
    newdict["age"] = int(input("Please enter student age: "))  
    newdict["address"] = input("Please enter student address: ")
   # newdict["Qualification"] = input("Please enter student qualification: ")
    newdict["contactnumber"] = input("Please enter contact number: ")
    
    qualifications = []
    while True:
      qualification = input("Please enter student qualification: ")
      qualifications.append(qualification)
        
      more_qualifications = input("Do you want to add more qualifications? (yes/no): ").strip().lower()
      if more_qualifications != 'yes':
       break
    
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


path = r"C:\pythoncode\SRC\filehandling\data.json"
students_list = []


## STUDENT DETAIL SEARCH BY QUALIFICATION
def search_student_by_qualification():
    """Search and display students by qualification."""
    qualification = input("Enter the qualification to search detail: ").strip()
    try:
    
        with open(path, "r") as f:
            students = json.load(f)
        
    
        filtered_students = [
            student for student in students if qualification in student.get("qualification", [])
        ]
        
    
        if filtered_students:
            print(f"\nStudents with qualification '{qualification}':")
            print(json.dumps(filtered_students, indent=2))
        else:
            print(f"No students found with qualification '{qualification}'.")
    except FileNotFoundError:
        print("No student records found.")
    except json.JSONDecodeError:
        print("Error reading student data.")

        

def search_by_mobile_number():
    contact_number = input("Please enter the contact number to search: ")
    
    try:
        with open(path, "r") as f:
            students = json.load(f)
        
        found = False
        for student in students:
            if student["contactnumber"] == contact_number:
                print(f"Student found: {json.dumps(student, indent=2)}")
                found = True
                break
        
        if not found:
            print("No student found with the given contact number.")
    
    except FileNotFoundError:
        print("No student records found.")

# Main program loop
while True:
    display_menu()
    """Main function to run the student management system."""
    choice = input("Enter your choice (1-5): ")

    if choice == '1':  # Register a new student
        # new_student = register_student()
        # students_list.append(new_student)
        # save_to_file(students_list)
        # print("Student registered successfully.")
        new_student = register_student()
        with open(path,"r") as f:
            students_list=json.load(f)

            students_list.append(new_student)
            save_to_file(students_list)
            print("student register succesfully")
    
    elif choice == '2':  # Display all students
        display_all_students()

    elif choice == '3':  # search student detail by qualification
         search_student_by_qualification() 

    elif choice == '4':  # search student detail by contact number
         search_by_mobile_number()        
    
    elif choice == '5':  # Exit
        print(" YOU ARE EXIT FROM THIS PROGRAM (GOOD BYE!).")
        break
    
    else:
        print("Invalid choice. Please try again.")