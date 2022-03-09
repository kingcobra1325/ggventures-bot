import scrapy


class Fra0037Spider(scrapy.Spider):
    name = 'fra_0037'
    allowed_domains = ['https://www.excelia-group.com/']
    start_urls = ['http://https://www.excelia-group.com//']

    def parse(self, response):
        pass
