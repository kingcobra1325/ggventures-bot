import scrapy


class Can0008Spider(scrapy.Spider):
    name = 'can_0008'
    allowed_domains = ['https://www.mun.ca/']
    start_urls = ['http://https://www.mun.ca//']

    def parse(self, response):
        pass
