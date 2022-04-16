import scrapy


class Zaf0009Spider(scrapy.Spider):
    name = 'zaf_0009'
    allowed_domains = ['https://regenesys.net/']
    start_urls = ['http://https://regenesys.net//']

    def parse(self, response):
        pass
