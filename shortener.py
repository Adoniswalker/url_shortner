from flask import request

from database import Database, insert, get_url
import string
import random


class Shortener:
    def __init__(self):
        pass

    def shorten(self, url):
        unique_url = self.generate_short_url()
        while get_url(unique_url):
            unique_url = self.generate_short_url()
        insert(url, unique_url)
        return unique_url

    def generate_short_url(self):
        letters = string.ascii_letters + string.digits
        return ''.join(random.choice(letters) for i in range(7))

    def get_url(self, short_url):
        return get_url(short_url)
