import scrapy


class Chn0035Spider(scrapy.Spider):
    name = 'chn_0035'
    allowed_domains = ['https://en.szu.edu.cn/']
    start_urls = ['http://https://en.szu.edu.cn//']

    def parse(self, response):
        pass
