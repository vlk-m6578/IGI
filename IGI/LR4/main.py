"""
LabWork 4(15) "Working with files, classes, serializers, regular expressions, and standard libraries."
Python version: 3.13.2
Developer: Lebedeva Milana
Date of development: 19.04.2025
"""

"""
Main module to run all laboratory tasks.
"""

from task1_serialization.rational import RationalController

def main_menu():
    while True:
        print("\nMain Menu")
        print("1. Task 1: Rational Numbers Serialization.")
        print("0. Exit")
        choice = input("Enter your choice: ")

        if choice == "1":
            RationalController().run()
        elif choice == "0":
            print("Exiting program...")
            break
        else:
            print("Invalid choice. Try again.")

if __name__ == "__main__":
    main_menu()