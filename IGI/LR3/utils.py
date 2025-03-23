def log_decorator(func):
    """
    Decorator for logging function calls
    """
    def wrapper(*args, **kwargs):
        print(f"Function call: {func.__name__}")
        return func(*args, **kwargs)
    return wrapper