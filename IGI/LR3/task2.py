from input import input_int, input_agreement

def sum():
    """
    Calculate sum of numbers until value > 100
    """
    sum = 0
    while True:
        num = input_int("Enter integer(stop when >100): ")
        if num > 100:
            break
        sum += num
    return sum

def run_task2():
    while True:
        print("\nStart entering numbers: ")

        result = sum()

        print(f"Total sum: {result}")

        if not input_agreement("\nContinue calculation? (y/n): "):
            break