#!/usr/bin/python3

def safe_print_list_integers(my_list=[], x=0):
    
    try:
        if my_list[i] >= 0:
            for x in my_list:
                print(my_list[x], end="")
                x = x+1
        i=i+1
    except IndexError:
        print("list index out of range")
