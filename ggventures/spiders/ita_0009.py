import scrapy


class Ita0009Spider(scrapy.Spider):
    name = 'ita_0009'
    allowed_domains = ['https://businessschool.luiss.it/en/']
    start_urls = ['http://https://businessschool.luiss.it/en//']

    def parse(self, response):
        pass
