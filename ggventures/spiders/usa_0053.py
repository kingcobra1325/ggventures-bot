import scrapy


class Usa0053Spider(scrapy.Spider):
    name = 'usa_0053'
    allowed_domains = ['https://www.kellogg.northwestern.edu/']
    start_urls = ['http://https://www.kellogg.northwestern.edu//']

    def parse(self, response):
        pass
