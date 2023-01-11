#!/usr/bin/python3
"""
    class Student that defines a student by:
        (based on 11-student.py)
    Public instance attributes:
        first_name
        last_name
        age
    Instantiation with first_name, last_name and age:
    def __init__(self, first_name, last_name, age):
    Public method def to_json(self, attrs=None): that
    retrieves a dictionary representation of a Student instance
    (same as 10-class_to_json.py):
        If attrs is a list of strings, only attribute
        names contained in this list must be retrieved.
        Otherwise, all attributes must be retrieved
    You are not allowed to import any module
"""


class Student:
    """ class to create a dict obj """

    def __init__(self, first_name, last_name, age):
        """ initialization for Student object """
        self.age = age
        self.last_name = last_name
        self.first_name = first_name

    def to_json(self, attrs=None):
        """ retrieves a dictionary representation """
        dic = {}
        if type(attrs) != list:
            return self.__dict__
        else:
            for item in attrs:
                if type(item) != str:
                    return self.__dict__
            for key in self.__dict__:
                if key in attrs:
                    dic[key] = self.__dict__[key]
        return dic
