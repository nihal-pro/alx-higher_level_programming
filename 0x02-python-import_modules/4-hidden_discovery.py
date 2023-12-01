#!/usr/bin/python3
if __name__ == "__main__":
    import importlib.util
    from inspect import getmembers, isfunction
    spec = importlib.util.spec_from_file_location("hidden", "hidden_4.pyc")
    h = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(h)
    for name, obj in getmembers(h):
        if isfunction(obj) and name != "__init__":
            print("{}".format(name))
