# Sample data: http://python-data.dr-chuck.net/comments_42.xml (Sum=2553)
# OBJECTIVE: SUM number of comments

import urllib
import xml.etree.ElementTree as ET
counts = 0
url = raw_input("Enter location:")
html = urllib.urlopen(url).read()
tree = ET.fromstring(html)
lst = tree.findall("comments/comment")
print "Retrieving", url
print "Count: ", len(lst)
for comment in lst:
    counts = counts + int(comment.find('count').text)
print "Sum: ", counts
