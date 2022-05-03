import scrapy


class Esp0015Spider(scrapy.Spider):
    name = 'esp_0015'
    allowed_domains = ['https://www.topuniversities.com/universities/iede-business-school']
    start_urls = ['http://https://www.topuniversities.com/universities/iede-business-school/']

    def parse(self, response):
        pass
