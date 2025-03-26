import math
from input import input_float, input_agreement
from utils import log_decorator

@log_decorator
def calculate(x, eps, max_iter = 500):
    """
    Calculate e^x using Taylor series expansion
    Args:
        x(float): Input value
        eps(float): Precision
        max_iter(int): Maximum iterations
    Returns:
        tuple: (result, n, math_result)
        where
            result(float): Final calculation e^x using Taylor
            n(int): Count of iterations
            math_result(float): Calculation e^x using math module
    """
    result = 1.0
    n = 1
    term = 1.0
    math_result = math.exp(x)

    while n<max_iter and abs(term)>eps:
        term *= x/n
        result += term
        n += 1

    return result, n, math_result

def run_task1():
    
    while True:
        x = input_float("Enter x value: ")
        eps = input_float("Enter precision(eps): ")

        result, n, math_result = calculate(x, eps)

        print("\n{:^10}|{:^10}|{:^15}|{:^15}|{:^10}".format("x", "n", "F(x)", "Math F(x)", "eps"))
        print("-"*65)
        print("{:^10.2f}|{:^10}|{:^15.6f}|{:^15.6f}|{:^10.0e}".format(x, n, result, math_result, eps))  

        if not input_agreement("\nContinue calculation? (y/n): "):
            break


