import scrapy


class Chn0028Spider(scrapy.Spider):
    name = 'chn_0028'
    allowed_domains = ['https://www.ruc.edu.cn/en']
    start_urls = ['http://https://www.ruc.edu.cn/en/']

    def parse(self, response):
        pass
