import scrapy


class Esp0022Spider(scrapy.Spider):
    name = 'esp_0022'
    allowed_domains = ['https://dbs.deusto.es/cs/Satellite/deusto-b-school/es/deustobschool/sobre-deusto-business-school/presentacion-28']
    start_urls = ['http://https://dbs.deusto.es/cs/Satellite/deusto-b-school/es/deustobschool/sobre-deusto-business-school/presentacion-28/']

    def parse(self, response):
        pass
