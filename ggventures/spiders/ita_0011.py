import scrapy


class Ita0011Spider(scrapy.Spider):
    name = 'ita_0011'
    allowed_domains = ['https://www.som.polimi.it/en/the-school/about-us/mip/']
    start_urls = ['http://https://www.som.polimi.it/en/the-school/about-us/mip//']

    def parse(self, response):
        pass
