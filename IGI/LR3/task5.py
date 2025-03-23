from input import input_agreement, input_int, input_float, input_int_positive

def input_list():
    """
        Input list of float with validation
        Returns:
            list
    """
    lst = []
    n = input_int_positive("Enter list size: ")
    for i in range(n):
        while True:
            num = input_float(f"Element {i}: ")
            lst.append(num)
            break
    return lst

def task_with_list(lst):
    """
    Work with list according to requirements:
        1. Find count of zero elements
        2. Calculate sum of elements located after the minimum abs element
    Args:
        list
    Returns:
        tuple: (count, sum)
    """
    count = sum(1 for i in lst if i == 0)
    
    lst_abs = [abs(i) for i in lst]
    min_abs = min(abs(i) for i in lst_abs)
    min_index = lst_abs.index(min_abs)
    sum_after_zero = sum(lst[min_index + 1:]) if min_index + 1 < len(lst) else 0

    return count, sum_after_zero

def run_task5():

    while True:
        numbers = input_list()
        print("\nEntered list: ", numbers)

        count, sum_after_zero = task_with_list(numbers)

        print("\nResults:")
        print(f"Count of zero elements: {count}")
        print(f"Sum: {sum_after_zero}")

        if not input_agreement("\nContinue? (y/n): "):
            break

    