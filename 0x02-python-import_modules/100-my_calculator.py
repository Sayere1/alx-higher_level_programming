#!/usr/bin/python3

if __name__ == "__main__":

    import sys
    from calculator_1 import add, mul, sub, div

    if len(sys.argv) - 1 != 3:
        print("Usage: ./100-my_calculator.py <a> <operator> <b>")
        sys.exit(1)
    signs = ["*", "+", "-", "/"]
    argv = sys.argv
    m = argv[1]
    n = argv[2]
    o = argv[3]
    if y not in signs:
        print("Unknown operator. Available operators: +, -, * and /")
        sys.exit(1)
    else:
        if argv[2] == '+':
            print("{} {} {} = {}".format(m, n, o, add(int(m), int(o))))
        elif argv[2] == "*":
            print("{} {} {} = {}".format(m, n, o, mul(int(m), int(o))))
        elif argv[2] == '/':
            print("{} {} {} = {}".format(m, n, o, div(int(m), int(o))))
        elif argv[2] == '-':
            print("{} {} {} = {}".format(m, n, o, sub(int(m), int(o))))
