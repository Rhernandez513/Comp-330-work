#!/usr/bin/python

# requires https://github.com/edburnett/twitter-text-python 
# can be installed via
# $ pip install twitter-text-python

from __future__ import unicode_literals
from ttp import ttp

text = "@burnettedmond, you now support #IvoWertzel's tweet parser! https://github.com/edburnett/\
        @burnettedmond, you now support #IvoWertzel's tweet parser! https://github.com/edburnett/\
        @burnettedmond, you now support #IvoWertzel's tweet parser! https://github.com/edburnett/\
        @burnettedmond, you now support #IvoWertzel's tweet parser! https://github.com/edburnett/"

p = ttp.Parser()
result = p.parse(text)
print("Printing reply-to user: " + result.reply)
print("Printing user mentions: ")
print(result.users)
print("Printing Hashtags: ")
print(result.tags)
print("Printing URLS: ")
print(result.urls)

import unittest

class parser_test(unittest.TestCase):

    def setUp(self):
        self.parser = ttp.Parser()
        self.text = text

    def test_tweet_too_long(self):
        result = self.parser.parse(self.text)
        self.assertEqual(result.users, ['burnettedmond', 'burnettedmond', 'burnettedmond', 'burnettedmond'])

    def test_tweet_works(self):
        result = self.parser.parse(self.text)
        self.assertEqual(result.tags, ['IvoWertzel', 'IvoWertzel', 'IvoWertzel', 'IvoWertzel'])

    def test_mention_count(self):
        result = self.parser.parse(self.text)
        self.assertEqual(len(result.users), 4)

    def test_url_count(self):
        result = self.parser.parse(self.text)
        self.assertEqual(len(result.urls), 4)

    def test_contains_url(self):
        url = 'https://github.com/edburnett/'
        result = self.parser.parse(self.text)
        self.assertIn(url, result.urls)

    def test_contains_user(self):
        user = 'burnettedmond'
        result = self.parser.parse(self.text)
        self.assertIn(user, result.users)

    def test_does_not_contain_user(self):
        user = 'ronarr513'
        result = self.parser.parse(self.text)
        self.assertNotIn(user, result.users)
    
    def test_is_not_referenced_url(self):
        url = 'http://google.com/'
        result = self.parser.parse(self.text)
        self.assertNotIn(url, result.urls)

if __name__ == '__main__':
    unittest.main()

