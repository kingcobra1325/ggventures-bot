import scrapy


class Usa0058Spider(scrapy.Spider):
    name = 'usa_0058'
    allowed_domains = ['https://lallyschool.rpi.edu/']
    start_urls = ['http://https://lallyschool.rpi.edu//']

    def parse(self, response):
        pass
