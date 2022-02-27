import scrapy


class Can0013Spider(scrapy.Spider):
    name = 'can_0013'
    allowed_domains = ['https://esg.uqam.ca/en/']
    start_urls = ['http://https://esg.uqam.ca/en//']

    def parse(self, response):
        pass
