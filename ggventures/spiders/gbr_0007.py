import scrapy


class Gbr0007Spider(scrapy.Spider):
    name = 'gbr_0007'
    allowed_domains = ['https://www.bayes.city.ac.uk/']
    start_urls = ['http://https://www.bayes.city.ac.uk//']

    def parse(self, response):
        pass
