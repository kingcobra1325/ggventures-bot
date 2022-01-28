import scrapy


class Gbr0047Spider(scrapy.Spider):
    name = 'gbr_0047'
    allowed_domains = ['https://www.uwe.ac.uk/about/faculties-and-departments/business-and-law/bristol-business-school']
    start_urls = ['http://https://www.uwe.ac.uk/about/faculties-and-departments/business-and-law/bristol-business-school/']

    def parse(self, response):
        pass
