#!/usr/bin/python3
"""
    function that returns an object
    (Python data structure) represented by a JSON string:
    Prototype: def from_json_string(my_str):
    You don’t need to manage exceptions if the
    JSON string doesn’t represent an object.
"""


import json


def from_json_string(my_str):
    """ take json str and gives a python object """
    return json.loads(my_str)
