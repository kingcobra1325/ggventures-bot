import scrapy


class Chn0050Spider(scrapy.Spider):
    name = 'chn_0050'
    allowed_domains = ['http://english.ynu.edu.cn/']
    start_urls = ['http://http://english.ynu.edu.cn//']

    def parse(self, response):
        pass
