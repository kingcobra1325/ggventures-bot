import scrapy


class Can0017Spider(scrapy.Spider):
    name = 'can_0017'
    allowed_domains = ['https://haskayne.ucalgary.ca/']
    start_urls = ['http://https://haskayne.ucalgary.ca//']

    def parse(self, response):
        pass
