import scrapy


class Esp0020Spider(scrapy.Spider):
    name = 'esp_0020'
    allowed_domains = ['https://dbs.deusto.es/cs/Satellite/deusto-b-school/en/deusto-business-school-1']
    start_urls = ['http://https://dbs.deusto.es/cs/Satellite/deusto-b-school/en/deusto-business-school-1/']

    def parse(self, response):
        pass
