# -*- coding:utf-8 -*-
from baikespider import urls, downloader, parser, outputer


class SpiderMain(object):
    def __init__(self):
        self.urls = urls.UrlManger()
        self.download = downloader.HtmlDownloader()
        self.parser = parser.HtmlParser()
        self.output = outputer.HtmlOutput()

    def craw(self, url, craw_num=5):
        print(craw_num)
        count = 1
        self.urls.add_new_url(url)
        while self.urls.has_new_url():
            try:
                new_url = self.urls.get_new_url()
                print(new_url)
                print('craw %d', count)
                html_cont = self.download.down_load(new_url)
                new_urls, new_data = self.parser.parse(new_url, html_cont)
                self.urls.add_new_urls(new_urls)
                self.output.collect_data(new_data)
                count += 1
                if count == craw_num:
                    break
            except:
                print('craw failed')

        self.output.output_html()


if __name__ == '__main__':
    root_url = "https://baike.baidu.com/item/Python"
    obj_spider = SpiderMain()
    obj_spider.craw(root_url)
