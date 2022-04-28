import scrapy


class Chn0039Spider(scrapy.Spider):
    name = 'chn_0039'
    allowed_domains = ['http://english.uibe.edu.cn/']
    start_urls = ['http://http://english.uibe.edu.cn//']

    def parse(self, response):
        pass
