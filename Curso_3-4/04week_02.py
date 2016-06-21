# The program will use urllib to read the HTML from the data
# files below, extract the href= values from the anchor tags,
# scan for a tag that is in a particular position relative to
# the first name in the list, follow that link and repeat the
# process a number of times and report the last name you find.

import urllib
from bs4 import BeautifulSoup

tag_list = list()
result_list = list()
i = 0
url = raw_input("Enter URL: ")
count = raw_input("Enter count: ")
position = raw_input("Enter position: ")
index_pos = int(position)
index_count = int(count)

# Create list of URLs function

def create_list( url ):
    html = urllib.urlopen(url).read()
    data = BeautifulSoup(html, 'html.parser')
    tags = data('a')
    for tag in tags:
        tag_list.append(tag.get('href'))
    return
print "Retrieving: ", url

# Execution
while i < index_count:
    create_list( url )
    url = tag_list[index_pos - 1]
    tag_list = list()
    i = i + 1
    print "Retrieving: ", url
