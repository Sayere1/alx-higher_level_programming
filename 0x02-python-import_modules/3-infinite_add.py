#!/usr/bin/python3

if __name__ == "__main__":

    import sys

    argv = sys.argv
    y = len(argv) - 1
    sum = 0
    if y == 0:
        print(sum)
    else:
        for i in range(1, len(argv)):
            sum += int(argv[i])
        print(sum)
