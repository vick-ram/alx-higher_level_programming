#!/usr/bin/python3
if __name__ == "__main__":
    def add_tuple(tuple_a=(), tuple_b=()):
        a1, a2 = tuple_a + (0, 0)
        b1, b2 = tuple_b + (0, 0)
        return (a1 + b1, a2 + b2)
