import scrapy


class Fra0028Spider(scrapy.Spider):
    name = 'fra_0028'
    allowed_domains = ['https://international.icn-artem.com/']
    start_urls = ['http://https://international.icn-artem.com//']

    def parse(self, response):
        pass
