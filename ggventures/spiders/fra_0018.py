import scrapy


class Fra0018Spider(scrapy.Spider):
    name = 'fra_0018'
    allowed_domains = ['https://www.excelia-group.com/']
    start_urls = ['http://https://www.excelia-group.com//']

    def parse(self, response):
        pass
