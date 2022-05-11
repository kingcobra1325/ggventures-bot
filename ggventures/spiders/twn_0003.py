import scrapy


class Twn0003Spider(scrapy.Spider):
    name = 'twn_0003'
    allowed_domains = ['https://commerce.nccu.edu.tw/?locale=en']
    start_urls = ['http://https://commerce.nccu.edu.tw/?locale=en/']

    def parse(self, response):
        pass
