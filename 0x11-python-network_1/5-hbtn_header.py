#!/usr/bin/python3
"""import module"""

if __name__ == "__main__":
    import requests
    from sys import argv
    print(requests.get(argv[1]).headers.get("X-Request-Id"))
