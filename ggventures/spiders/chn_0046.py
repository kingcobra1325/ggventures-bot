import scrapy


class Chn0046Spider(scrapy.Spider):
    name = 'chn_0046'
    allowed_domains = ['https://www.xmu.edu.my/']
    start_urls = ['http://https://www.xmu.edu.my//']

    def parse(self, response):
        pass
