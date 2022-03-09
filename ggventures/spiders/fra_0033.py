import scrapy


class Fra0033Spider(scrapy.Spider):
    name = 'fra_0033'
    allowed_domains = ['https://www.ipag.edu/en']
    start_urls = ['http://https://www.ipag.edu/en/']

    def parse(self, response):
        pass
