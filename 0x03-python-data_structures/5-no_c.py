#!/usr/bin/python3
if __name__ == "__main__":
    def no_c(my_string):
        new_string = []
        for char in my_string:
            if char not in "cC":
                new_string.append(char)
        return "".join(new_string)
