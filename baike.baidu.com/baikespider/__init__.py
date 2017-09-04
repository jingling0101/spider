from baikespider import spider

__version__ = '1.0.1'
__copyright__ = "Copyright (c) 2017-2017 Leonard Richardson"
__license__ = "MIT"
__all__ = [
    'SpiderMain',
]
__author__ = 'jingling0101 <621019457@qq.com>'

if __name__ == '__main__':
    print(spider.SpiderMain().__class__)
    print('SpiderMain.....')


class SpiderMain(object):
    def __init__(self):
        self.manager = spider.SpiderMain()
