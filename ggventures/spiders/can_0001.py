import scrapy


class Can0001Spider(scrapy.Spider):
    name = 'can_0001'
    allowed_domains = ['https://brocku.ca/']
    start_urls = ['http://https://brocku.ca//']

    def parse(self, response):
        pass
