def print_square(size):
    """
    Prints a square with the character #.
    """
    # Check if size is an integer
    if not isinstance(size, int):
        raise TypeError("size must be an integer")

    # Check if size is less than 0
    if size < 0:
        raise ValueError("size must be >= 0")

    # Print a square of size 'size'
    for _ in range(size):
        print("#" * size)
