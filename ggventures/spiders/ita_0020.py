import scrapy


class Ita0020Spider(scrapy.Spider):
    name = 'ita_0020'
    allowed_domains = ['https://web.uniroma1.it/fac_economia/']
    start_urls = ['http://https://web.uniroma1.it/fac_economia//']

    def parse(self, response):
        pass
