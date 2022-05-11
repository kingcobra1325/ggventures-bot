import scrapy


class Twn0007Spider(scrapy.Spider):
    name = 'twn_0007'
    allowed_domains = ['https://management.ntu.edu.tw/en/']
    start_urls = ['http://https://management.ntu.edu.tw/en//']

    def parse(self, response):
        pass
