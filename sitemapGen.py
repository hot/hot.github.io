#!/usr/bin/python

import json
f = open("main.json")
jData = json.load(f)
f.close()

xmlHead = """<?xml version="1.0" encoding="UTF-8"?>
<urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9"> 
"""

xmlEntry = """ <url><loc>http://hot.github.io/posts/{}</loc></url>
"""
xmlEnd = """</urlset>"""

wholeXml = xmlHead

for post in jData["posts"]:
    wholeXml += xmlEntry.format(post["path"])

wholeXml += xmlEnd

with open('sitemap.xml', 'w') as outfile:
    outfile.write(wholeXml)


