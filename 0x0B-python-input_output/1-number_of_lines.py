#!/usr/bin/python3
"""
    function that returns the number
    of lines of a text file:
    Prototype: def number_of_lines(filename=""):
    You must use the with statement
    You don’t need to manage file permission or
    file doesn't exist exceptions.
"""


def number_of_lines(filename=""):
    """ return the number of lines of a file """
    i = 0
    with open(filename, encoding='utf-8') as file:
        for line in file:
            i += 1
    return i
