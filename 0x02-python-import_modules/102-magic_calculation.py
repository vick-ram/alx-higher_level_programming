def magic_calculation(a, b):
    # Import the add and sub functions from the magic_calculation_102 module
    from magic_calculation_102 import add, sub
    # Compare a and b
    if a < b:
        # If a is less than b, assign the result of add(a, b) to c
        c = add(a, b)
        # Loop from 4 to 6 (excluding 6)
        for i in range(4, 6):
            # Add i to c
            c = add(c, i)
        # Return c
        return c
    else:
        # If a is not less than b, return the result of sub(a, b)
        return sub(a, b)
