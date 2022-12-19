#!/usr/bin/python3

def safe_print_division(a, b):
    try:
        div = a / b
    except (TypeError, ZeroDivisionError):
        div = None
    finally:
        print("Inside result: {}".format(div))
        return (div)
Footer
© 2022 GitHub, Inc.
Footer navigation
Terms
