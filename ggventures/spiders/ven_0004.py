import scrapy


class Ven0004Spider(scrapy.Spider):
    name = 'ven_0004'
    allowed_domains = ['https://www.dcea.usb.ve/']
    start_urls = ['http://https://www.dcea.usb.ve//']

    def parse(self, response):
        pass
