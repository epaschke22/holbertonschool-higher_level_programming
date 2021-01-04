#!/usr/bin/python3
def safe_function(fct, *args):
    import sys
    try:
        return fct(args[0], args[1])
    except ZeroDivisionError:
        print("Exception: division by zero", file=sys.stderr)
    except IndexError:
        print("Exception: list index out of range", file=sys.stderr)
    return None
