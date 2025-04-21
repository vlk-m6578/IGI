"""
LabWork 4(15) "Working with files, classes, serializers, regular expressions, and standard libraries."
Python version: 3.13.2
Developer: Lebedeva Milana
Date of development: 19.04.2025
"""

"""
Main module to run all laboratory tasks.
"""

from task1.controller import RationalController
from task2.text_analysis_controller import TextAnalysisController
from task3.controller import SeriesAnalysisController
from task4.main_task4 import create_square
from task5.controller import MatrixController

def main_menu():
    while True:
        print("\nMain Menu")
        print("1. Task 1: Rational Numbers Serialization.")
        print("2. Task 2: Text Analysis")
        print("3. Task 3: Series Expansion")
        print("4. Task 4: Square")
        print("5. Task 5: Matrix Analysis")
        print("0. Exit")
        choice = input("Enter your choice: ")

        if choice == "1":
            RationalController().run()
        elif choice == "2":
            run_text_analysis()
        elif choice == "3":
            SeriesAnalysisController().run_analysis()
        elif choice == "4":
            create_square()
        elif choice == "5":
            MatrixController().run()
        elif choice == "0":
            print("Exiting program...")
            break
        else:
            print("Invalid choice. Try again.")

def run_text_analysis():
    """Handle Task 2 workflow."""
    file_path = input("Enter path to text file: ").strip()
    
    try:
        with open(file_path, "r", encoding="utf-8") as f:
            text = f.read()
    except FileNotFoundError:
        print("Error: File not found.")
        return
    except UnicodeDecodeError:
        print("Error: Invalid file encoding.")
        return
    
    controller = TextAnalysisController()
    controller.run_analysis(text)
    
    # Display all results
    print("\n=== Analysis Results ===")
    print(f"Total sentences: {controller.results.get('total_sentences', 0)}")
    print(f"Declarative sentences: {controller.results.get('declarative_sentences', 0)}")
    print(f"Interrogative sentences: {controller.results.get('interrogative_sentences', 0)}")
    print(f"Exclamatory sentences: {controller.results.get('exclamatory_sentences', 0)}")
    print(f"Average sentence length: {controller.results.get('avg_sentence_length', 0)}")
    print(f"Average word length: {controller.results.get('avg_word_length', 0)}")
    print(f"Smiles found: {controller.results.get('smiles_count', 0)}")
    print(f"Phones found: {controller.results.get('phones', [])}")
    print(f"Filtered words: {controller.results.get('filtered_words', [])}")
    print(f"Words with consonant endings: {controller.results.get('consonant_endings_count', 0)}")
    print(f"Every 7th word: {controller.results.get('seventh_words', [])}")
    print(f"Words with avg length: {controller.results.get('words_with_avg_length', 'N/A')}")
    
    # Save results
    controller.save_results()

if __name__ == "__main__":
    main_menu()