import scrapy


class Chn0037Spider(scrapy.Spider):
    name = 'chn_0037'
    allowed_domains = ['https://www.seu.edu.cn/english/']
    start_urls = ['http://https://www.seu.edu.cn/english//']

    def parse(self, response):
        pass
