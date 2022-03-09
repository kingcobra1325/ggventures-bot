import scrapy


class Fra0025Spider(scrapy.Spider):
    name = 'fra_0025'
    allowed_domains = ['https://www.topuniversities.com/universities/euromed-management']
    start_urls = ['http://https://www.topuniversities.com/universities/euromed-management/']

    def parse(self, response):
        pass
