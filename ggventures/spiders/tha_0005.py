import scrapy


class Tha0005Spider(scrapy.Spider):
    name = 'tha_0005'
    allowed_domains = ['https://mba.kku.ac.th/site/eng/?page_id=98']
    start_urls = ['http://https://mba.kku.ac.th/site/eng/?page_id=98/']

    def parse(self, response):
        pass
