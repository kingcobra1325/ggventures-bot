import scrapy


class Usa0070Spider(scrapy.Spider):
    name = 'usa_0070'
    allowed_domains = ['https://www.gsb.stanford.edu/']
    start_urls = ['http://https://www.gsb.stanford.edu//']

    def parse(self, response):
        pass
