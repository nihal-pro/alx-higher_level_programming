#!/usr/bin/python3
"""import model"""

if __name__ == "__main__":
    import requests
    from sys import argv
    request = requests.get(argv[1])
    if request.status_code >= 400:
        print("Error code: {}".format(request.status_code))
    else:
        print(request.text)
