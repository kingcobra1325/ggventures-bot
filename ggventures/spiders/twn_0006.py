import scrapy


class Twn0006Spider(scrapy.Spider):
    name = 'twn_0006'
    allowed_domains = ['https://www.ntust.edu.tw/?Lang=en']
    start_urls = ['http://https://www.ntust.edu.tw/?Lang=en/']

    def parse(self, response):
        pass
