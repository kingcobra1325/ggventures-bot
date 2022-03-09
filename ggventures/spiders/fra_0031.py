import scrapy


class Fra0031Spider(scrapy.Spider):
    name = 'fra_0031'
    allowed_domains = ['https://www.inseec.education/']
    start_urls = ['http://https://www.inseec.education//']

    def parse(self, response):
        pass
