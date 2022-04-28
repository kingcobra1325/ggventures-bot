import scrapy


class Col0006Spider(scrapy.Spider):
    name = 'col_0006'
    allowed_domains = ['http://fce.unal.edu.co/']
    start_urls = ['http://http://fce.unal.edu.co//']

    def parse(self, response):
        pass
