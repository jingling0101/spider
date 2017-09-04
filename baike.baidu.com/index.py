import baikespider

# 爬取url
root_url = "https://baike.baidu.com/item/php"
obj_spider = baikespider.SpiderMain()
# 第一个参数为爬取url 第二个是爬取数量  输出为out.html
obj_spider.manager.craw(root_url, 10)
