#!/usr/bin/python3
"""import module"""

if __name__ == "__main__":
    import requests
    from sys import argv
    auth = (argv[1], argv[2])
    request = requests.get("https://api.github.com/user", auth=auth)
    print(request.json().get("id"))
