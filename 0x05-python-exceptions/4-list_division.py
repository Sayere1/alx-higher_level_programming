#!/usr/bin/python3

# Args: my_list_1 (list), my_list_2 (list), list_length (int)
# Return: A new list of length list_length containing /

def list_division(my_list1, my_list2, list_length):
    my_new_list = []
    for i in range(0, list_length):
        try:
            division = my_list1[i] / my_list2[i]
        except TypeError:
            print("wrong type")
            division = 0
        except ZeroDivisionError:
            print("division by 0")
            division = 0
        except IndexError:
            print("out of range")
            division = 0
        finally:
            my_new_list.append(division)
    return (my_new_list)