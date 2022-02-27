import scrapy


class Can0007Spider(scrapy.Spider):
    name = 'can_0007'
    allowed_domains = ['https://www.degroote.mcmaster.ca/']
    start_urls = ['http://https://www.degroote.mcmaster.ca//']

    def parse(self, response):
        pass
