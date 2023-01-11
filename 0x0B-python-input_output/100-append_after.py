#!/usr/bin/python3
"""
    function that inserts a line of text to a file,
    after each line containing a specific string (see example):
    Prototype:
    def append_after(filename="", search_string="", new_string=""):
    You must use the with statement
    You don’t need to manage file permission or file doesn't exist
    exceptions.
    You are not allowed to import any module
"""


def append_after(filename="", search_string="", new_string=""):
    """ append a string into a new_line after find another """
    text = ""
    with open(filename, mode="r", encoding='utf-8') as f:
        lines = f.readlines()
    for line in lines:
        if line.find(search_string) != -1:
            text += line + new_string
        else:
            text += line
    with open(filename, mode="w", encoding='utf-8') as f:
        f.write(text)
