import scrapy


class Deu0025Spider(scrapy.Spider):
    name = 'deu_0025'
    allowed_domains = ['https://www.uni-hohenheim.de/en/international-business-and-economics-masters']
    start_urls = ['http://https://www.uni-hohenheim.de/en/international-business-and-economics-masters/']

    def parse(self, response):
        pass
