import scrapy


class Chn0053Spider(scrapy.Spider):
    name = 'chn_0053'
    allowed_domains = ['http://english.zzu.edu.cn/']
    start_urls = ['http://http://english.zzu.edu.cn//']

    def parse(self, response):
        pass
