#!/usr/bin/python3
def safe_function(fct, *args):
    import sys
    try:
        res = fct(*args)
    except Exception as err:
        sys.stderr.write(f"Exception: {err}\n")
        res = None
    return res
