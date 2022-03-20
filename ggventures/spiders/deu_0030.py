import scrapy


class Deu0030Spider(scrapy.Spider):
    name = 'deu_0030'
    allowed_domains = ['https://www.uni-passau.de/en/msc-busadmin/']
    start_urls = ['http://https://www.uni-passau.de/en/msc-busadmin//']

    def parse(self, response):
        pass
