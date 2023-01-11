#!/usr/bin/python3
"""
    function that reads a text file (UTF8)
    and prints it to stdout:
    Prototype: def read_file(filename=""):
    You must use the with statement
    You don’t need to manage file permission or
    file doesn't exist exceptions.
"""


def read_file(filename=""):
    """ read a file """
    if filename:
        with open(filename, mode="r", encoding='utf-8') as file:
            for line in file:
                print(line, end="")
