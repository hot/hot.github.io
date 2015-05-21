#!/usr/bin/python

import json
f = open("main.json")
jData = json.load(f)
f.close()


xmlHead = """
<html>
<body>
"""

xmlEntry = """ <a href=posts/"{}">{}</a>
"""
xmlEnd = """</body></html>"""

wholeXml = xmlHead

for post in jData["posts"]:
    path = post["path"]
    wholeXml += xmlEntry.format(path, path)

wholeXml += xmlEnd

with open('alllinks.html', 'w') as outfile:
    outfile.write(wholeXml)


