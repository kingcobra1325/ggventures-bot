import scrapy


class Chn0030Spider(scrapy.Spider):
    name = 'chn_0030'
    allowed_domains = ['https://en.sdu.edu.cn/']
    start_urls = ['http://https://en.sdu.edu.cn//']

    def parse(self, response):
        pass
