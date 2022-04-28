import scrapy


class Col0002Spider(scrapy.Spider):
    name = 'col_0002'
    allowed_domains = ['https://www.udea.edu.co/wps/portal/udea/web/inicio/unidades-academicas/ciencias-economicas']
    start_urls = ['http://https://www.udea.edu.co/wps/portal/udea/web/inicio/unidades-academicas/ciencias-economicas/']

    def parse(self, response):
        pass
