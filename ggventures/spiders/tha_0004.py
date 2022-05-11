import scrapy


class Tha0004Spider(scrapy.Spider):
    name = 'tha_0004'
    allowed_domains = ['https://www.ku.ac.th/en/faculty-of-business-administration/']
    start_urls = ['http://https://www.ku.ac.th/en/faculty-of-business-administration//']

    def parse(self, response):
        pass
