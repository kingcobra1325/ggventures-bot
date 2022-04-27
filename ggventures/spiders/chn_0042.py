import scrapy


class Chn0042Spider(scrapy.Spider):
    name = 'chn_0042'
    allowed_domains = ['https://en.tongji.edu.cn/']
    start_urls = ['http://https://en.tongji.edu.cn//']

    def parse(self, response):
        pass
