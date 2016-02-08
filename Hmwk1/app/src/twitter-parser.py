#!/usr/bin/python

# requires https://github.com/edburnett/twitter-text-python 
# can be installed via
# $ pip install twitter-text-python

from __future__ import unicode_literals
from ttp import ttp

p = ttp.Parser()
result = p.parse("@burnettedmond, you now support #IvoWertzel's tweet parser! https://github.com/edburnett/")

print("Printing reply-to user: " + result.reply)
print("Printing user mentions: ")
print(result.users)
print("Printing Hashtags: ")
print(result.tags)
print("Printing URLS: ")
print(result.urls)
