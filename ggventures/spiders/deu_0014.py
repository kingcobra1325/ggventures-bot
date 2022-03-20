import scrapy


class Deu0014Spider(scrapy.Spider):
    name = 'deu_0014'
    allowed_domains = ['https://www.ku.de/wfi']
    start_urls = ['http://https://www.ku.de/wfi/']

    def parse(self, response):
        pass
