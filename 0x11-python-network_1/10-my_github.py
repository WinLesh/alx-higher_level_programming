#!/usr/bin/python3
""" A Script that gets info of account from Github API using credentials
uses the github API to diplay your id
"""
if __name__ == "__main__":
    import sys
    import requests
    user = sys.argv[1]
    pas = sys.argv[2]
    API = "https://api.github.com/users"
    API = API + "/{}".format(user)
    r = requests.get(API, auth=requests.auth.HTTPBasicAuth(user, pas))
    if r.status_code == 200:
        print(r.json().get('id'))
    else:
        print("None")if __name__ == "__main__":
