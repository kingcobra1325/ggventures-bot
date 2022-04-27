import scrapy


class Chn0043Spider(scrapy.Spider):
    name = 'chn_0043'
    allowed_domains = ['https://www.tsinghua.edu.cn/en/']
    start_urls = ['http://https://www.tsinghua.edu.cn/en//']

    def parse(self, response):
        pass
