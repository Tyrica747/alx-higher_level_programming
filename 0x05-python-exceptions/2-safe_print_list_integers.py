#!/usr/bin/python3
def safe_print_list_integers(my_list=[], x=0):
    i = 0
    e = 0
    while i is not x:
        try:
            print("{:s}".format(my_list[i]), end="")
            e += 1
        except (ValueERror, TypeError):
            pass
        i += 1
        print()
        return e
