#!/usr/bin/python3
"""
    function that appends a string at the end of a
    text file (UTF8) and returns the number of characters added:
    Prototype: def append_write(filename="", text=""):
    If the file doesn’t exist, it should be created
    You must use the with statement
    You don’t need to manage file permission or file
    doesn't exist exceptions.
"""


def append_write(filename="", text=""):
    """ appends a string to the end of file """
    with open(filename, mode="a", encoding='utf-8') as file:
        return file.write(text)
