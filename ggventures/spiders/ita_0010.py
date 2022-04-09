import scrapy


class Ita0010Spider(scrapy.Spider):
    name = 'ita_0010'
    allowed_domains = ['https://mib.edu/']
    start_urls = ['http://https://mib.edu//']

    def parse(self, response):
        pass
