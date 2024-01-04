#!/usr/bin/python3
from sys import argv

args = len(argv) - 1
if args == 0:
    print("0 arguments.")
elif args == 1:
    print("1 argument:")
else:
    print("{} arguments".format(args))
for i in range(1, args + 1):
    print("{}: {}".format(i, argv[i]))
