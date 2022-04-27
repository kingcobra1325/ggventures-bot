import scrapy


class Col0004Spider(scrapy.Spider):
    name = 'col_0004'
    allowed_domains = ['https://www.eafit.edu.co/escuela-administracion']
    start_urls = ['http://https://www.eafit.edu.co/escuela-administracion/']

    def parse(self, response):
        pass
