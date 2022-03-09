import scrapy


class Fra0019Spider(scrapy.Spider):
    name = 'fra_0019'
    allowed_domains = ['https://www.escp.eu/']
    start_urls = ['http://https://www.escp.eu//']

    def parse(self, response):
        pass
