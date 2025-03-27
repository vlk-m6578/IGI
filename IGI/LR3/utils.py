def log_decorator(func):
    """
    Decorator for logging function calls
    """
    def wrapper(*args, **kwargs):
        print(f"Function call: {func.__name__}")
        return func(*args, **kwargs)
    return wrapper

def value_generator():
    
    x_values = [i for i in range(-5, 6)]   #x from -5 to 5
    eps_values = [10**(-i) for i in range(1, 6)]  #eps from 0.1 to 0.00001

    for x in x_values:
        for eps in eps_values:
            yield x, eps