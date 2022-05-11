import scrapy


class Ukr0005Spider(scrapy.Spider):
    name = 'ukr_0005'
    allowed_domains = ['https://www.unipage.net/en/10197/lviv_institute_of_management']
    start_urls = ['http://https://www.unipage.net/en/10197/lviv_institute_of_management/']

    def parse(self, response):
        pass
