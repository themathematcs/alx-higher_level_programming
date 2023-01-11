#!/usr/bin/python3
""" class MyList that inherits from list """


class MyList(list):
    """ MyList inherits from list """

    def print_sorted(self):
        """ print list in ascending order """
        print(sorted(self))
