import scrapy


class Chn0040Spider(scrapy.Spider):
    name = 'chn_0040'
    allowed_domains = ['http://www.tju.edu.cn/english/']
    start_urls = ['http://http://www.tju.edu.cn/english//']

    def parse(self, response):
        pass
