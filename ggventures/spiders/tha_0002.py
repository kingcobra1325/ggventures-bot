import scrapy


class Tha0002Spider(scrapy.Spider):
    name = 'tha_0002'
    allowed_domains = ['https://www.cmu.ac.th/en/faculty/business_administration/aboutus']
    start_urls = ['http://https://www.cmu.ac.th/en/faculty/business_administration/aboutus/']

    def parse(self, response):
        pass
