import scrapy


class Col0001Spider(scrapy.Spider):
    name = 'col_0001'
    allowed_domains = ['https://www.javeriana.edu.co/dir-servicios-universitarios/fac-cienciasadministrativas']
    start_urls = ['http://https://www.javeriana.edu.co/dir-servicios-universitarios/fac-cienciasadministrativas/']

    def parse(self, response):
        pass
