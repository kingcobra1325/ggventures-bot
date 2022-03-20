import scrapy


class Deu0028Spider(scrapy.Spider):
    name = 'deu_0028'
    allowed_domains = ['https://www.wiwi.uni-muenster.de/fakultaet/en']
    start_urls = ['http://https://www.wiwi.uni-muenster.de/fakultaet/en/']

    def parse(self, response):
        pass
