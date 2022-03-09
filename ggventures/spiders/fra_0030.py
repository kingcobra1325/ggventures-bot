import scrapy


class Fra0030Spider(scrapy.Spider):
    name = 'fra_0030'
    allowed_domains = ['https://www.insead.edu/']
    start_urls = ['http://https://www.insead.edu//']

    def parse(self, response):
        pass
