import scrapy


class Gbr0003Spider(scrapy.Spider):
    name = 'gbr_0003'
    allowed_domains = ['https://www.aston.ac.uk/bss/aston-business-school']
    start_urls = ['http://https://www.aston.ac.uk/bss/aston-business-school/']

    def parse(self, response):
        pass
