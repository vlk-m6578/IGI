"""
LabWork 3 "Standard data types, collections, functions, modules."
Python version: 3.13.2
Developer: Lebedeva Milana
Date of development: 20.03.2025
"""

from task1 import run_task1
from task2 import run_task2
from task3 import run_task3
from task4 import run_task4
from task5 import run_task5


def show_menu():
    """Display main menu"""
    print("\n" + "=" * 30)
    print("Main menu: ")
    print("1. task1")
    print("2. task2")
    print("3. task3")
    print("4. task4")
    print("5. task5")
    print("6. Exit")
    print("=" * 30)


def main():
    """Main program"""
    while True:
        show_menu()
        choice = input("Choose: ")

        try:
            if choice == '1':
                run_task1()
            elif choice == '2':
                run_task2()
            elif choice == '3':
                run_task3()
            elif choice == '4':
                run_task4()
            elif choice == '5':
                run_task5()
            elif choice == '6':
                print("Exiting program...")
                break
            else:
                print("Invalid choice. Try again: ")

        except Exception as e:
            print(f"Error {str(e)}")

if __name__ == "__main__": main() 
            
