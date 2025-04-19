
from typing import Dict
from task1_serialization.utils import input_rational, validate_input
from task1_serialization.serializers import CSVSerializer, PickleSerializer
from task1_serialization.models import RationalNumber

class RationalController:
    """Controller class for managing rational numbers operations."""

    def __init__(self):
        self.numbers: Dict[str, RationalNumber] = {}
        self.serializers = {
            'csv': CSVSerializer(),
            'pickle': PickleSerializer()
        }

    def run(self):
        """Main interaction loop for Task 1."""
        while True:
            print("\nTask 1 Menu")
            print("1. Input 10 rational numbers")
            print("2. Check for duplicates")
            print("3. Find maximum number")
            print("4. Serialize data")
            print("5. Deserialize data")
            print("6. Display numbers")
            print("0. Return to Main Menu")
            choice = input("Enter your choice: ")

            if choice == "1":
                self.input_numbers()
            elif choice == "2":
                self.check_duplicates()
            elif choice == "3":
                self.find_max()
            elif choice in ("4", "5"):
                self.handle_serialization(choice)
            elif choice == "6":
                self.display_numbers()
            elif choice == "0":
                break
            else:
                print("Invalid choice. Try again.")

    def input_numbers(self):
        """Input 10 rational numbers from user."""
        self.numbers.clear()
        for i in range(1, 11):
            while True:
                try:
                    num = input_rational(f"Enter number {i} (format a/b): ")
                    self.numbers[f"num{i}"] = num
                    break
                except ValueError as e:
                    print(f"Error: {e}")

    def check_duplicates(self):
        """Check for duplicate numbers in the dataset."""
        values = list(self.numbers.values())
        duplicates = any(
            values[i] == values[j]
            for i in range(len(values))
            for j in range(i + 1, len(values))
        )
        print("Duplicate numbers exist." if duplicates else "No duplicates found.")

    def find_max(self):
        """Find and display the maximum rational number."""
        if not self.numbers:
            print("No numbers available.")
            return
        max_num = max(self.numbers.values())
        print(f"Maximum number: {max_num}")

    def handle_serialization(self, choice: str):
        """Handle serialization/deserialization operations."""
        serializer_type = input("Choose serializer (csv/pickle): ").lower()
        serializer = self.serializers.get(serializer_type)

        if not serializer:
            print("Invalid serializer type.")
            return
        
        filename = input("Enter filename: ")
        try:
            if choice == "4":
                serializer.serialize(self.numbers, filename)
                print("Data serialized successfully.")
            else:
                self.numbers = serializer.deserialize(filename)
                print("Data deserialized successfully.")
        except Exception as e:
            print(f"Error: {str(e)}")

    def display_numbers(self):
        """Display all stored numbers."""
        for key, value in self.numbers.items():
            print(f"{key}: {value}")
        


         