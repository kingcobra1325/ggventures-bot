import scrapy


class Fra0034Spider(scrapy.Spider):
    name = 'fra_0034'
    allowed_domains = ['https://www.groupeisc.com/en/']
    start_urls = ['http://https://www.groupeisc.com/en//']

    def parse(self, response):
        pass
