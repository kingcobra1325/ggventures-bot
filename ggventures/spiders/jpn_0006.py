import scrapy


class Jpn0006Spider(scrapy.Spider):
    name = 'jpn_0006'
    allowed_domains = ['https://www.iuj.ac.jp/']
    start_urls = ['http://https://www.iuj.ac.jp//']

    def parse(self, response):
        pass
