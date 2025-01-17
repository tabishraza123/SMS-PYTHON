import json
import os

def display_menu():
    """Displays the menu options."""
    print("\nMenu:")
    print("1. Register a new student")
    print("2. Display all students")
    print("3. Exit")

def register_student():
    """Registers a new student by taking input and saving it to a file."""
    new_student = {}
    try:
        new_student["id"] = int(input("Please enter student ID: "))
        new_student["name"] = input("Please enter student name: ")
        new_student["qualification"] = input("Please enter student qualification: ")
        new_student["age"] = int(input("Please enter student age: "))
        new_student["address"] = input("Please enter student address: ")
        new_student["contact_number"] = input("Please enter contact number: ")
    except ValueError:
        print("Invalid input. Please enter the correct data type.")
        return 0
