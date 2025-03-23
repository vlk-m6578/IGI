def input_int(value):
    """Get validated int input from user"""
    while True:
        try:
            return int(input(value))
        except ValueError:
            print("Invalid input. Try again: ")


def input_float(value):
    """Get validated float input from user"""
    while True:
        try:
            return float(input(value))
        except ValueError:
            print("Invalid input. Try again: ")


def input_int_positive(value):
    """Get validated int positive input from user"""
    while True:
        try:
            num = int(input(value))
            if num > 0:
                return num 
            else:
                print("Number must be positive. Try again.")
        except ValueError:
            print("Invalid input. Try again: ")


def input_agreement(value):
    """Get validated yes/no input from user"""
    while True:
        result = input(value).lower()
        if result in ('y', 'yes'):
            return True
        elif result in ('n', 'no'):
            return False
        print("Enter yes or no: ")