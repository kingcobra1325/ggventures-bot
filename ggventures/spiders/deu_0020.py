import scrapy


class Deu0020Spider(scrapy.Spider):
    name = 'deu_0020'
    allowed_domains = ['https://www.uni-due.de/ub/en/ewiwi.shtml']
    start_urls = ['http://https://www.uni-due.de/ub/en/ewiwi.shtml/']

    def parse(self, response):
        pass
