import scrapy


class Bra0010Spider(scrapy.Spider):
    name = 'bra_0010'
    allowed_domains = ['https://www.best-masters.com/master-at-pontificia-universidade-catolica-do-parana-pucpr-escola-de-negocios.html']
    start_urls = ['http://https://www.best-masters.com/master-at-pontificia-universidade-catolica-do-parana-pucpr-escola-de-negocios.html/']

    def parse(self, response):
        pass
