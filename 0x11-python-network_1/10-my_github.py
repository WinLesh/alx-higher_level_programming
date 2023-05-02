#!/usr/bin/python3
""" A Script that gets info of account from Github API using credentials
uses the github API to diplay your id
"""

if __name__ == "__main__":
    auth = HTTPBasicAuth(sys.argv[1], sys.argv[2])
    r = requests.get("https://api.github.com/user", auth=auth)
    print(r.json().get("id"))
