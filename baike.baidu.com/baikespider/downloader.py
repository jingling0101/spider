# -*- coding:utf8 -*-
from urllib import request


class HtmlDownloader(object):
    def __init__(self):
        pass

    def down_load(self, url):
        self._url = ''
        if url is None:
            return None

        response = request.urlopen(url)
        return response.read().decode("utf-8")
