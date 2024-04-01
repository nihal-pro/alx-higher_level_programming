#!/usr/bin/python3
"""import module"""

if __name__ == "__main__":
    from urllib import request
    from sys import argv
    with request.urlopen(argv[1]) as requests:
        if requests.getcode() == 200:
            # print(requests.headers)
            print(requests.headers['X-Request-Id'])
