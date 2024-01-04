#!/usr/bin/python3
if __name__ == "__main__":
    from sys import argv

    def infinite_add(args):
        result = sum(int(arg) for arg in args)
        print(result)

if __name__ == "__main__":
    infinite_add(argv[1:])
