import scrapy


class Fra0022Spider(scrapy.Spider):
    name = 'fra_0022'
    allowed_domains = ['https://eslsca.edu.eg/']
    start_urls = ['http://https://eslsca.edu.eg//']

    def parse(self, response):
        pass
