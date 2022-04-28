import scrapy


class Chn0045Spider(scrapy.Spider):
    name = 'chn_0045'
    allowed_domains = ['https://en.whu.edu.cn/']
    start_urls = ['http://https://en.whu.edu.cn//']

    def parse(self, response):
        pass
