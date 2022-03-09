import scrapy


class Fra0042Spider(scrapy.Spider):
    name = 'fra_0042'
    allowed_domains = ['https://fasest.univ-lille.fr/']
    start_urls = ['http://https://fasest.univ-lille.fr//']

    def parse(self, response):
        pass
