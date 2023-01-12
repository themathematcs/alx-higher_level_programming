#!/usr/bin/python3
"""
    function that reads n lines of a text file (UTF8)
    and prints it to stdout:
    Prototype: def read_lines(filename="", nb_lines=0):
    Read the entire file if nb_lines is lower or equal
    to 0 OR greater or equal to the total number of lines
    of the file
    You must use the with statement
    You don’t need to manage file permission or file doesn't
    exist exceptions.
"""


def read_lines(filename="", nb_lines=0):
    """ read nb_lines of a text """
    with open(filename, encoding='utf-8') as f:
        if (nb_lines <= 0):
                print(f.read(), end="")
        else:
            cont = 0
            while (cont < nb_lines):
                print(f.readline(), end="")
                cont += 1
