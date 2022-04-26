import scrapy


class Lka0001Spider(scrapy.Spider):
    name = 'lka_0001'
    allowed_domains = ['https://mgmt.cmb.ac.lk/']
    start_urls = ['http://https://mgmt.cmb.ac.lk//']

    def parse(self, response):
        pass
