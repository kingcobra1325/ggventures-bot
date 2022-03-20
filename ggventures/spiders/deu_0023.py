import scrapy


class Deu0023Spider(scrapy.Spider):
    name = 'deu_0023'
    allowed_domains = ['https://www.frs.uni-freiburg.de/en/iga-en/promotion/ansprechstellen/ansprechst-en']
    start_urls = ['http://https://www.frs.uni-freiburg.de/en/iga-en/promotion/ansprechstellen/ansprechst-en/']

    def parse(self, response):
        pass
