#!/usr/bin/python3
"""import module"""

if __name__ == "__main__":
    from sys import argv
    from urllib import request, error
    try:
        with request.urlopen(argv[1]) as resp:
            if resp.getcode() == 200:
                content = resp.read().decode('utf-8')
                print(content)
    except error.HTTPError as err:
        print("Error code: {}".format(err.code))
