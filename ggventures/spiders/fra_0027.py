import scrapy


class Fra0027Spider(scrapy.Spider):
    name = 'fra_0027'
    allowed_domains = ['https://www.hec.edu/en']
    start_urls = ['http://https://www.hec.edu/en/']

    def parse(self, response):
        pass
