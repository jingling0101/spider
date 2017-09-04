# -*- coding:utf8 -*-
class UrlManger(object):
    def __init__(self):
        self.end_urls = set()
        self.new_urls = set()

    def add_new_url(self, url):
        if url is None:
            return
        if url not in self.end_urls and url not in self.new_urls:
            return self.new_urls.add(url)

    def add_new_urls(self, urls):
        if urls is None or len(urls) == 0:
            return
        for url in urls:
            if url not in self.new_urls and url not in self.end_urls:
                self.new_urls.add(url)
        # print('new',self.new_urls)
        # print('end',self.end_urls)
        return self.new_urls

    def has_new_url(self):
        return len(self.new_urls) > 0

    def get_new_url(self):
        new_url = self.new_urls.pop()
        self.end_urls.add(new_url)
        return new_url
