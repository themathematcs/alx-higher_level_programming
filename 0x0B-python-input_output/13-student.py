#!/usr/bin/python3
"""
    class Student that defines a student by:
        (based on 12-student.py)
    Public instance attributes:
        first_name
        last_name
        age
    Instantiation with first_name, last_name and age:
    def __init__(self, first_name, last_name, age):
    Public method def to_json(self, attrs=None):
    that retrieves a dictionary representation of a
    Student instance (same as 10-class_to_json.py):
        If attrs is a list of strings, only attributes name
        contain in this list must be retrieved.
        Otherwise, all attributes must be retrieved
    Public method def reload_from_json(self, json):
    that replaces all attributes of the Student instance:
        You can assume json will always be a dictionary
        A dictionary key will be the public attribute name
        A dictionary value will be the value of the public
        attribute
    You are not allowed to import any module
    Now, you have a simple implementation of a serialization
    and deserialization mechanism (concept of representation of
    an object to another format, without losing any information
    and allow us to rebuild an object based on this representation)
"""


class Student:
    """ class to create a dict obj """

    def __init__(self, first_name, last_name, age):
        """ initialization for Student object """
        self.last_name = last_name
        self.first_name = first_name
        self.age = age

    def to_json(self, attrs=None):
        """ retrieves a dictionary representation of obj attrs"""
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

    def reload_from_json(self, json):
        """ replaces all attrs of an instance given json obj """
        for key in json:
            if key in self.__dict__:
                self.__dict__[key] = json[key]
