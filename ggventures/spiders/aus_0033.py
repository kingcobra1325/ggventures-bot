import scrapy


class Aus0033Spider(scrapy.Spider):
    name = 'aus_0033'
    allowed_domains = ['https://www.westernsydney.edu.au/schools/sobus']
    start_urls = ['http://https://www.westernsydney.edu.au/schools/sobus/']

    def parse(self, response):
        pass
