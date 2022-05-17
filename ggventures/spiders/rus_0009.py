import scrapy


class Rus0009Spider(scrapy.Spider):
    name = 'rus_0009'
    allowed_domains = ['https://www.rusvuz.com/economics-universities/kazan-state-institute-of-finance-and-economics/']
    start_urls = ['http://https://www.rusvuz.com/economics-universities/kazan-state-institute-of-finance-and-economics//']

    def parse(self, response):
        pass
