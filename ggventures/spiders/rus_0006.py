import scrapy


class Rus0006Spider(scrapy.Spider):
    name = 'rus_0006'
    allowed_domains = ['https://www.topuniversities.com/universities/institute-management-business-law']
    start_urls = ['http://https://www.topuniversities.com/universities/institute-management-business-law/']

    def parse(self, response):
        pass
