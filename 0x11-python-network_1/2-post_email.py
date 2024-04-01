#!/usr/bin/python3
"""import module"""

if __name__ == "__main__":
    from urllib import request, parse
    from sys import argv
    data = parse.urlencode({'email': argv[2]}).encode('utf-8')
    # print(data)
    with request.urlopen(argv[1], data) as requests:
        if requests.getcode() == 200:
            content = requests.read().decode('utf-8')
            print(content)
