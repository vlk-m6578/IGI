import math
from input import input_float, input_agreement
from utils import log_decorator, value_generator

@log_decorator
def calculate(x, eps, max_iter=500):
    result = 1.0
    n = 1
    term = 1.0
    math_result = math.exp(x)

    while n < max_iter and abs(term) > eps:
        term *= x / n
        result += term
        n += 1

    return result, n, math_result



def run_task1():
    gen = value_generator()
    while True:
        input_method = input("Choose input method (g - generator, n - manual): ").strip().lower()
        
        if input_method == 'g':
            try:
                x, eps = next(gen)
                print(f"Using generated values: x = {x}, eps = {eps}")
            except StopIteration:
                print("No more generated values available. Please switch to manual input.")
                continue
        elif input_method == 'n':
            x = input_float("Enter x value: ")
            eps = input_float("Enter precision (eps): ")
        else:
            print("Invalid input method. Please enter 'g' for generator or 'n' for manual.")
            continue

        result, n, math_result = calculate(x, eps)

        print("\n{:^10}|{:^10}|{:^15}|{:^15}|{:^10}".format("x", "n", "F(x)", "Math F(x)", "eps"))
        print("-" * 65)
        print("{:^10.2f}|{:^10}|{:^15.6f}|{:^15.6f}|{:^10.0e}".format(x, n, result, math_result, eps))

        if not input_agreement("\nContinue calculation? (y/n): "):
            break