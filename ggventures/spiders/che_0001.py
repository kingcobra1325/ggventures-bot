import scrapy


class Che0001Spider(scrapy.Spider):
    name = 'che_0001'
    allowed_domains = ['https://www.educatis.org/']
    start_urls = ['http://https://www.educatis.org//']

    def parse(self, response):
        pass
