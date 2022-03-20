import scrapy


class Deu0027Spider(scrapy.Spider):
    name = 'deu_0027'
    allowed_domains = ['https://www.mannheim-business-school.com/en/']
    start_urls = ['http://https://www.mannheim-business-school.com/en//']

    def parse(self, response):
        pass
