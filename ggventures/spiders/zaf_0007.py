import scrapy


class Zaf0007Spider(scrapy.Spider):
    name = 'zaf_0007'
    allowed_domains = ['https://commerce.nwu.ac.za/business-school']
    start_urls = ['http://https://commerce.nwu.ac.za/business-school/']

    def parse(self, response):
        pass
