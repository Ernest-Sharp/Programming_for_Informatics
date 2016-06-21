import urllib
from bs4 import BeautifulSoup
result = 0
html = urllib.urlopen("http://python-data.dr-chuck.net/comments_206756.html").read()
soup = BeautifulSoup(html, 'html.parser')
tags = soup('span')
for tag in tags:
    num = int(tag.contents[0])
    result = result + num

print result