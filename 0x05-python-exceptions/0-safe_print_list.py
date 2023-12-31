#!/usr/bin/python3

# Args: my_list = elmnt is printed frm this lst , x(int)
# Return: num of elmnt

def safe_print_list(my_list=[], x=0):
    ret_elmnt = 0
    for i in range(x):
        try:
            print("{}".format(my_list[i]), end="")
            ret_elmnt = ret_elmnt + 1
        except IndexError:
            break
    print("")
    return (ret_elmnt)
