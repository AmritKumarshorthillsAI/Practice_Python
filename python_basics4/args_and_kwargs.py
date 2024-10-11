def print_args(*args):
    """
    Print all positional arguments.
    
    Parameters:
    *args: Variable length argument list.
    """
    print("Positional arguments received:")
    for arg in args:
        print(arg)

def print_kwargs(**kwargs):
    """
    Print all keyword arguments.
    
    Parameters:
    **kwargs: Arbitrary keyword arguments.
    """
    print("Keyword arguments received:")
    for key, value in kwargs.items():
        print(f"{key}: {value}")

def combine_args_and_kwargs(*args, **kwargs):
    """
    Combine positional and keyword arguments.
    
    Parameters:
    *args: Variable length argument list.
    **kwargs: Arbitrary keyword arguments.
    """
    print(type(args))
    print(type(kwargs))
    print("Combining positional and keyword arguments:")
    print("Positional arguments:", args)
    print("Keyword arguments:", kwargs)

def main():
    # Example usage of *args
    print_args(1, 2, 3, "four", "five")

    # Example usage of **kwargs
    print_kwargs(name="Alice", age=30, city="New York")

    # Example usage of both *args and **kwargs
    combine_args_and_kwargs(10, 20, fruit="apple", vegetable="carrot")

if __name__ == "__main__":
    main()
