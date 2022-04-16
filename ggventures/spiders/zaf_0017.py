import scrapy


class Zaf0017Spider(scrapy.Spider):
    name = 'zaf_0017'
    allowed_domains = ['https://www.usb.ac.za/']
    start_urls = ['http://https://www.usb.ac.za//']

    def parse(self, response):
        pass
