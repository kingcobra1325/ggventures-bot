import scrapy


class Aus0025Spider(scrapy.Spider):
    name = 'aus_0025'
    allowed_domains = ['https://www.newcastle.edu.au/school/newcastle-business-school']
    start_urls = ['http://https://www.newcastle.edu.au/school/newcastle-business-school/']

    def parse(self, response):
        pass
