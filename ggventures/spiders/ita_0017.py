import scrapy


class Ita0017Spider(scrapy.Spider):
    name = 'ita_0017'
    allowed_domains = ['https://www.unisi.it/centri-servizi-di-facolt%C3%A0/centro-servizi-facolt%C3%A0-di-economia-richard-m-goodwin']
    start_urls = ['http://https://www.unisi.it/centri-servizi-di-facolt%C3%A0/centro-servizi-facolt%C3%A0-di-economia-richard-m-goodwin/']

    def parse(self, response):
        pass
