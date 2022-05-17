import scrapy


class Rus0003Spider(scrapy.Spider):
    name = 'rus_0003'
    allowed_domains = ['https://www.ranepa.ru/eng/landings/eng-institute-of-business-studies/']
    start_urls = ['http://https://www.ranepa.ru/eng/landings/eng-institute-of-business-studies//']

    def parse(self, response):
        pass
