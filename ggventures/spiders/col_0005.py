import scrapy


class Col0005Spider(scrapy.Spider):
    name = 'col_0005'
    allowed_domains = ['https://www.uexternado.edu.co/administracion-de-empresas/']
    start_urls = ['http://https://www.uexternado.edu.co/administracion-de-empresas//']

    def parse(self, response):
        pass
