# The program will prompt for a URL, read the JSON data
# from that URL using urllib and then parse and extract
# the comment counts from the JSON data, compute the sum
# of the numbers in the file and enter the sum below
# Sample data: http://python-data.dr-chuck.net/comments_42.json (Sum=2553)
# Actual data: http://python-data.dr-chuck.net/comments_206757.json (Sum ends with 19)

import json
import urllib
result = 0
url = raw_input("Enter location: ")
if len(url) < 1:
    url = "http://python-data.dr-chuck.net/comments_206757.json"
print "Rerieving", url
url_data = urllib.urlopen(url).read()
print "Retrieved", len(url_data), "characters"
data = json.loads(url_data)
comments = data['comments']
print "Count: ",len(comments)
for comment in comments:
    result = result + int(comment['count'])
print "Sum:", result

