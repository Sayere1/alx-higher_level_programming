#!/usr/bin/python3

if __name__ == "__main__":

    import sys

    argv = sys.argv
    y = len(argv) - 1
    if y == 0:
        print("0 arguments.")
    elif y == 1:
        print("{} argument:".format(y))
        print("{}: {}".format(y, argv[y]))
    elif y > 1:
        print("{} arguments:".format(y))
        for i in range(1, len(argv)):
            print("{}: {}".format(i, argv[i]))
