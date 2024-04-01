#!/usr/bin/python3
"""Fetches https://alx-intranet.hbtn.io/status"""
if __name__ == "__main__":
    import requests
    with requests.get('https://alx-intranet.hbtn.io/status') as req:
        response = req.text
        print("Body response:")
        print("\t- type: {}".format(type(response)))
        print("\t- content: {}".format(response))
